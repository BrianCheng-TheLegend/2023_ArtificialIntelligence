### This code is for Simulated annealing to find the best path with shortest distance
import math
import random

def SA(mat):

    Temp= 200              # Initial temperature
    minT= 1                # Temperatute stop
    itrl= 150              # set iterations 
    eta = 0.95             # set the temperature every time cool down
    k=1                    # set the initial k

    num_of_cities=len(mat) # number of cities
    best_path=[]           # shortest path

    # setup initial path with start (0) and end (0)
    array=[]           
    for i in range(1,len(mat)):
        array.append(i)
    array.insert(0,0)
    array.append(0)
    best_path=array

    # setup initial distance
    best_dist=distance(num_of_cities,best_path)

    # 
    while(k<itrl):
        # set change position
        change_1=random.randint(1,num_of_cities-1)
        change_2=random.randint(1,num_of_cities-1)
        # change array
        array[change_1],array[change_2]=array[change_2],array[change_1]
        # calculate distance
        now_dist=distance(num_of_cities,array) 

        # if the current distance is smaller than best distance 
        # than teh current path will become best path
        if now_dist<best_dist:
            best_dist=now_dist
            best_path=array
        else:
            pr=PR(now_dist,best_dist,Temp)
            R=random.random()
            if R<pr:
                best_dist=now_dist
                best_path=array  
            else:
                array[change_1],array[change_2]=array[change_2],array[change_1]
        Temp*=eta
        k+=1

    return best_path,best_dist

# function for calculate distance
def distance(size,array):
    dist=0
    for i in range(size):
        dist+=distances[array[i]][array[i+1]]
    return dist

def PR(now_dist,best_dist,Temp):
    return min(1,math.exp(-(now_dist-best_dist)/Temp))

           #  0, 1, 2, 3, 4
distances =[[ 0, 1, 9,  8, 40], # 0
            [ 1, 0, 2, 35, 50], # 1
            [ 9, 2, 0, 30, 10], # 2
            [ 8, 35, 30, 0, 5], # 3
            [40, 50, 10, 5, 0]] # 4


best_path,best_dist = SA(distances)

print("最短路徑 : ",best_path)
print("最短距離 : ",best_dist)
