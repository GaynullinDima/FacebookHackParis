function searchSongs(value) {
    console.log(value);
    if (value == "") return;
        $.ajax({
        url: "https://api.spotify.com/v1/search?q=" + value + "&type=track&market=US&limit=10&offset=0",
        beforeSend: function (jqXHR, settings) {
            jqXHR.setRequestHeader("Accept", "application/json");
            jqXHR.setRequestHeader("Content-Type", "application/json");
            jqXHR.setRequestHeader("Authorization", "Bearer BQAeKLzwe-ehRvbK08GKkR4CL4YdJGIeqGEbh9J8RCfNb5ctlFU8jBXjAogv9Lvcpq9XsrF7dF-jXLRGk-yDoEeG8d06znAZelAVRbhMA189iH4yRYAQ6FeE7aiVSuKxheHQ5gfCCHJ8ujqXOxJDPlD8SA");
        },
        success: function(result){
            console.log(result);
            updateTable(result);
        }
    });
}

function updateTable(obj) {
    var html = '<tbody>';
    for (var i = 0; i < obj.tracks.items.length; i++) {
        html += '<td>' + obj.tracks.items[i].name + '</td>';
        html += '<td>' + obj.tracks.items[i].artists[0].name + '</td></tr>';
    }
    html += '</tbody>';
    document.getElementById("table").innerHTML = html;
}
