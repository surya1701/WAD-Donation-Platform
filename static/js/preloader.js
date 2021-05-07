$(window).on('load', function () {
    setTimeout(removeLoader, 500);
});
function removeLoader() {
    $(".preloader").fadeOut(500, function () {
        $(".preloader").css("display", "none");
        $("#links-nav").css("opacity", "100");
    });
}