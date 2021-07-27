
import copy
from django import forms
from django.db import models
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.forms.models import modelform_factory
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _, ugettext_lazy
from xadmin.layout import FormHelper, Layout, Fieldset, Container, Col
from xadmin.plugins.actions import BaseActionView, ACTION_CHECKBOX_NAME
from xadmin.util import model_ngettext, vendor
from xadmin.views.base import filter_hook
from xadmin.views.edit import ModelFormAdminView

BATCH_CHECKBOX_NAME = '_batch_change_fields'


class ChangeFieldWidgetWrapper(forms.Widget):

    def __init__(self, widget):
        super(ChangeFieldWidgetWrapper, self).__init__(attrs=widget.attrs)
        self.needs_multipart_form = widget.needs_multipart_form
        self.choices = getattr(widget, 'choices', None)
        self.widget = widget

    def __deepcopy__(self, memo):
        obj = copy.copy(self)
        obj.widget = copy.deepcopy(self.widget, memo)
        obj.attrs = self.widget.attrs
        memo[id(self)] = obj
        return obj

    @property
    def media(self):
        media = self.widget.media + vendor('xadmin.plugin.batch.js')
        return media

    def render(self, name, value, attrs=None, **kwargs):
        output = []
        self.widget.choices = self.choices
        is_required = self.widget.is_required
        output.append(u'<div class="btn-group-toggle"><label class="btn btn-secondary">'
            '<input type="checkbox" class="batch-field-checkbox" name="%s" value="%s"%s/> %s</label>' %
            (BATCH_CHECKBOX_NAME, name, (is_required and ' checked="checked"' or ''), _('Change this field')))
        output.extend([('<div class="control-wrap batch-field-wrap mt-2" style="%s" id="id_%s_wrap_container">' %
            ((not is_required and 'display: none;' or ''), name)),
            self.widget.render(name, value, attrs), '</div></div>'])
        return mark_safe(u''.join(output))

    def build_attrs(self, extra_attrs=None, **kwargs):
        "Helper function for building an attribute dictionary."
        self.attrs = self.widget.build_attrs(extra_attrs=None, **kwargs)
        return self.attrs

    def value_from_datadict(self, data, files, name):
        return self.widget.value_from_datadict(data, files, name)

    def id_for_label(self, id_):
        return self.widget.id_for_label(id_)


class BatchChangeAction(BaseActionView):

    action_name = "change_selected"
    description = ugettext_lazy('Batch Change selected %(verbose_name_plural)s')
    batch_change_form_template = None
    model_perm = 'change'

    batch_fields = []
    batch_fields_exclude = []

    def init_action(self, list_view):
        super().init_action(list_view)
        self.edit_view = self.get_model_view(ModelFormAdminView, self.model)
        self.save_form_post = bool(self.request.POST.get('post'))

    def change_models(self, queryset, cleaned_data):
        n = queryset.count()

        data = {}
        fields = self.opts.fields + self.opts.many_to_many
        for field in fields:
            # [declared_fields] It has a custom field overlapping the pattern.
            if not field.editable or isinstance(field, models.AutoField) \
                    or field.name not in cleaned_data or \
                    field.name in self.form_obj.declared_fields:
                continue
            data[field] = cleaned_data[field.name]

        # custom declared fields
        for field_name in self.form_obj.declared_fields:
            field = self.form_obj.fields.get(field_name)
            if field and field_name in cleaned_data and field_name not in data:
                data[field] = cleaned_data[field_name]

        if n:
            for obj in queryset:
                for field, v in data.items():
                    field.save_form_data(obj, v)
                obj.save()
            self.message_user(_("Successfully change %(count)d %(items)s.") % {
                "count": n, "items": model_ngettext(self.opts, n)
            }, 'success')

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = self.edit_view.formfield_for_dbfield(db_field,
                                                         required=self.save_form_post,
                                                         **kwargs)
        formfield.widget = ChangeFieldWidgetWrapper(formfield.widget)
        return formfield

    def get_change_form(self, fields):
        batch_form = getattr(self.edit_view, "batch_form", self.edit_view.form)
        defaults = {
            "form": batch_form,
            "fields": fields,
            "formfield_callback": self.formfield_for_dbfield,
            "exclude": getattr(self.edit_view, "batch_fields_exclude", ())
        }
        return modelform_factory(self.model, **defaults)

    @staticmethod
    def formfield_for_declared(form, fields):
        """Processes declared fields that are not in the model"""
        for field_name in form.declared_fields:
            if field_name not in fields:
                continue
            field = form.fields.get(field_name)
            if field and not isinstance(field.widget, ChangeFieldWidgetWrapper):
                if not hasattr(field, 'save_form_data'):
                    raise ImproperlyConfigured("Custom fields need to implement "
                                               "the 'save_form_data(self, obj, value)' "
                                               "method in order to update instances.")
                field.widget = ChangeFieldWidgetWrapper(field.widget)
        return form

    @staticmethod
    def formfield_declared_in_post(form, fields):
        """Keep only declared fields sent in the post"""
        for field_name in form.declared_fields:
            if field_name not in fields and field_name in form.fields:
                del form.fields[field_name]
        return form

    def do_action(self, queryset):
        if not self.has_change_permission():
            raise PermissionDenied

        change_fields = [field for field in self.request.POST.getlist(BATCH_CHECKBOX_NAME)
                         if field in self.batch_fields]

        if change_fields and self.save_form_post:
            form = self.get_change_form(change_fields)(data=self.request.POST,
                                                       files=self.request.FILES)
            self.form_obj = self.formfield_declared_in_post(form, change_fields)
            if self.form_obj.is_valid():
                self.change_models(queryset, self.form_obj.cleaned_data)
                return None
        else:
            form = self.get_change_form(self.batch_fields)()
            # Support for declared fields but without affecting field inheritance.
            self.form_obj = self.formfield_for_declared(form, self.batch_fields)

        helper = FormHelper()
        helper.form_tag = False
        helper.include_media = False
        helper.use_custom_control = False
        helper.add_layout(Layout(Container(Col('full',
            Fieldset("", *self.form_obj.fields.keys(), css_class="unsort no_title"), horizontal=True, span=12)
        )))
        self.form_obj.helper = helper
        count = len(queryset)
        if count == 1:
            objects_name = force_text(self.opts.verbose_name)
        else:
            objects_name = force_text(self.opts.verbose_name_plural)

        context = self.get_context()
        context.update({
            "title": _("Batch change %s") % objects_name,
            'objects_name': objects_name,
            'form': self.form_obj,
            'queryset': queryset,
            'count': count,
            "opts": self.opts,
            "app_label": self.app_label,
            'action_checkbox_name': ACTION_CHECKBOX_NAME,
        })

        return TemplateResponse(self.request, self.batch_change_form_template or
                                self.get_template_list('views/batch_change_form.html'), context)

    @filter_hook
    def get_media(self):
        media = super(BatchChangeAction, self).get_media()
        media = media + self.form_obj.media + self.vendor(
            'xadmin.page.form.js', 'xadmin.form.css')
        return media
