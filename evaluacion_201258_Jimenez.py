import argparse
import threading
import time
import random

estado = None
candados = []
PERSONAS = 0 
RAFAGA_COMER = 0
TOTAL_TIEMPO_COMER = 0   

ESTADO_ESPERANDO = "E"
ESTADO_COMIENDO = "C"

def tomarPalillo(no_persona):
    palillo_der = candados[(no_persona - 1) % PERSONAS]
    palillo_izq = candados[no_persona]
    
    palillo_izq.acquire()

    if palillo_der.acquire(blocking=False):
        return True
    else:
        palillo_izq.release()
        return False


def palilloDisponible(no_persona):
    candados[no_persona].release()
    candados[(no_persona - 1) % PERSONAS].release()


def iniciarSimulacion(no_persona):
    intentos_fallidos = 0
    tiempo_comiendo = 0

    while tiempo_comiendo < TOTAL_TIEMPO_COMER:
        if tomarPalillo(no_persona):
            intentos_fallidos = 0

            tiempo_comer = min(RAFAGA_COMER, TOTAL_TIEMPO_COMER - tiempo_comiendo)
            tiempo_comiendo += tiempo_comer
            print(f"PERSONA {no_persona} comiendo")
            time.sleep(tiempo_comiendo)
            palilloDisponible(no_persona)

            estado[no_persona] = ESTADO_ESPERANDO
            tiempo_esperando = random.uniform(0, 5)
            print(f"PERSONA {no_persona} Esperando palillos")
            time.sleep(tiempo_esperando)
        else:
            estado[no_persona] = ESTADO_ESPERANDO
            intentos_fallidos += 1

            tiempo_reintentar = random.uniform(0, 3)
            print(f"PERSONA {no_persona} Esperando palillos"
                f" Intento {intentos_fallidos}")
            time.sleep(tiempo_reintentar)
        
def obtenerArgumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numPersonas", type=int, default=8)
    parser.add_argument("-r", "--palillos", type=int, default=4)
    parser.add_argument("-t", "--tiempoComer", type=int, default=10)
    return parser.parse_args()


if __name__ == '__main__':
    args = obtenerArgumentos()

    PERSONAS = args.numPersonas
    RAFAGA_COMER = args.palillos
    TOTAL_TIEMPO_COMER = args.tiempoComer
    
    estado = PERSONAS * [ESTADO_ESPERANDO]

    for _ in range(PERSONAS):
        candados.append(threading.RLock())

    hilos = []
    for i in range(args.numPersonas):
        nuevo_hilo = threading.Thread(target=iniciarSimulacion, args=(i,))
        hilos.append(nuevo_hilo)
    
    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()