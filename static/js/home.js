var number = document.getElementById('number');
var form = document.getElementsByTagName('form')[0];
number.addEventListener('blur', function(){ checkNumber(); }, false);
form.addEventListener('submit', function(event){ checkForm(event); }, false);

function checkNumber() {
    span = document.getElementsByClassName('error')[0];
    if (number.value < 1 || !number.value) {
        span.textContent = "Please pick how many tracks you would like in your playlist";
    }
    else if (number.value > 25) {
        span.textContent = "Number of tracks cannot exceed 25";
        number.value = null;
    }
    else {
        span.textContent = "";
    }
}

function checkForm(e) {
    checkNumber();

    span = document.getElementsByClassName('error')[0];

    if (span.textContent != "") {
        e.preventDefault();
    }
}