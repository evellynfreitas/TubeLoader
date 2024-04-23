from pytube import YouTube, Playlist


def baixarVideo(url, pasta):
    video = YouTube(url)
    video.streams.get_highest_resolution().download(pasta)


def baixarPlaylist(url_playlist, pasta):
    playlist = Playlist(url_playlist)

    for url in playlist:
        baixarVideo(url, pasta)
