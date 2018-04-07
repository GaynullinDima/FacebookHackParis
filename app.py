from flask import Flask, render_template
import playlist
import song
import json

app = Flask(__name__)

p = playlist.Playlist()
s1 = song.Song("1", 1)
s2 = song.Song("2", 2)
p.list.put(s1)
p.list.put(s2)


@app.route('/')
def index():
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
    return 'Your vote is received'


if __name__ == '__main__':
    app.run()
