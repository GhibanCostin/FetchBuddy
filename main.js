var theDiv = document.getElementById("username");
var usertag = document.createTextNode("Hello, Guest");
theDiv.appendChild(usertag);

var user_id = 3;
var match_nr = -1;
var match = "";
var contents = "";
let map_array = [];

function change_theme() {
    var link = document.getElementsByClassName("link")[0];
    if (link.getAttribute("id") == "off_link") {
        link.href = 'secondary.css';
        link.id = "on_link";
        document.getElementsByTagName("span")[0].innerHTML = "on";
    } else {
        link.href = 'main.css';
        link.id = "off_link";
        document.getElementsByTagName("span")[0].innerHTML = "off";
    }
};

class UserFetch {
    constructor(maps, userId) {
        this.pool = [];
        this.chances = [];
        this.totalChances = 0;
        for (let i = 0; i < maps.length; ++i) {
            let cluster = maps[i];
            for (let j = 0; j < cluster.length; ++j) {
                if (i === 0) {
                    this.chances[j] = cluster[j] === cluster[userId] ? 2 : 1;
                    this.totalChances += cluster[j] === cluster[userId] ? 2 : 1;
                } else {
                    if (cluster[j] === cluster[userId]) {
                        this.chances[j]++;
                        this.totalChances++;
                    }
                }
            }
        }
        this.totalChances -= this.chances[userId];
        this.chances[userId] = 0;
    }

    getRandomArbitrary(min, max) {
        return Math.random() * (max - min) + min;
    }

    getMatch() {
        for (let i = 0; i < this.chances.length; i++) {
            let n = Math.floor(this.chances[i] / this.totalChances * 100);
            for (let j = 0; j < n; j++) {
                this.pool.push(i);
            }
        }

        let idx = Math.floor(this.getRandomArbitrary(0, this.pool.length));
        return this.pool[idx];
    }

}

function parseCSV(contents) {
    var results = Papa.parse(contents);
    for (var i = 1; i < results.data.length; ++i) {
        console.log(results.data[i][1]);
        if (results.data[i][0] == user_id) {
            username = results.data[i][1];
            theDiv.removeChild(usertag);
            usertag = document.createTextNode("Hello, " + username);
            theDiv.appendChild(usertag);
        }

        if (results.data[i][0] == match_nr) {
            match = "Your buddy is " + results.data[i][1] + " from the " +
                results.data[i][2] + " department, " + " who is working on project " +
                results.data[i][3] + " and likes " + results.data[i][4] + ". Have fun!";
        }
    }
}

function readSingleFile(e) {
    var file = e.target.files[0];
    if (!file) {
        return;
    }
    var reader = new FileReader();
    reader.onload = function(e) {
        contents = e.target.result;
        if (file.type == "application/json") {
            var parsed = JSON.parse(contents);
            map_array = [parsed[10], parsed[8], parsed[6], parsed[4], parsed[2]];
        } else if (file.type == "text/csv" || file.type == "application/vnd.ms-excel") {
            document.getElementById("file-input").style.display = "none";
            //parseCSV(contents);
        }
    };
    reader.readAsText(file);
}

document.getElementById('file-input')
    .addEventListener('change', readSingleFile, false);

function fetch() {
    let matcher = new UserFetch(map_array, user_id);
    match_nr = matcher.getMatch();
    parseCSV(contents);
    document.getElementById("buddy").innerHTML = match;
};