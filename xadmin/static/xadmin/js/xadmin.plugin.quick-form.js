
;(function($){

  $('form.widget-form').on('post-success', function(e, data){
    $(this).data('ajaxform').clean();
    $('.alert-success #change-link').attr('href', data['change_url']);
    $('.alert-success').show()
  });

  var AjaxForm = function(element, options) {
    var that = this;

    this.$form = $(element);
    this.ainit()
  }

  AjaxForm.prototype = {

    constructor: AjaxForm

    , ainit: function(){
      this.$mask = $('<div class="mask"><h1 style="text-align:center;"><i class="fa-spinner fa-spin fa fa-large"></i></h1></div>')

      this.$form.prepend(this.$mask);
      this.$form.submit($.proxy(this.submit, this));

      this.$form.find('input, select, textarea').each(function(){
        var el = $(this);
        if (el.is("[type=checkbox]")) {
          el.data('init-value', el.attr('checked'))
        } else if (el.is("select")) {
          el.data('init-value', el[0].selectedIndex)
        } else {
          el.data('init-value', el.val())
        }
      })
    }

    , clean: function(){
      this.$form.find('input, select, textarea').each(function(){
        var el = $(this);
        if (el.is("[type=checkbox]")) {
          el.removeAttr('checked')
        } else if (el.is("select")) {
          el[0].selectedIndex = el.data('init-value')||0
        } else {
          el.val(el.data('init-value')||'')
        }
        el.change()
      })
    }

    , submit: function(e) {
        e.stopPropagation();
        e.preventDefault();

        $.when(this.save())
        .done($.proxy(function(data) {
          this.$mask.hide();

          this.$form.find('submit, button[type=submit], input[type=submit]').removeClass('disabled');
          this.$form.find('.alert-success').hide();

          if(data['result'] !== 'success' && data['errors']){
            var err_html, index, non_fields_errors = [];
            for (index = data['errors'].length - 1; index >= 0; index--) {
              var error = data['errors'][index];
              var errdiv = this.$form.find('#div_' + error['id']);
              if(errdiv.length){
                errdiv.addClass('has-error');
                err_html = [];
                var err_id;
                for (var j = error['errors'].length - 1; j >= 0; j--) {
                  err_id = 'error_' + j + '_' + error['id'];

                  // Prevent the message from being repeated several times.
                  errdiv.find("#"+err_id).remove();

                  err_html.push('<span id="'+ err_id + '" class="text-danger">' + error['errors'][j] + '</span>')
                }
                errdiv.find('.controls').append(err_html.join('\n'))
              } else {
                non_fields_errors = non_fields_errors.concat(error['errors'])
              }
            }
            if(non_fields_errors.length){
              err_html = [];
              for (index = non_fields_errors.length - 1; index >= 0; index--) {
                err_html.push('<p class="text-danger"><strong>'+error['errors'][index]+'</strong></p>')
              }
              this.$form.prepend(err_html.join('\n'))
            }
          } else {
            this.$form.trigger('post-success', data);
          }
        }, this))
        .fail($.proxy(function(xhr) {
          this.$mask.hide();
          alert(typeof xhr === 'string' ? xhr : xhr.responseText || xhr.statusText || 'Unknown error!');
        }, this));
    }
    , save: function(newValue) {

      this.$form.find('.text-error, .help-inline.error').remove();
      this.$form.find('.control-group').removeClass('error');

      this.$mask.show();
      this.$form.find('submit, button[type=submit], input[type=submit]').addClass('disabled');

      var off_check_box = Object();
      // this.$form.find('input[type=checkbox]').each(function(){
      //   if(!$(this).attr('checked')){
      //     off_check_box[$(this).attr('name')] = '';
      //   }
      // })

      var $nonfile_input = this.$form.serializeArray();

      var formData = new FormData();

      $nonfile_input.forEach(function(field) {
        formData.append(field.name, field.value)
      });

      var $file_input = this.$form.find("input[type=file]");
      $file_input.each(function (idx, file) {
        formData.append($(file).attr('name'), file.files[0]);
      });

      return $.ajax({
        data: formData,
        url: this.$form.attr('action'),
        type: "POST",
        dataType: 'json',
        contentType: false,
        processData: false,
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.getCookie('csrftoken'));
        }
      })
    },
  }

  $.fn.ajaxform = function ( option ) {
    var args = Array.apply(null, arguments);
    args.shift();
    return this.each(function () {
      var $this = $(this),
        data = $this.data('ajaxform'),
        options = typeof option == 'object' && option;
      if (!data) {
        $this.data('ajaxform', (data = new AjaxForm(this)));
      }
    });
  };

  $.fn.ajaxform.Constructor = AjaxForm;

  $.fn.exform.renders.push(function(f){
    if (f.is('.quick-form')) {
      f.ajaxform()
    }
  });

  var QuickAddBtn = function(element, options) {
    var that = this;

    this.$btn = $(element);
    this.add_url = this.$btn.attr('href');
    this.$for_input = $('#' + this.$btn.data('for-id'));
    this.$for_wrap = $('#' + this.$btn.data('for-id') + '_wrap_container');
    this.refresh_url = this.$btn.data('refresh-url');
    this.rendered_form = false;

    this.binit(element, options);
  }

  QuickAddBtn.prototype = {

     constructor: QuickAddBtn

    , binit: function(element, options){
      this.$btn.click($.proxy(this.click, this))
    }
    , click: function(e) {
      e.stopPropagation();
      e.preventDefault();

      if(!this.modal) {
        var modal = $("#nunjuks-modal-main").template_render$({
          header: {title: this.$btn.attr('title')},
          modal: {size: 'modal-xl'},
          confirm_button: {
            text: gettext('Add'),
            class: "btn-submit",
            icon: 'fa fa-plus',
            tag: 'a'
          },
        }).appendTo('body');
        var self = this;
        modal.find('.modal-body').html('<h2 style="text-align:center;"><i class="fa-spinner fa-spin fa fa-large"></i></h2>')
        modal.find('.modal-body').load(this.add_url, function(form_html, status, xhr){
          var form = $(this).find('form');
          form.addClass('quick-form');
          form.on('post-success', $.proxy(self.post, self));
          form.exform();

          modal.find('.modal-footer').show();
          modal.find('.btn-submit').click(function(){form.submit()});

          self.$form = form
        });
        this.modal = modal
      }
      this.modal.modal();

      return false
    }
    , post: function(e, data){
      this.$form.data('ajaxform').clean();
      var wrap = this.$for_wrap;
      var input = this.$for_input;
      var selected = [data['obj_id']];
      if (input.attr('multiple')){
        if (input.hasClass("select2-multiple")) {
          selected.push($("#" + input.attr("id")).val());
        } else {
          var opt = 'option';
          if (input.hasClass('selectdropdown') || input.hasClass('select-multi')) {
            opt = 'option:selected';
          }
          selected.push($.map(input.find(opt), function (opt) {
            return opt.value;
          }));
        }
      }
      $.get(this.refresh_url + selected.join() ,function(form_html, status, xhr){
        wrap.html($('<body>' + form_html + '</body>').find('#' + wrap.attr('id')).html());
        wrap.exform();
      });
      this.modal.modal('hide');
    }

  }

  $.fn.ajax_addbtn = function ( option ) {
    return this.each(function () {
      var $this = $(this), data = $this.data('ajax_addbtn');
      if (!data) {
          $this.data('ajax_addbtn', (data = new QuickAddBtn(this)));
      }
    });
  };

  $.fn.ajax_addbtn.Constructor = QuickAddBtn;

  $.fn.exform.renders.push(function(f){
    f.find('a.btn-ajax').ajax_addbtn()
  })

})(jQuery);
