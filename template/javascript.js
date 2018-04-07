var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var obj = JSON.parse(this.responseText);
        console.log(obj);
        var html = '<thead><tr><th scope="col">#</th><th scope="col">Song</th><th scope="col">Artist</th><th scope="col">Votes</th></tr></thead><tbody>';
        for (var i = 0; i < obj.tracks.items.length; i++) {
            html += '<tr><th scope="row">' + (i + 1) + '</th>';
            html += '<td>' + obj.tracks.items[i].name + '</td>';
            html += '<td>' + obj.tracks.items[i].artists[0].name + '</td>';
            html += '<td>' + (10 - i) + '</td></tr>';
        }
        html += '</tbody>';
        document.getElementById("table").innerHTML = html;
        //document.getElementById("table").append(html);
    }
};
xmlhttp.open("GET", "data.json", true);
xmlhttp.send();




