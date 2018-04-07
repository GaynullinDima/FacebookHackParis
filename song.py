def cmp(a, b):
    return (a > b) - (a < b)


class Song:

    def __init__(self, songJson, numberVotes):
        self.songJson = songJson
        self.numberVotes = numberVotes

    def __cmp__(self, other):
        return cmp(self.numberVotes, other.numberVotes)
