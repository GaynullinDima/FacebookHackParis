import spotipy
import spotipy.util as util


#Run only once to create a playlist    
#spotify.user_playlist_create("11157131956", "FBHackathon", public=True)

scope = 'playlist-modify-public'

tokenIS = util.prompt_for_user_token("Facebook Hackathon",scope,client_id=clientId,client_secret=clientSecret,redirect_uri='http://localhost/')

spotify = spotipy.Spotify(auth=tokenIS)

#Run only once to create a playlist    
#spotify.user_playlist_create(userId, "FBHackathon", public=True)

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
    
    spotify.user_playlist_add_tracks(userId, "6ETLDvLQH17UUAL4a8Sf0C", ["spotify:track:" + track for track in tracks])


