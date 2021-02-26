import pytube

url = input('Enter Link OF The Video:')

youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
print(video.title)
video.download("C://Users//HP//Downloads")