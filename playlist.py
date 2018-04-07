import queue
import song


class Playlist:

    def __init__(self):
        self.list = queue.PriorityQueue()


if __name__ == '__main__':
    p = Playlist()
    s1 = song.Song("1", 1);
    s2 = song.Song("2", 2);
    p.list.put(s1);
    p.list.put(s2);
    for s in p.list.queue:
        print(s)

    while not p.list.empty():
        s = p.list.get()
        print(s.songJson)
