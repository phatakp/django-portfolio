$(document).ready(function () {
    new WOW().init();
    $('.form-control').focus(function () {
        console.log($(this));
        $inputSelected = $(this);
        $inputSelected.attr('placeholder', '');
        $parentGroup = $inputSelected.parent().parent();
        $parentGroup.addClass('active');

    });
});