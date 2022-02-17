from math import sin, cos
from time import time
from multiprocessing import Pool

# y=3x * sin(2 / x) + cos(3 * x)
A = 1 # левый предел интегрирования
B = 7 # правый предел интегрирования
N = 1000000 # количество отрезков 
h = (B - A) / (N - 1) # шаг сетки
PROCESSES = 1 # количество процессов

def CalculateIntegral(i): # функция для подсчета одного отрезка

    if i == A or i == N:
        x = i
        return( (h / 2) * (3 * x * sin(2 / x) + cos(3 * x)) )

    else:
        x = A + (i - 1) * h
        return( h  * (3 * x * sin(2 / x) + cos(3 * x)) )

if __name__ == "__main__":
    
    start_time = time() 

    with Pool(PROCESSES) as p: # подключение пула процессов с количеством процессов, равным PROCESSES
        res = sum(p.map(CalculateIntegral, list(range(1, N)))) # суммирование результата каждого процесса в переменную res 

    end_time = time()
  
    print("Количество процессов: ", PROCESSES)
    print("Значение интеграла: ", res)
    print("Время: ", end_time - start_time)