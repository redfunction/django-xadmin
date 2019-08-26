var gulp = require('gulp');

function genericTask() {
    var srcs = [
        "bower_components/**/css/*.css",
        "bower_components/**/css/*.less",
        "bower_components/**/js/*.js",
        "bower_components/**/locales/*.js",
        "bower_components/**/img/**",
        "!bower_components/flot/**",
        "!bower_components/datejs/**",
        "!bower_components/bootstrap-datepicker/js/**",
        "!bower_components/sifter/**",
        "!bower_components/bootstrap/**",
        "!bower_components/**/src/**",
        "!bower_components/**/jquery/**",
        "!bower_components/**/jquery.js",
        "!bower_components/**/js-packages/**",
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
    return gulp.src("bower_components/flot/src/*.js")
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

function datejsTask() {
    return gulp.src("bower_components/datejs/src/**")
        .pipe(gulp.dest('vendor/datejs/js'));
}

function jqueryUITask() {
    var srcs = [
        "bower_components/jquery-ui/**/core.js",
        "bower_components/jquery-ui/**/effect.js",
        "bower_components/jquery-ui/**/widget.js",
    ];
    return gulp.src(srcs)
        .pipe(gulp.dest('vendor/jquery-ui'));
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
    datejsTask,
    jqueryUITask,
    bootstrapTask
);
