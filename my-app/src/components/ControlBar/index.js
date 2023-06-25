import React from 'react';
import './index.css';

const ControlBar = ({ onShuffle, onReverse }) => {
    return (
        <div className='control-bar'>
            <button onClick={onShuffle}>Shuffle</button>
            <button onClick={onReverse}>Reverse</button>
        </div>
    );
};

export default ControlBar;
