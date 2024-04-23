from pytube import YouTube, Playlist


def baixarVideo(url):
    video = YouTube(url)
    video.streams.get_highest_resolution().download()
