from pytube import YouTube, Playlist


def baixarVideo(url):
    video = YouTube(url)
    video.streams.get_highest_resolution().download()


def baixarPlaylist(url_playlist):
    playlist = Playlist(url_playlist)

    for url in playlist:
        baixarVideo(url)
