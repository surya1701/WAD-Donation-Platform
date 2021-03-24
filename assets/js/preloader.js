$(window).on('load', function () {
    setTimeout(removeLoader, 1500);
});
function removeLoader() {
    $(".preloader").fadeOut(500, function () {
        $(".preloader").remove();
        $("#links-nav").css("opacity", "100");
    });
}