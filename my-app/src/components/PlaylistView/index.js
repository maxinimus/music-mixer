import React, { useState, useEffect } from 'react';
import TrackList from '../TrackList';
import { fetchTracks } from '../../services/api';
import './index.css';

const PlaylistView = ({ selectedPlaylist }) => {
    const [tracks, setTracks] = useState([]);
    const [playlist, setPlaylist] = useState([]);
    const [data, setData] = useState(null);
    const [playlistImageUrl, setPlaylistImageUrl] = useState(null);

    useEffect(() => {
        if (selectedPlaylist) {
            fetchTracks(selectedPlaylist)
                .then(response => {
                    const data = response.data;
                    if (data.status === 'success') {
                        setTracks(data.tracks);
                        setPlaylist(data.playlist)
                        setData(data);
                        setPlaylistImageUrl(data.playlist.playlist_img_url);
                    } else {
                        console.error(data.message);
                    }
                })
                .catch(error => {
                    console.error('Error fetching tracks:', error);
                });
        }
    }, [selectedPlaylist]);

    return (
        <div className="playlist-view">
            <div className="playlist-header" >
                {playlistImageUrl && (
                    <a href={`https://open.spotify.com/playlist/${playlist.playlist_id}`} target="_blank" rel="noopener noreferrer">
                        <img src={playlistImageUrl} alt="playlist" className="playlist-cover" />
                    </a>
                )}
                {data && (
                    <div className='information-holder'>
                <a href={`https://open.spotify.com/playlist/${playlist ? playlist.playlist_id : ''}`} target="_blank" rel="noopener noreferrer" className="playlist-title-link">
                    <h1 className='playlist-title'> 
                        {selectedPlaylist}
                    </h1>
                </a>
                        <div className='info-row'>
                            <span className='creator-name'>
                                {playlist ? playlist.creator_name : 'N/A'}
                            </span>
                            <span className='track-number'>
                                {tracks && tracks.tracks_names ? tracks.tracks_names.length : 0} tracks
                            </span>
                            <span className='playlist-length'>
                                {playlist ? playlist.playlist_length : 'N/A'}
                            </span>
                        </div>
                    </div>
                )}
            </div>

            <TrackList tracks={tracks} />
        </div>
    );
};

export default PlaylistView;
