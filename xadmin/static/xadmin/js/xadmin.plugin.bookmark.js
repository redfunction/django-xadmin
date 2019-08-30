(function($) {

  $(function(){
    $('#bookmark_form').each(function(){
      var f = $(this);
      f.submit(function(e){
        f.find('button[type=submit]').button('loading');
        $.post(f.attr('action'), f.serialize(), function(data){
          $('#bookmark-menu .add-bookmark').remove();
          $('#bookmark-menu').append('<a class="dropdown-item" href="'+ data.url +'" title="'+ data.title +'"><i class="fa fa-bookmark"></i> '+ data.title +'</a>');
        }, 'json');
        return false;
      });
    });
  });

})(jQuery);