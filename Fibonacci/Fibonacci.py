import multiprocessing as mp 
import time 
import math


def fib(n):   #Fibonacci

    if n < 0:    
        print("Error de introducción") 
    elif n == 1: 
        return 0
    elif n == 2: 
        return 1
    else:
        n_cores = mp.cpu_count()   #Numero de cores utilizados del ordenador
        size_array = math.ceil(n / n_cores) #Numero de expediente dividido entre el numero de cores
        MC = mp.RawArray('i', n) 
        cores = []

        for core in range(n_cores): 
            i_MC = min(core * size_array, n) 
            f_MC = min((core + 1) * size_array, n)
            cores.append(mp.Process(target = par_core, args = (n, MC, i_MC, f_MC))) #Se cogen los cores y se van añadiendo

        for core in cores:
            core.start() 
        
        for core in cores:
            core.join()
        
        return MC[n]

def par_core(n, MC, i_MC, f_MC):
    for i in range(i_MC, f_MC):
        MC[i] = fib(n - 1) + fib(n - 2) #Formula de Fibonacci

if __name__ == "__main__":  
    n = 21838989
    inicio = time.time() #Tiempo de inicio
    print(fib(n))
    fin = time.time() #Tiempo final
    print('Tiempo de ejecucion SECUENCIAL = ', fin-inicio) #Resta para evitar que si se ejecuta no quede el tiempo restante