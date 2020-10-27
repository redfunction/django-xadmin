(function($) {
  $(function(){
    if($("#g-theme-menu")){
      $('#g-theme-menu a').click(function(){
        var top_nav = $('#top-nav');
        var $el = $(this);
        var themeHref = $el.data('css-href');
        
        var topmenu = $('#top-nav .navbar-collapse');
        if(topmenu.data('bs.collapse')) topmenu.collapse('hide');

        var modal = $("#nunjuks-modal-main").template_render$({
            header: {title: gettext('Loading theme')},
            modal: {id: 'load-theme-modal', size: 'modal-md',},
            body: '<h2 style="text-align:center;"><i class="fa-spinner fa-spin fa fa-large"></i></h2>',
            footer: '&nbsp'
          }).appendTo('body');

        modal.on('shown.bs.modal', function(){
          $.save_user_settings("site-theme", themeHref, function(){
            $.setCookie('_theme', themeHref);

            var $iframe = $("<iframe>");
            $iframe.css("display", 'none');
            $iframe.appendTo(document.body);

            modal.on('hidden', function(e) {
              modal.remove();
            });

            $iframe.on("load", function () {
              $('#site-theme').attr('href', themeHref);

              setTimeout(function(){
                var nav_height = top_nav.outerHeight();
                $('#body-content').animate({'margin-top': (nav_height + 10)}, 500, 'easeOutBounce');
              }, 500);

              modal.modal('hide');
              $iframe.remove();
            });

            $iframe.attr('src', window.location.href);
            $iframe.append('<!doctype><html><head></head><body>');
            $iframe.append('<link rel="stylesheet" href="'+themeHref+'" />');
            $iframe.append('</body></html>');

            // option selected
            $el.parent().find("a").removeClass('active');
            $el.addClass('active');
          });
        });

        modal.modal().css(
            {
                'margin-top': function () {
                    return window.pageYOffset;
                }
            });
      })
    }
  });

})(jQuery);