import requests
import time
import threading
import mysql.connector
from pytube import YouTube

def get_service():
    urlPoke = 'https://pokeapi.co/api/v2/pokemon?limit=10&offset=0'
    data = requests.get(urlPoke)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                pokemones = x['name']
                info_db(pokemones)

def info_db(pokemones):
 conexion = mysql.connector.connect(
        user='root',
        password='eduardo',
        host='localhost',
        database='pokemon',
        port='3306'
    )
 sentence = conexion.cursor()
 query = "INSERT INTO lista(pokemon) VALUES ('{0}')".format(pokemones)
 sentence.execute(query)
 conexion.commit()

def get_videoService():
    urls_video = ["https://www.youtube.com/watch?v=eVTXPUF4Oz4","https://www.youtube.com/watch?v=kXYiU_JCYtU","https://www.youtube.com/watch?v=qcR1KbbhRTs","https://www.youtube.com/watch?v=mFv4KqFU3kM","https://www.youtube.com/watch?v=ysSxxIqKNN0"]
    destino = ("C:/Users/corre/Documents/src")
    
    for urls in urls_video:
      yt = YouTube(urls)
      video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
      save_video(video,destino)
      
def save_video(video,destino):    
    video.download(destino)

def get_services():
    x = 0
    for x in range(0, 50):
      print(f'Data input = {x}')
      response = requests.get('https://randomuser.me/api/')
      time.sleep(0.3)
      if response.status_code == 200:
         results = response.json().get('results')
         name = results[0].get('name').get('first')
         print(name)

if __name__ == '__main__':
    th1 = threading.Thread(target=get_services)
    th2 = threading.Thread(target=get_videoService)
    th3 = threading.Thread(target=get_service)

    th1.start()
    th2.start()
    th3.start()
    
    th1.join()
    th2.join()
    th3.join()