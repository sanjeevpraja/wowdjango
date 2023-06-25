$(document).ready(function () {
  $('.notification').on('click', function () {
    $('.flex-pane').toggleClass('active');
  });
  $('.flex-pane .close').on('click', function () {
    $('.flex-pane').toggleClass('active');
  });
});