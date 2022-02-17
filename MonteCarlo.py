from time import time
import random
from multiprocessing import Pool

R = 7 # радиус окружности
N = 10000000 # количество точек
RectangleSquare = 4 * R ** 2 # площадь квадрата через радиус вписанной окружности
pointsForThread = list() # кол-во точек на один процесс
PROCESSES = 4 # количество процессов

for i in range(PROCESSES): # разделяет общее количество точек на каждый поток
    pointsForThread.append(N / PROCESSES)

def isPointInCircle (x, y, R): # проверяет, находится ли точка внутри окружности
    return True if ((x**2 + y**2) < R**2) else False

def CircleSquare (RectangleSquare, pointsInCircle, N): #площадь окружности
    return RectangleSquare * (pointsInCircle / N)

def PointsInCircle(pointsInThread): #кол-во точек в окружности для одного потока
    pointsInCircleForProcess = 0
    for _ in range(int(pointsInThread)):
        if isPointInCircle(random.uniform(-R, R), random.uniform(-R, R), R):
            pointsInCircleForProcess += 1
    return pointsInCircleForProcess

if __name__ == '__main__':
    
    start_time = time()

    with Pool(PROCESSES) as p: # подключение пула процессов с количеством процессов, равным PROCESSES
        res = sum(p.map(PointsInCircle, pointsForThread))

    end_time = time()

    print("Количество процессов: ", PROCESSES)
    print ("Площадь круга с радиусом {R} равна {result}".format(R = R, result = CircleSquare(RectangleSquare, res, N)))
    print("Время: ", end_time - start_time)