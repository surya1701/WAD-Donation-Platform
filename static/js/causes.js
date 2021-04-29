function causes_show(c) {
    var causes = document.getElementsByClassName("acause");
    for (var i = 0; i < causes.length; i++) {
        causes[i].style.display = 'none';
    }
    causes = document.getElementsByClassName(c);
    for (var i = 0; i < causes.length; i++) {
        causes[i].style.display = 'inline';
    }
}