let currentSongIndex = 0;

const songs = [
    { title: 'Canción 1 - Artista 1', artist: 'artista1', src: 'musica/cancion1.mp3', cover: 'caratula1.jpg' },
    { title: 'Canción 2 - Artista 2', artist: 'artista2', src: 'musica/cancion2.mp3', cover: 'caratula2.jpg' },
];

function openPlayer(title, artist, src, cover) {
    document.getElementById('songTitle').innerText = title;
    document.getElementById('albumCover').src = cover;
    document.getElementById('audioSource').src = src;
    document.getElementById('audioPlayer').load();
    document.getElementById('playerModal').style.display = 'block';
}

function closePlayer() {
    document.getElementById('playerModal').style.display = 'none';
    document.getElementById('audioPlayer').pause();
}