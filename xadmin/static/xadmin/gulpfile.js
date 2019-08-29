var gulp = require('gulp');

function genericTask() {
    var srcs = [
        "bower_components/**/css/*.css",
        "bower_components/**/css/*.less",
        "bower_components/**/js/*.js",
        "bower_components/**/dist/*.css",
        "bower_components/**/dist/*.less",
        "bower_components/**/dist/*.js",
        "bower_components/**/locales/*.js",
        "bower_components/**/img/**",
        "!bower_components/font-awesome/**",
        "!bower_components/flot/**",
        "!bower_components/datejs/**",
        "!bower_components/bootstrap-datepicker/js/**",
        "!bower_components/selectize/**",
        "!bower_components/sifter/**",
        "!bower_components/bootstrap/**",
        "!bower_components/**/src/**",
        "!bower_components/**/jquery/**",
        "!bower_components/**/jquery.js",
        "!bower_components/**/docs/**",
    ];
    return gulp.src(srcs)
        .pipe(gulp.dest('vendor'));
}

function jqueryTask() {
    return gulp.src("bower_components/jquery/dist/**")
        .pipe(gulp.dest('vendor/jquery'));
}

function flotTask() {
    return gulp.src("bower_components/flot/source/*.js")
        .pipe(gulp.dest('vendor/flot/js'));

}

function micropluginTask() {
    return gulp.src("bower_components/microplugin/src/*.js")
        .pipe(gulp.dest('vendor/microplugin/js'));

}

function sifterTask() {
    return gulp.src("bower_components/sifter/*.js")
        .pipe(gulp.dest('vendor/sifter/js'));
}

function selectizeTask() {
    return gulp.src(["bower_components/selectize/dist/**/*.js",
        "bower_components/selectize/dist/**/*.css"])
        .pipe(gulp.dest('vendor/selectize'));
}

function datejsTask() {
    return gulp.src("bower_components/datejs/src/**")
        .pipe(gulp.dest('vendor/datejs/js'));
}

function jqueryUITask() {
    var srcs = [
        "bower_components/jquery-ui/**/core.js",
        "bower_components/jquery-ui/**/effect.js",
        "bower_components/jquery-ui/**/widget.js",
        "bower_components/jquery-ui/**/**/mouse.js",
        "bower_components/jquery-ui/**/**/sortable.js",
    ];
    return gulp.src(srcs)
        .pipe(gulp.dest('vendor/jquery-ui'));
}

function fontAwesomeTask() {
    var srcs = [
        "bower_components/font-awesome/**/*.js",
        "bower_components/font-awesome/**/*.css",
        "bower_components/font-awesome/**/otfs/**",
        "bower_components/font-awesome/**/webfonts/**",
        "!bower_components/font-awesome/js-packages/**",
    ];
    return gulp.src(srcs)
        .pipe(gulp.dest('vendor/font-awesome'));
}

function bootstrapTask() {
    var srcs = [
        "bower_components/bootstrap/dist/**/*.css",
        "bower_components/bootstrap/dist/**/*.js",
        "bower_components/bootstrap/js/dist/**",
        "!bower_components/bootstrap/build/**",
    ];
    return gulp.src(srcs)
        .pipe(gulp.dest('vendor/bootstrap'));
}

exports.default = gulp.series(
    genericTask,
    jqueryTask,
    flotTask,
    sifterTask,
    micropluginTask,
    fontAwesomeTask,
    selectizeTask,
    datejsTask,
    jqueryUITask,
    bootstrapTask
);
