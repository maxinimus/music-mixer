// my-app/src/services/api.js

import axios from 'axios';

export const authenticate = () => {
    return axios.post(`/authenticate`);
};

export const fetchPlaylists = () => {
    return axios.get(`/playlists`);
};

export const fetchTracks = (playlistName) => {
    return axios.post(`/tracks`, { playlist_name: playlistName });
};

export const shufflePlaylist = (playlistName) => {
    return axios.post(`/shuffle`, { playlist_name: playlistName });
}

export const reversePlaylist = (playlistName) => {
    return axios.post(`/reverse`, { playlist_name: playlistName });
}
