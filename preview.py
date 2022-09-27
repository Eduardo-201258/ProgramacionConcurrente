import threading
import time
import concurrent.futures
import requests

def service():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(service_url())
        
def service_url():
    urls = ['https://www.google.com', 'https://www.10ejemplos.com','https://www.yahoo.com','https://www.yahoo.com.mx','https://10ejemplos.com/category/gramática','https://www.ejemplode.com/12-clases_de_espanol/48-ejemplo_de_triptongo.html','https://www.facebook.com','https://www.youtube.com','https://www.wikipedia.org','https://en.wikipedia.org',
            'http://www.direccion.org/ejemplo/item.html','https://pinguinodigital.com/blog/ejemplos-sobre-que-es-una-url/',
            'https://disenowebakus.net/imagenes/logo-akus.jpg','https://cnnespanol.cnn.com/','https://www.tocacuatro.com/','https://blog.virtualianet.com/buscar-imagenes-libres-derecho-autor-google/','https://themeisle.com/blog/what-is-a-website-url/','https://www.goya.com/es/recipes/caraotas-negras',
            'https://www.amazon.com/','https://okdiario.com/salud/tecnicas-medir-pulso-4673064','https://www.youtube.com/watch?v=CM4CkVFmTds']
    for x in urls:
        
        stat = requests.head(x)
        if stat.status_code == 200:
            print(stat.status_code, 'SITIO DISPONIBLE')
        else:
            print(stat.status_code, 'sitio NO disponible')

if __name__ == "__main__":
    
    while True:
        init_time = time.time()
        th1 = threading.Thread(target=service)
        th1.start()
        th1.join()
        end_time = time.time()-init_time
        print("tiempo de ejecucion = ", end_time)
        time.sleep(240)


