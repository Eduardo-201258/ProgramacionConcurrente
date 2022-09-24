from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)


def service_video(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        video=id
        self.id=video

    def run(self):
        semaforo.acquire()
        service_video(self.id)
        semaforo.release()


destino = r"C:/Users/corre/Documents/src"
threads_semaphore = [Hilo('https://www.youtube.com/watch?v=eVTXPUF4Oz4'), Hilo('https://www.youtube.com/watch?v=kXYiU_JCYtU'), Hilo('https://www.youtube.com/watch?v=mFv4KqFU3kM'), Hilo('https://www.youtube.com/watch?v=mFv4KqFU3kM'), Hilo('https://www.youtube.com/watch?v=LYU-8IFcDPw'), Hilo('https://www.youtube.com/watch?v=ysSxxIqKNN0'), Hilo('https://www.youtube.com/watch?v=YLHpvjrFpe0'), Hilo('https://www.youtube.com/watch?v=0xyxtzD54rM'), Hilo('https://www.youtube.com/watch?v=Soa3gO7tL-c')]
for x in threads_semaphore:
    x.start()