var modal = document.getElementById("myModal");
var l_modal = document.getElementById("logoutModal");


var btn = document.getElementById("myBtn");
var l_btn = document.getElementById("logout-link");

var span = document.getElementsByClassName("close")[0];
var l_span = document.getElementsByClassName("close")[1];

btn.onclick = function () {
  modal.style.display = "block";
  l_modal.style.display = "none";
}
l_btn.onclick = function () {
  modal.style.display = "none";
  l_modal.style.display = "block";
}
span.onclick = function () {
  modal.style.display = "none";
}
l_span.onclick = function () {
  l_modal.style.display = "none";
}
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  if (event.target == l_modal) {
    l_modal.style.display = "none";
  }
}