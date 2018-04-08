import threading

import schedule
import recommendation
import song
from datetime import datetime
from playlist import Playlist

interval = datetime.now().time().microsecond + 4
s1 = song.Song({"name": "Kiss", "duration_ms": 1}, 1)
s2 = song.Song({"name": "Duval", "duration_ms": 2}, 2)
s3 = song.Song({"name": "mars", "duration_ms": 3}, 3)
s4 = song.Song({"name": "mama", "duration_ms": 5}, 5)
p = Playlist()
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
        recommendation.AddTracksToPlayList(current_song.song_json["name"])


schedule.every().second.do(job)

while True:
    schedule.run_pending()