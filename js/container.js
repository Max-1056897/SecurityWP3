var modal = document.getElementById("myModal");
var button = document.getElementById("myButton");
var close = document.getElementsByClassName("close")[0];

button.onclick = function() {
  modal.style.display = "block";
}

close.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
