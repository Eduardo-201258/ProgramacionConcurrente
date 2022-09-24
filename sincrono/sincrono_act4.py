import time
from pytube import YouTube

def video():
    urls_video = ["https://www.youtube.com/watch?v=eVTXPUF4Oz4","https://www.youtube.com/watch?v=kXYiU_JCYtU","https://www.youtube.com/watch?v=qcR1KbbhRTs","https://www.youtube.com/watch?v=mFv4KqFU3kM","https://www.youtube.com/watch?v=ysSxxIqKNN0"]
    destino = ("C:/Users/corre/Documents/src")
    
    for urls in urls_video:
      yt = YouTube(urls)
      video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
      save_video(video,destino)
      
def save_video(video,destino):    
    video.download(destino)
         
if __name__ == "__main__":
    init_time = time.time()
    video()
    end_time = time.time()-init_time
    print(end_time)



