import React from 'react';
import './index.css';
import { authenticate } from '../../services/api';

const PlaylistColumn = ({ playlists, handlePlaylistClick, handleUpdatePlaylists }) => {
    return (
        <div className="playlist-column">
            <div className='buttons'> 
                <button onClick={authenticate}> Authenticate </button>
                <button onClick={handleUpdatePlaylists}> Update </button> 
            </div> 
            {playlists && playlists.map(playlist => (
                <div className="playlist-item" key={playlist.name} onClick={() => handlePlaylistClick(playlist.name)}>
                    <img className="playlist-image" src={playlist.image_url} alt={''} />
                    <span className="playlist-name">{playlist.name}</span>
                </div>
            ))} 
        </div>
    );
};

export default PlaylistColumn;
