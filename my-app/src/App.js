import React, { useState } from 'react';
import { authenticate, fetchPlaylists } from './services/api';
import PlaylistColumn from './components/PlaylistColumn';
import PlaylistView from './components/PlaylistView';
import ControlBar from './components/ControlBar';
import './App.css';
import { shufflePlaylist, reversePlaylist } from './services/api';

const App = () => {
  const [playlists, setPlaylists] = useState(null);
  const [selectedPlaylist, setSelectedPlaylist] = useState(null);

  // useEffect((isAuthenticated) => {
  //   // Call authenticate on component mount
  //   if (isAuthenticated) {
  //     return;
  //   }
  //   authenticate()
  //     .then(response => {
  //       if (response.data.status === 'authenticated') {
  //         setIsAuthenticated(true);
  //         // Fetch playlists after successful authentication
  //         fetchPlaylists().then(response => {
  //           setPlaylists(response.data.playlists);
  //         });
  //       }
  //     })
  //     .catch(error => {
  //       console.error('Error during authentication:', error);
  //     });
  // }, []);

  const handleUpdatePlaylists = () => {      // Call authenticate on component mount
    authenticate()
      .then(response => {
        if (response.data.status === 'authenticated') {
          // Fetch playlists after successful authentication
          fetchPlaylists().then(response => {
            setPlaylists(response.data.playlists);
          });
        }
      }
    )}

  const handlePlaylistClick = playlistName => {
    setSelectedPlaylist(playlistName);
  };

  const handleShuffleButtonClick = () => {
    // If there is no selected playlist, do nothing
    // if (!selectedPlaylist) {
    //   return;
    // }
    // otherwise, call the backend to shuffle the selected playlist, and set the selected playlist to the shuffled playlist (mixer)
    shufflePlaylist(selectedPlaylist)
      .then(response => {
        const data = response.data;
        if (data.status === 'success') {
          // setSelectedPlaylist('mixer');
        } else {
          console.error('Error shuffling playlist');
        }
      }
    )
  }

  const handleReverseButtonClick = () => {
    // If there is no selected playlist, do nothing
    if (!selectedPlaylist) {
      return;
    }
    // otherwise, call the backend to reverse the playlist, and set the selected playlist to the reversed playlist
    reversePlaylist(selectedPlaylist)
      .then(response => {
        const data = response.data;
        if (data.status === 'success') {
          // setSelectedPlaylist('mixer');
        } else {
          console.error('Error reversing playlist');
        }
      }
    )
  } 



  return (
    <div className="App">
      {(
        <div className='main-content'> 
          <PlaylistColumn
            playlists={playlists}
            handlePlaylistClick={handlePlaylistClick}
            handleUpdatePlaylists={handleUpdatePlaylists}
          />
          <PlaylistView selectedPlaylist={selectedPlaylist} />
        </div>
      )}
      
      <ControlBar 
        onShuffle={handleShuffleButtonClick}
        onReverse={handleReverseButtonClick}
      />

    </div>
  );
};

export default App;
