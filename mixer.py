import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os 
import random
import time

# ------------------ load environment variables ------------------ #

load_dotenv()

# ------------------ environment variables ------------------ #

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# ------------------ functions that utilize spotify api ------------------ #

# authenticate the user
def authenticate():
    # set up authorization
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                    client_secret=client_secret,
                                                    redirect_uri='http://localhost:3000',
                                                    scope='playlist-modify-private,\
                                                    playlist-modify-public,\
                                                    playlist-read-private,\
                                                    playlist-read-collaborative,\
                                                   '))
    return sp

# get the current user
def get_current_user(sp):
    user = sp.current_user()
    user_id = user['id']
    return user_id

# delete all the mixers that exist
def delete_all_mixers(sp):
    playlists = sp.user_playlists(get_current_user(sp))
    user_id = get_current_user(sp)
    for playlist in playlists['items']: 
        if playlist['name'] == 'mixer':
            sp.user_playlist_unfollow(user_id, playlist['id'])

# clear the 'mixer' playlist
def clear_mixer_playlist(sp):
    user_id = get_current_user(sp)
    playlists = sp.user_playlists(user_id)

    for playlist in playlists['items']: 
        if playlist['name'] == 'mixer':
            tracks = get_all_tracks_from_playlist(playlist['id'], sp)
            sp.user_playlist_remove_all_occurrences_of_tracks(user_id, playlist['id'], tracks)
            return playlist
        
    return None

# get all tracks ids from a playlist
def get_all_tracks_from_playlist(playlist_id, sp):
    tracks = sp.playlist_tracks(playlist_id)
    track_ids = []
    for track in tracks['items']:
        track_ids.append(track['track']['id'])
    
    return track_ids

# get a list of track names from a list of track ids
def get_track_names_from_ids(track_ids, sp):
    print(track_ids)
    sp = authenticate()
    track_names = []
    for track_id in track_ids:
        track = sp.track(track_id)
        track_names.append(track['name'])

    return track_names

# get platylist image from a playlist id
def get_playlist_image(playlist_id, sp):
    playlist = sp.playlist(playlist_id)
    if len(playlist['images']) == 0:
        return None
    return playlist['images'][0]['url']

# get all playlists of the user
def get_all_playlists(sp):
    playlists = sp.user_playlists(get_current_user(sp))
    # delete the mixer playlist from the list of playlists
    # for playlist in playlists['items']:
    #     if playlist['name'] == 'mixer':
    #         playlists['items'].remove(playlist)
    #         break

    return playlists

# check if the user is authenticated
def is_authenticated(sp):
    try:
        sp.current_user()
        return True
    except:
        return False

# get the id of a playlist
def get_playlist_id(sp, playlist_name):
    playlists = get_all_playlists(sp)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            return playlist['id']
    return None

# add tracks to a playlist
def add_tracks_to_playlist(sp, playlist_id, track_ids):
    if len(track_ids) != 0: 
        sp.playlist_add_items(playlist_id, track_ids)

# create a mixer playlist
def create_mixer_playlist(sp):
    user_id = get_current_user(sp)
    mixer = sp.user_playlist_create(user=user_id,
                                    name='mixer',
                                    public=False)
    return mixer

# shuffle the tracks
def shuffle_tracks(tracks):
    random.shuffle(tracks)
    return tracks

# reverse the order of the tracks
def reverse_tracks(tracks):
    tracks.reverse()
    return tracks

# play the track of the given track id 
def play_track(sp, track_id):
    # get track uri from track id
    track = sp.track(track_id)
    track_uri = track['uri']

    sp.start_playback(uris=[track_uri])

# get all track img urls from a list of track ids
def get_track_img_urls(track_ids, sp):
    track_img_urls = []
    for track_id in track_ids:
        track = sp.track(track_id)
        track_img_urls.append(track['album']['images'][0]['url'])
    
    return track_img_urls

# get playlist image from a playlist id
def get_playlist_image(playlist_id, sp):
    playlist = sp.playlist(playlist_id)
    if len(playlist['images']) == 0:
        return None
    return playlist['images'][0]['url']

# get the number of tracks in a playlist
def get_num_tracks_in_playlist(playlist_id, sp):
    playlist = sp.playlist(playlist_id)
    return playlist['tracks']['total']

# get the length of a playlist in seconds
def get_playlist_length(playlist_id, sp):
    playlist = sp.playlist(playlist_id)
    tracks = playlist['tracks']['items']
    length = 0
    for track in tracks:
        length += track['track']['duration_ms']

    length = length / 1000
    # convert to minutes and seconds
    minutes = length // 60
    seconds = length % 60
    # round the seconds
    seconds = round(seconds)
    minutes = round(minutes)
    # convert to string
    length = str(minutes) + ' min ' + str(seconds) + ' sec'

    return length

# get the playlist creator's name
def get_playlist_creator_name(playlist_id, sp):
    playlist = sp.playlist(playlist_id)
    return playlist['owner']['display_name']