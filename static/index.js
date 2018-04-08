var config = {
    apiKey: "AIzaSyBryG57RvSSjAUCwBPhD8rgSYulgifYP8I",
    authDomain: "facebookhackatonparis.firebaseapp.com",
    databaseURL: "https://facebookhackatonparis.firebaseio.com",
    projectId: "facebookhackatonparis",
    storageBucket: "facebookhackatonparis.appspot.com",
    messagingSenderId: "115421883193"
};
firebase.initializeApp(config);

var database = firebase.database();


var playListRef = database.ref('playlist/').orderByChild("votes");
playListRef.on('value', function(snapshot) {
    updatePlaylist(snapshot);
});

function updatePlaylist(snap) {
    var table = document.getElementById("table");
    table.innerHTML = "";
    snap.forEach(function(childSnapshot) {
        var row = '';
        votes = childSnapshot.val().votes;
        songName = childSnapshot.val().name;
        artist = childSnapshot.val().artist;
        var x = table.insertRow(0);
        var x1 = x.insertCell();
        x1.innerHTML = songName;
        var x2 = x.insertCell();
        x2.innerHTML = artist;
        var x3 = x.insertCell();
        x3.innerHTML = votes;
        x.onclick = function () {
            firebase.database().ref('playlist/' + childSnapshot.key + '/votes').set(childSnapshot.val().votes + 1);
        }
    });
}
