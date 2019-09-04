
/* Engine that loads templates attached to body */

function JqueryTemplateEngine(options) {
    this.options = $.extend({noCache: true}, options);
}

JqueryTemplateEngine.prototype.getSource = function (name) {
    // load the template
    // return an object with:
    //   - src:     String. The template source.
    //   - path:    String. Path to template.
    //   - noCache: Bool. Don't cache the template (optional).
    var $ele = $(name);
    var text = $ele.text();
    return {
        src: text,
        path: name,
        noCache: this.options.noCache
    }
};

$.fn.nujunks_env = new nunjucks.Environment(new JqueryTemplateEngine({}));

$.fn.template_render = function (ctx) {
    return $.fn.nujunks_env.render("#" + this.attr('id'), ctx);
}

$.fn.template_render$ = function (ctx, options) {
    return $($.proxy($.fn.template_render, this)(ctx, options));
}