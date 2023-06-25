import React from 'react';
import './index.css';

const TrackList = ({ tracks }) => {
    return (
        <ul className="track-list">
            {tracks.tracks_names && tracks.tracks_names.map((track, index) => (
                <li className="track-item" key={index} >
                    <img className="album-cover" src={tracks.track_img_url[index]} alt="album cover" />
                    <div className="track-info">
                        <span className="track-name">{track}</span>
                    </div>
                </li>
            ))}
        </ul>
    );
};

export default TrackList;