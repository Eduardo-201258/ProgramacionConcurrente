import threading
from pytube import YouTube


mutex = threading.Lock()
def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        video=id
        self.id=video


    def run(self):
        mutex.acquire()
        descarga(self.id)
        mutex.release()

destino = ("C:/Users/corre/Documents/src")
Hilos = [Hilo('https://www.youtube.com/watch?v=eVTXPUF4Oz4'), Hilo('https://www.youtube.com/watch?v=kXYiU_JCYtU'), Hilo('https://www.youtube.com/watch?v=LYU-8IFcDPw'), Hilo('https://www.youtube.com/watch?v=ysSxxIqKNN0'), Hilo('https://www.youtube.com/watch?v=YLHpvjrFpe0'), Hilo('https://www.youtube.com/watch?v=3GQvsthnjeE'), Hilo('https://www.youtube.com/watch?v=AnSM63vhtXI'), Hilo('https://www.youtube.com/watch?v=kSv6qlPtvR0')]
for h in Hilos:
    h.start()