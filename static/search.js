var config = {
    apiKey: "AIzaSyBryG57RvSSjAUCwBPhD8rgSYulgifYP8I",
    authDomain: "facebookhackatonparis.firebaseapp.com",
    databaseURL: "https://facebookhackatonparis.firebaseio.com",
    projectId: "facebookhackatonparis",
    storageBucket: "facebookhackatonparis.appspot.com",
    messagingSenderId: "115421883193"
};
firebase.initializeApp(config);

function searchSongs(value) {
    console.log(value);
    if (value == "") return;
        $.ajax({
        url: "https://api.spotify.com/v1/search?q=" + value + "&type=track&market=US&limit=10&offset=0",
        beforeSend: function (jqXHR, settings) {
            jqXHR.setRequestHeader("Accept", "application/json");
            jqXHR.setRequestHeader("Content-Type", "application/json");
            jqXHR.setRequestHeader("Authorization", "Bearer BQDrNi3Loe_ZgXyZHnxETkfOFpJu0Of2TG6HgqVNrqgUwC0_ZUFB17WpvJBZ9MmK7ofay5N-OCkJkOfCN2c-Lv0Bi52i5PefarwyPbnv1nqVJt_sqBFXIgK7TOG2RXolzG2l6CyI9GcYc54HAmXOrGQWxQ");
        },
        success: function(result){
            updateTable(result);
        }
    });
}

function updateTable(obj) {
    var table = document.getElementById("table");
    var items = obj.tracks.items;
    table.innerHTML = "";
    for (var i = 0; i < items.length; i++) {
        var row = '';
        songName = items[i].name;
        artist = items[i].artists[0].name;
        id = items[i].id;
        duration_ms = items[i].duration_ms;
        var x = table.insertRow(0);
        var x1 = x.insertCell();
        x1.innerHTML = songName;
        var x2 = x.insertCell();
        x2.innerHTML = artist;
        x.id = id;
        x1.id = songName;
        x2.id = artist;
        x2.class = duration_ms;
        x.onclick = function () {
            firebase.database().ref('playlist/' + this.id).set({
                name: this.cells[0].id,
                artist: this.cells[1].id,
                votes: 1,
                duration_ms: x2.class
            });
        }
    }
}
