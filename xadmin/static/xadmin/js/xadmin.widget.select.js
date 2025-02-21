;(function($){
    // add select render
    $.fn.exform.renders.push(function(f){
      if($.fn.selectize){
        f.find('select:not(.select-search):not(.selectize-off):not([multiple=multiple])').selectize();
        f.find('.select-search').each(function(){
            var $el = $(this);
            var preload = $el.hasClass('select-preload');
            $el.selectize({
                valueField: 'id',
                labelField: '__str__',
                searchField: '__str__',
                create: false,
                maxItems: 1,
                preload: preload,
                load: function(query, callback) {
                    if(!preload && !query.length) return callback();
                    $.ajax({
                        url: $el.data('search-url')+$el.data('choices'),
                        dataType: 'json',
                        data: {
                            '_q_' : query,
                            '_cols': 'id.__str__'
                        },
                        type: 'GET',
                        error: function() {
                            callback();
                        },
                        success: function(res) {
                            var objects = null;
                            if (window.hasOwnProperty("__admin_object_id__")) {
                                var object_id = window.__admin_object_id__;
                                objects = [];
                                $.each(res.objects, function (idx, item) {
                                    if (object_id !== item.id) {
                                        objects.push(item);
                                    }
                                });
                            } else {
                                objects = res.objects;
                            }
                            callback(objects);
                        }
                    });
                }
            });
        })
    }});
})(jQuery)

