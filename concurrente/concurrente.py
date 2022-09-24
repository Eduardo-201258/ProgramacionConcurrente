import time
from unittest import result
import mysql.connector
import requests

# Implementar requests
    # consumir un servicio que descarge por lo menos 5000 registros
    # utilizar un for
    # for x in data:
     # write_db(x.name)

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


if __name__ == "_main_":
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)