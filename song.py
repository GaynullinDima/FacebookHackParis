class Song:

    def __init__(self, songJson, numberVotes):
        self.songJson = songJson
        self.numberVotes = numberVotes

    def __lt__(self, other):
        return self.numberVotes > other.numberVotes
