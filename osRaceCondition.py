import threading
import time

# Recurso compartido global (variable de interés)
contador = 0

def incrementar_contador(iteraciones):
    global contador
    for _ in range(iteraciones):
        # La "sección crítica" son estas tres operaciones:
        # 1. Leer el valor actual de 'contador'
        # 2. Incrementar el valor (cálculo)
        # 3. Escribir el nuevo valor en 'contador'
        temp = contador 
        temp = temp + 1
        contador = temp

if __name__ == '__main__':
    ITERACIONES = 10000000
    
    # Crea los dos hilos
    hilo1 = threading.Thread(target=incrementar_contador, args=(ITERACIONES,))
    hilo2 = threading.Thread(target=incrementar_contador, args=(ITERACIONES,))
    
    start_time = time.time()
    
    # Inicia la ejecución de los hilos
    hilo1.start()
    hilo2.start()
    
    # Espera a que ambos hilos terminen
    hilo1.join()
    hilo2.join()
    
    end_time = time.time()

    print("--- Resultado INSEGURO ---")
    print(f"Resultado esperado: {ITERACIONES * 2}")
    print(f"Resultado real:     {contador}")
    print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")

