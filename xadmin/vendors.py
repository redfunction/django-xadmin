
vendors = {
    "bootstrap": {
        'js': {
            'dev': [
                'xadmin/vendor/bootstrap/js/bootstrap.bundle.js',
            ],
            'production': [
                'xadmin/vendor/bootstrap/bootstrap.bundle.min.js',
            ],
            'cdn': '"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js'
        },
        'css': {
            'dev': [
                'xadmin/vendor/bootstrap/css/bootstrap.css',
                'xadmin/vendor/bootstrap/css/bootstrap-reboot.css'
            ],
            'production': [
                'xadmin/vendor/bootstrap/css/bootstrap.css',
                'xadmin/vendor/bootstrap/css/bootstrap-reboot.min.css'
            ],
            'cdn': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'
        },
        'responsive': {
            'css': {
                'dev': 'xadmin/vendor/bootstrap/bootstrap-responsive.css',
                'production': 'xadmin/vendor/bootstrap/bootstrap-responsive.css'
            }}
    },
    'jquery': {
        "js": {
            'dev': 'xadmin/vendor/jquery/jquery.js',
            'production': 'xadmin/vendor/jquery/jquery.min.js',
        }
    },
    'nunjucks': {
        "js": {
            'dev': ['xadmin/vendor/nunjucks/nunjucks.js',
                    'xadmin/js/nunjucks.engine.js'],
            'production': ['xadmin/vendor/nunjucks/nunjucks.min.js',
                           'xadmin/js/nunjunks.engine.js'],
        }
    },
    'jquery-ui-effect': {
        "js": {
            'dev': 'xadmin/vendor/jquery-ui/ui/effect.js',
            'production': 'xadmin/vendor/jquery-ui/ui/minified/effect.js'
        }
    },
    'jquery-ui-sortable': {
        "js": {
            'dev': [
                'xadmin/vendor/jquery-ui/ui/widget.js',
                'xadmin/vendor/jquery-ui/ui/widgets/mouse.js',
                'xadmin/vendor/jquery-ui/ui/widgets/sortable.js'
            ],
            'production': [
                'xadmin/vendor/jquery-ui/ui/minified/widget.js',
                'xadmin/vendor/jquery-ui/ui/minified/mouse.js',
                'xadmin/vendor/jquery-ui/ui/widgets/sortable.js'
            ]
        }
    },
    "font-awesome": {
        "css": {
            'dev': [
                'xadmin/vendor/font-awesome/css/fontawesome.css',
                'xadmin/vendor/font-awesome/css/solid.css',
            ],
            'production': [

                'xadmin/vendor/font-awesome/css/fontawesome.min.css',
                'xadmin/vendor/font-awesome/css/solid.min.css',
            ]
        }
    },
    "timepicker": {
        "css": {
            'dev': 'xadmin/vendor/bootstrap-timepicker/css/bootstrap-timepicker.css',
            'production': 'xadmin/vendor/bootstrap-timepicker/css/bootstrap-timepicker.min.css',
        },
        "js": {
            'dev': 'xadmin/vendor/bootstrap-timepicker/js/bootstrap-timepicker.js',
            'production': 'xadmin/vendor/bootstrap-timepicker/js/bootstrap-timepicker.min.js',
        }
    },
    "clockpicker": {
        "css": {
            'dev': 'xadmin/vendor/clockpicker/dist/bootstrap-clockpicker.css',
            'production': 'xadmin/vendor/clockpicker/dist/bootstrap-clockpicker.min.css',
        },
        "js": {
            'dev': 'xadmin/vendor/clockpicker/dist/bootstrap-clockpicker.js',
            'production': 'xadmin/vendor/clockpicker/dist/bootstrap-clockpicker.min.js',
        }
    },
    "datepicker": {
        "css": {
            'dev': 'xadmin/vendor/bootstrap-datepicker/dist/css/bootstrap-datepicker.css'
        },
        "js": {
            'dev': 'xadmin/vendor/bootstrap-datepicker/dist/js/bootstrap-datepicker.js',
        }
    },
    "flot": {
        "js": {
            'dev': [
                'xadmin/vendor/flot/js/jquery.canvaswrapper.js',
                'xadmin/vendor/flot/js/jquery.flot.js',
                'xadmin/vendor/flot/js/jquery.flot.drawSeries.js',
                'xadmin/vendor/flot/js/jquery.colorhelpers.js',
                'xadmin/vendor/flot/js/jquery.flot.browser.js',
                'xadmin/vendor/flot/js/jquery.flot.uiConstants.js',
                'xadmin/vendor/flot/js/jquery.flot.saturated.js',
                'xadmin/vendor/flot/js/jquery.flot.pie.js',
                'xadmin/vendor/flot/js/jquery.flot.time.js',
                'xadmin/vendor/flot/js/jquery.flot.resize.js',
                'xadmin/vendor/flot/js/jquery.flot.aggregate.js',
                'xadmin/vendor/flot/js/jquery.flot.categories.js']
        }
    },
    "image-gallery": {
        "css": {
            'dev': 'xadmin/vendor/bootstrap-image-gallery/css/bootstrap-image-gallery.css',
            'production': 'xadmin/vendor/bootstrap-image-gallery/css/bootstrap-image-gallery.css',
        },
        "js": {
            'dev': ['xadmin/vendor/load-image/load-image.js', 'xadmin/vendor/bootstrap-image-gallery/js/bootstrap-image-gallery.js'],
            'production': ['xadmin/vendor/load-image/load-image.min.js', 'xadmin/vendor/bootstrap-image-gallery/js/bootstrap-image-gallery.js']
        }
    },
    "select": {
        "css": {
            'dev': ['xadmin/vendor/select2/dist/css/select2.css',
                    'xadmin/vendor/selectize/css/selectize.css',
                    'xadmin/vendor/selectize/css/selectize.bootstrap3.css'],
        },
        "js": {
            'dev': [
                'xadmin/vendor/selectize/js/standalone/selectize.js',
                'xadmin/vendor/select2/dist/js/select2.js',
                'xadmin/vendor/select2/dist/js/select2_locale_%(lang)s.js'],
            'production': [
                'xadmin/vendor/selectize/standalone/selectize.min.js',
                'xadmin/vendor/select2/dist/js/select2.min.js',
                'xadmin/vendor/select2/dist/js/select2_locale_%(lang)s.js']
            }
    },
    "multiselect": {
        "css": {
            'dev': 'xadmin/vendor/bootstrap-multiselect/css/bootstrap-multiselect.css',
        },
        "js": {
            'dev': 'xadmin/vendor/bootstrap-multiselect/js/bootstrap-multiselect.js',
        }
    },
    "snapjs": {
        "css": {
            'dev': 'xadmin/vendor/snapjs/snap.css',
        },
        "js": {
            'dev': 'xadmin/vendor/snapjs/snap.js',
        }
    },
}
