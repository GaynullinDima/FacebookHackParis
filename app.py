from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import schedule
from flask import Flask, render_template, request
import playlist
import recommendation
import song
import json

executor = ThreadPoolExecutor(1)
app = Flask(__name__, static_url_path='/static')

interval = datetime.now().time().microsecond + 1
s1 = song.Song({"name": "Kiss", "duration_ms": 1}, 1)
s2 = song.Song({"name": "Duval", "duration_ms": 2}, 2)
s3 = song.Song({"name": "mars", "duration_ms": 3}, 3)
s4 = song.Song({"name": "mama", "duration_ms": 5}, 5)
p = playlist.Playlist()
p.list.put(s1)
p.list.put(s2)
p.list.put(s3)
p.list.put(s4)

def job():
    global interval
    print(interval)
    if datetime.now().time().microsecond >= interval:
        current_song = p.list.get()
        interval += current_song.song_json["duration_ms"]
        print(current_song.song_json["duration_ms"])
        print(current_song.song_json["name"])
        recommendation.AddTracksToPlayList(current_song.song_json["name"])


def task():
    schedule.every().second.do(job)
    while True:
        schedule.run_pending()

@app.route('/')
def index():
    executor.submit(task)
    return render_template('index.html', p=p)


# @app.route('/<qwe>/')
# def initial_list(qwe):
#     return ''


@app.route('/search')
def search():
    return render_template('search.html')


# @app.route('/<qwe>/search/<query>')
# def search(qwe, query):
#     # search request to Spotify API
#     return 'Search Results'


@app.route('/voted')
def voted():
    return render_template('voted.html')

if __name__ == '__main__':
    app.run()
