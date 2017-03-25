
//Variables
var iframe = document.getElementsByTagName('iframe');
var content = document.getElementsByClassName('data');

foreach (data in content) {
    data.addEventListener('click', pickSong(event), false);
}

function pickSong(e) {
    var div = e.target();
    
    var blah = document.getElementById('cock');

    foreach (data in content) {
        data.style(background-color: black;)
    }

    var uri = blah.textContent;
    var url = "https://embed.spotify.com/?uri=" . uri
    iframe.src(url);
}