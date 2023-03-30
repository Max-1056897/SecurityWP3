// leerling inloggen formulier validatie
var leerlingForm = document.querySelector("#leerling-form");
if (leerlingForm) {
  leerlingForm.addEventListener("submit", function(event) {
    var gebruikersnaamInput = document.querySelector("#leerling-gebruikersnaam");
    var wachtwoordInput = document.querySelector("#leerling-wachtwoord");
    var error = false;

    if (!gebruikersnaamInput.value) {
      gebruikersnaamInput.classList.add("is-invalid");
      error = true;
    } else {
      gebruikersnaamInput.classList.remove("is-invalid");
    }

    if (!wachtwoordInput.value) {
      wachtwoordInput.classList.add("is-invalid");
      error = true;
    } else {
      wachtwoordInput.classList.remove("is-invalid");
    }

    if (error) {
      event.preventDefault();
    }
  });
}

// docent inloggen formulier validatie
var docentForm = document.querySelector("#docent-form");
if (docentForm) {
  docentForm.addEventListener("submit", function(event) {
    var gebruikersnaamInput = document.querySelector("#docent-gebruikersnaam");
    var wachtwoordInput = document.querySelector("#docent-wachtwoord");
    var error = false;

    if (!gebruikersnaamInput.value) {
      gebruikersnaamInput.classList.add("is-invalid");
      error = true;
    } else {
      gebruikersnaamInput.classList.remove("is-invalid");
    }

    if (!wachtwoordInput.value) {
      wachtwoordInput.classList.add("is-invalid");
      error = true;
    } else {
      wachtwoordInput.classList.remove("is-invalid");
    }

    if (error) {
      event.preventDefault();
    }
  });
}

// LEERLINGDASHBOARD
$(document).ready(function() {
    $("input[type='checkbox']").on("change", function() {
      var form = $(this).closest("form");
      form.submit();
    });
  });
  