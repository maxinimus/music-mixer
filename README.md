# Spotify Playlist Manager: Music Mixer

Spotify Playlist Manager, also known as Music Mixer, is an advanced web application that enhances your music experience by enabling sophisticated interactions with your Spotify playlists using the Spotify API. 

## Key Features:

1. **Browse** and **interact** with your Spotify playlists through an intuitive interface.

2. **View playlist details**, including the playlist image, name, number of tracks, duration, and creator name.

3. **Shuffle and transform playlists** with advanced functions not available in the Spotify app, such as reversing the track order or shuffling tracks into a new playlist.

4. **Directly open the playlist** on Spotify by clicking on the playlist name or image.

5. **Personalized interface** for an optimal playlist management experience.

6. **Authenticate** with your Spotify account to access your playlists.

## Getting Started:

### Prerequisites:

Before you get started, make sure you have the following installed:
- Python 3
- Flask
- React
- npm (Node package manager)

### Installation:

1. **Clone the Repository**

    First, you need to clone the Music Mixer repository to your local machine. Run the following command in your terminal:

    ```shell
    git clone https://github.com/maxinimus/music-mixer.git
    ```

2. **Install Python Packages**

    Navigate to the root directory of the project and install the necessary Python packages by running:

    ```shell
    pip install -r requirements.txt
    ```

3. **Install npm Packages**

   While still in the root directory of the project, execute the following commands to install the necessary npm packages:

    ```shell
    cd music-mixer
    npm install
    ```

4. **Set up Environment Variables**

   Create a `.env` file in the root directory of the project and add the following environment variables:

    ```
    CLIENT_ID=<your-spotify-client-id>
    CLIENT_SECRET=<your-spotify-client-secret>
    ```

   Replace `<your-spotify-client-id>` and `<your-spotify-client-secret>` with your Spotify app's client ID and client secret.

### Usage:

1. **Start the Flask Server**

   In the root directory of the project, start the Flask server by running:

   ```shell
   python3 app.py
   ```

2. **Start the React App**

   In a separate terminal, navigate to the `music-mixer/my-app` directory and start the React app with:

   ```shell
   npm start
   ```

3. **Access the Application**

   Open a browser and navigate to:

    ```
    http://localhost:3000
    ```
4. **Authenticate** with your Spotify account by clicking the "Authenticate" button.

5. **Retrieve Your Playlists** by clicking the "Update Playlists" button.

6. **Select and Manage Playlists** by clicking on any playlist name. Utilize the advanced shuffle functions or other playlist transformations as needed.

## Acknowledgements:

- This project utilizes the Spotify Web API.
