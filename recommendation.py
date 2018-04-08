import spotipy
import spotipy.util as util

user_id = "213ixzxyxviymnguhdflx2dcq"
client_id = "b846e5e7858140e19e2e35934dfc0657"
client_secret = "a70588927f2e4c138593eb8770fdc427"
#Run only once to create a playlist    
#spotify.user_playlist_create("11157131956", "FBHackathon", public=True)

scope = 'playlist-modify-public'

tokenIS = util.prompt_for_user_token("Facebook Hackathon",scope,client_id=client_id,client_secret=client_secret,redirect_uri='http://localhost/')

spotify = spotipy.Spotify(auth=tokenIS)

#Run only once to create a playlist    
spotify.user_playlist_create(user_id, "FBHackathon", public=True)

def GetTracks(name):    
    results = spotify.search(q='track:' + name, type='track')
    return results

def ListTracks(results):
    FoundTracks = []
    for i in range(len(results["tracks"]["items"])):
        FoundTracks.append(results["tracks"]["items"][i]["uri"])
    return FoundTracks

#For now, I assume that the first track to appear is the one that fits the user's wishes. 

def AddTracksToPlayList(name):
    tracks = [ListTracks(GetTracks(name))[0]]
    
    spotify.user_playlist_add_tracks(user_id, "75UiREDEvjVXjHE7i1I6wH", ["spotify:track:" + track for track in tracks])

def add_track_to_playlist_by_id(id):
    spotify.user_playlist_add_tracks(user_id, "75UiREDEvjVXjHE7i1I6wH", "spotify:track:" + id)
