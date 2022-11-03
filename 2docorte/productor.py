from threading import Thread
import threading 
import time, random
import queue

bodega = queue.Queue(maxsize=20)

class Productor(Thread):
    def __init__(self, array1):
        threading.Thread.__init__(self)
        self.array1 = array1

    def run(self):
        while True:
            if not bodega.full():
                array1 = random.randint(0, 20)
                bodega.put(array1)
                print("Se agrego un nuevo intem: " + str(array1))
                time.sleep(5)

class Consumidor(Thread):
    def __init__(self,array2):
        threading.Thread.__init__(self)
        self.array = array2
        

    def run(self):
        while True:
            if not bodega.empty():
                array2 = bodega.get()
                print('Se ha obtenido el intem: '+str(array2))
                time.sleep(5)

def main():
    array=[]
    hilo_produc = Productor(array)
    hilo_consum = Consumidor(array)

    hilo_produc.start()
    hilo_consum.start()
    if array.count > 10: 
        hilo_produc.wait()
        hilo_consum.signal()
    else:
        hilo_produc.signal()
        hilo_consum.wait()
    
    


main()