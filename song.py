class Song:

    def __init__(self, song_json, number_votes):
        self.song_json = song_json
        self.number_votes = number_votes

    def __lt__(self, other):
        return self.number_votes > other.number_votes
