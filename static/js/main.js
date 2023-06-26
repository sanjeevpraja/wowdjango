$(document).ready(function () {
    $('.notification').on('click', function () {
        $('.flex-pane').toggleClass('active');
    });
    $('.flex-pane .close').on('click', function () {
        $('.flex-pane').toggleClass('active');
    });
});
$(document).on('click', '.btn-add', function (e) {
    e.preventDefault();
    let parent = $(this).siblings('.box-steps');
    let step = parent.find('.box-step').first();
    parent.append(step.first().clone());
});
$(document).on('click', '.btn-delete', function (e) {
    e.preventDefault();
    $(this).closest('.box-step').remove();
});