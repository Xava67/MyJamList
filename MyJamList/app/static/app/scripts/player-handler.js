document.addEventListener('DOMContentLoaded', function () {
    const audioPlayer = document.getElementById('audioPlayer');
    const songRows = document.querySelectorAll('#songList .tr');
    const playPauseButton = document.getElementById('playPauseButton');
    const nextButton = document.getElementById('nextButton');
    const prevButton = document.getElementById('prevButton');
    const songTitle = document.getElementById('songTitle');
    const songChords = document.getElementById('songChords');
    let currentSongIndex = -1;
    let isPlaying = false;

    function loadSong(index) {
        if (index < songRows.length && index >= 0) {
            const songRow = songRows[index];
            audioPlayer.src = songRow.getAttribute('data-src');
            audioPlayer.play();
            currentSongIndex = index;
            isPlaying = true;
            playPauseButton.textContent = '[ || ]';
            updateActiveSong();
            updateSongTitle();
            updateIndividualButtons();
        }
    }

    function updateActiveSong() {
        songRows.forEach((row, index) => {
            row.classList.toggle('active', index === currentSongIndex);
        });
    }

    function updateSongTitle() {
        const songRow = songRows[currentSongIndex];
        const title = songRow.querySelector('.td:nth-child(2)').textContent;
        const chordsLink = songRow.querySelector('.chords-link').href;
        songTitle.textContent = title;
        songChords.href = chordsLink;
        songChords.textContent = 'Chords';
    }

    function togglePlayPause() {
        if (isPlaying) {
            audioPlayer.pause();
            playPauseButton.textContent = '[ > ]';
        } else {
            if (audioPlayer.src === '') {
                loadSong(0);
            } else {
                audioPlayer.play();
            }
            playPauseButton.textContent = '[ || ]';
        }
        isPlaying = !isPlaying;
        updateIndividualButtons();
    }

    function updateIndividualButtons() {
        songRows.forEach((row, index) => {
            const playPauseButtonIndiv = row.querySelector('#playPauseButtonIndiv');
            if (index === currentSongIndex) {
                playPauseButtonIndiv.textContent = isPlaying ? '[ || ]' : '[ > ]';
            } else {
                playPauseButtonIndiv.textContent = '[ > ]';
            }
        });
    }

    function playNext() {
        currentSongIndex = (currentSongIndex + 1) % songRows.length;
        loadSong(currentSongIndex);
        updateIndividualButtons();
    }

    function playPrevious() {
        currentSongIndex = (currentSongIndex - 1 + songRows.length) % songRows.length;
        loadSong(currentSongIndex);
        updateIndividualButtons();
    }

    audioPlayer.addEventListener('ended', playNext);
    playPauseButton.addEventListener('click', togglePlayPause);
    nextButton.addEventListener('click', playNext);
    prevButton.addEventListener('click', playPrevious);

    //songRows.forEach((row, index) => {
    //    const playPauseButtonIndiv = row.querySelector('#playPauseButtonIndiv');
    //    playPauseButtonIndiv.addEventListener('click', function () {
    //        if (currentSongIndex === index && isPlaying) {
    //            audioPlayer.pause();
    //            isPlaying = false;
    //            playPauseButton.textContent = '[ > ]';
    //            playPauseButtonIndiv.textContent = '[ > ]';
    //        }
    //        else {
    //            loadSong(index);
    //            isPlaying = true;
    //            playPauseButton.textContent = '[ || ]';
    //            playPauseButtonIndiv.textContent = '[ || ]';
    //        }
    //    });
    //});

    songRows.forEach((row, index) => {
        const playPauseButtonIndiv = row.querySelector('#playPauseButtonIndiv');
        const currentSongTitle = row.querySelector('#title').textContent;
        playPauseButtonIndiv.addEventListener('click', function () {
            if (currentSongIndex !== index) {
                loadSong(index);
            } else {
                if (isPlaying) {
                    audioPlayer.pause();
                } else {
                    audioPlayer.play();
                }
                isPlaying = !isPlaying;
                playPauseButton.textContent = isPlaying ? '[ || ]' : '[ > ]';
                playPauseButtonIndiv.textContent = isPlaying ? '[ || ]' : '[ > ]';
            }
        });
    });
});
