import pytube
# import sys

# url = sys.argv[1]
url = input("Enter The Audio URL:")

youtube = pytube.YouTube(url)
video = youtube.streams.filter(type="audio")
print("Downloading Audio")
try:
    video.first().download("C://Users//HP//Downloads")
except Exception:
    print()
    print("Try Again Later!!!!")
    print()