from flask import Flask, request, jsonify
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import mixer as m

app = Flask(__name__, static_folder='my-app/build', static_url_path='')
CORS(app)

@app.route('/authenticate', methods=['POST'])
@cross_origin()
def authenticate():
    auth_status = m.authenticate()
    if auth_status:  # assume your authenticate function returns True on success
        return jsonify({'status': 'authenticated'})
    else:
        return jsonify({'status': 'not authenticated'})

@app.route('/playlists', methods=['GET'])
@cross_origin()
def fetch_playlists():
    sp = m.authenticate()
    playlists = m.get_all_playlists(sp)
    
    if playlists is not None:
        playlist_info = [{'name': playlist['name'], 'image_url': m.get_playlist_image(playlist['id'], sp)} for playlist in playlists['items']]
        return jsonify({'playlists': playlist_info})
    else:
        return jsonify({'playlists': []})

@app.route('/tracks', methods=['POST'])
@cross_origin()
def tracks():
    playlist_name = request.get_json().get('playlist_name')
    sp = m.authenticate()  # assume you need to authenticate before mixing

    playlist_id = m.get_playlist_id(sp, playlist_name)
    if None == playlist_id:
        return jsonify({'status': 'error', 'message': 'playlist not found'})
    
    print('0')
    track_ids = m.get_all_tracks_from_playlist(playlist_id, sp)
    print('1')
    tracks_names = m.get_track_names_from_ids(track_ids, sp)
    print('2')
    track_img_url = m.get_track_img_urls(track_ids, sp)
    print('3')
    playlist_img_url = m.get_playlist_image(playlist_id, sp)
    print('4')
    number_of_tracks = len(track_ids)
    print('5')
    playlist_length = m.get_playlist_length(playlist_id, sp)
    print('6')
    creator_name = m.get_playlist_creator_name(playlist_id, sp)
    print('7')

    return jsonify({
    'status': 'success', 
    'tracks': {
        'tracks_names': tracks_names, 
        'track_ids': track_ids,
        'number_of_tracks': number_of_tracks,
        'track_img_url': track_img_url,
    },
    'playlist': {
        'playlist_img_url': playlist_img_url,
        'playlist_length': playlist_length,
        'playlist_id': playlist_id,
        'creator_name': creator_name,
    },
    })

@app.route('/shuffle', methods=['POST'])
@cross_origin()
def shuffle():
    playlist_name = request.get_json().get('playlist_name')
    sp = m.authenticate()

    mixer = m.clear_mixer_playlist(sp)
    if mixer is None:
        mixer = m.create_mixer_playlist(sp)

    playlist_id = m.get_playlist_id(sp, playlist_name)
    if None == playlist_id:
        return jsonify({'status': 'error', 'message': 'playlist not found'})
    
    track_ids = m.get_all_tracks_from_playlist(playlist_id, sp)
    shuffled_track_ids = m.shuffle_tracks(track_ids)
    # add tracks to mixer playlist
    m.add_tracks_to_playlist(sp, mixer['id'], shuffled_track_ids)

    return jsonify({'status': 'success'}) 

@app.route('/reverse', methods=['POST'])
@cross_origin()
def reverse():
    playlist_name = request.get_json().get('playlist_name')
    sp = m.authenticate()

    mixer = m.clear_mixer_playlist(sp)
    if mixer is None:
        mixer = m.create_mixer_playlist(sp)

    playlist_id = m.get_playlist_id(sp, playlist_name)
    if None == playlist_id:
        return jsonify({'status': 'error', 'message': 'playlist not found'})
    
    track_ids = m.get_all_tracks_from_playlist(playlist_id, sp)
    reversed_track_ids = m.reverse_tracks(track_ids)
    # add tracks to mixer playlist
    m.add_tracks_to_playlist(sp, mixer['id'], reversed_track_ids)

    return jsonify({'status': 'success'}) 

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
