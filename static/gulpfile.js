var gulp = require('gulp');
var sass = require('gulp-sass')(require('sass'));
var sourcemaps = require("gulp-sourcemaps");
var connect = require('gulp-connect');
var minify = require('gulp-minify');
var browserSync = require("browser-sync").create();
var exec = require('child_process').exec;

const SOURCE =  ['scss/*.scss', '!scss/bootstrap.scss'];
const DESTINATION = 'css/';


gulp.task('browserSync', function() {
     browserSync.init({
         proxy: {
             target: '127.0.0.1:8000'
         }
     });
});


gulp.task('sass', function(){
    return gulp.src(SOURCE)      
      .pipe(sourcemaps.init())
      .pipe(sass({outputStyle: 'compressed'})) // Using gulp-sass
      .pipe(sourcemaps.write())
      .pipe(gulp.dest(DESTINATION))
      .pipe(browserSync.reload({ stream: true }));
  });
gulp.task('sassboot', function(){
    return gulp.src('scss/bootstrap.scss')
      .pipe(sourcemaps.init())
      .pipe(sass({outputStyle: 'compressed'}))
      .pipe(sourcemaps.write())
      .pipe(gulp.dest(DESTINATION))
      .pipe(browserSync.reload({ stream: true }));
  });


gulp.task('jsmin', function() {
  gulp.src(['src/js/*.js'])
    .pipe(minify())
    .pipe(gulp.dest('build/js/'))
});

gulp.task('watch',  gulp.parallel('browserSync', function(){
    gulp.watch(['scss/commons/*.scss'], gulp.parallel('sass', 'sassboot'));
    gulp.watch(['scss/bootstrap.scss', 'scss/bootstrap/**/*.scss'], gulp.parallel('sassboot'));
    gulp.watch(['scss/**/*.scss','!scss/bootstrap.scss','!scss/commons/*.scss'], gulp.series(['sass']));
    // gulp.watch('js/*.js', gulp.series(['jsmin']));
}));


gulp.task('default', 
  gulp.series('sass', 'sassboot')
);