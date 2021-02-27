import pytube
# import sys

# url = sys.argv[1]
url = input("Enter The Video URL:")

youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
print(f'Downloadning {video.title}')
try:
    video.first().download("C://Users//HP//Downloads")
except Exception:
    print()
    print("Try Again Later!!!!")
    print()