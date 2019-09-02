jQuery(function() {
    $( ".column" ).sortable({
        connectWith: ".column",
        handle: '.card',
        forcePlaceholderSize: true,
        cursor: "move",
        cancel: ".unsort, .tab-content",
        helper: 'clone',
        stop: function( event, ui ) {
            var pos = [];
            $('.column').each(function(){
                var col = [];
                $(this).find('.card').each(function(){
                    col.push($(this).attr('id'));
                });
                pos.push(col.join(','));
            });
            var pos_val = pos.join('|');
            var key = $('#_portal_key').val();
            $.save_user_settings(key, pos_val, function(){
                //alert('success');
            });
        }
    });
    var callback = function() {
        $( this ).find('.icon.chevron').toggleClass( "fa fa-chevron-up" ).toggleClass( "fa fa-chevron-down" );
    };
    // It guarantees that the event will not be registered twice and with that when the
    // quick-form plugin is called make the main form get strange behavior.
    $(".card-header .btn.btn-link" ).unbind("click").click(callback);
});
