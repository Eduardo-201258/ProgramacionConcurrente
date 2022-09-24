import time
import threading
import concurrent.futures
import requests
from unittest import result
from urllib import request, response
from pytube import YouTube
import mysql.connector

def get_services(x=0):
    print(f'Data input = {x}')
    time.sleep(0.5)
    response = request.get('https://randomuser.me/api/')
    if response.status_code ==200:
        results = response.json().get('results')
        name =  results[0].get('name').get('first')
        print(name)

##########
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

#########
def service():
    dir = ["C:/Users/corre/Documents"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_video, dir)


def download_video():
    urls_video = ['https://www.youtube.com/watch?v=eVTXPUF4Oz4','https://www.youtube.com/watch?v=kXYiU_JCYtU','https://www.youtube.com/watch?v=mFv4KqFU3kM','https://www.youtube.com/watch?v=QNxaaIOl-XQ']
    for link in urls_video: 
     yt = YouTube(link)
     video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
     
     dir = ["C:/Users/corre/Documents"]
     
     video.download(dir)
     print("Se ha descargado los videos")


if __name__ == "__main__":
    init_time = time.time()
    x=0
    th2 = threading.Thread(target= get_service, args=[x])
    th2.start()
    
    service()
    end_time = time.time()-init_time
    print(end_time)
