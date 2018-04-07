import queue
import song


class Playlist:

    def __init__(self):
        self.list = queue.PriorityQueue()
