from moviepy.editor import *
from pytube import YouTube
import shutil, time

errors = 0

def download_files(url):
    global errors
    try:
        mp4 = YouTube(url).streams.get_highest_resolution().download()
        mp3 = mp4.split('.mp4', 1)[0] + '.mp3'
        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3)
        audio_clip.close()
        video_clip.close()

        os.remove(mp4)
    except Exception:
        print('Error')

def get_mp3():
    url = input('Enter a Youtube Link: ')
    start_time = time.time()

    download_files(url)
    print(f'Time elapsed: {time.time() - start_time} seconds')

get_mp3()
