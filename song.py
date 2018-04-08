class Song:

    def __init__(self, song_key, song_id, number_votes):
        self.song_key = song_key
        self.song_id = song_id
        self.number_votes = number_votes

    def __lt__(self, other):
        return self.number_votes > other.number_votes
