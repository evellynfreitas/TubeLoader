from pytube import YouTube

video = YouTube('https://www.youtube.com/watch?v=oKVYm8mIUdo')
print(video.title)
print(video.views)
print(video.thumbnail_url)

video.streams.get_highest_resolution().download()
