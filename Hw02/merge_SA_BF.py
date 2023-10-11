## this code is for Brute force to find the best path with shortest distance
import math
import random

def BF(mat):
    num_of_cities =len(mat) # number of cities
    best_path=[]            # shortest path
    best_dist=1000             # shortest distance
    # create an array have all point without start (0) and end (0)
    array=[]           
    for i in range(1,len(mat)):
        array.append(i)

    # get all path possible from arrangment   
    all_path=arrangement(array) 

    # add start (0) and end (0) in the array
    for arr in all_path:
        arr.insert(0,0)
        arr.append(0)

    for now_path in all_path:
        now_distance=0
        for i in range(len(mat)):
            now_distance+=distances[now_path[i]][now_path[i+1]]
        if now_distance <best_dist:
            best_dist = now_distance
            best_path=now_path

    return best_path,best_dist

# arrangement function 
def arrangement(arr):
    if len(arr)==1:
        return [arr]
    result=[]
    for i in range(len(arr)):
        rest_arr=arr[:i]+arr[i+1:]
        rest_list=arrangement(rest_arr)
        lists = []
        for term in rest_list:
            lists.append(arr[i:i+1]+term)
        result +=lists
    return result
    
def SA(mat):

    Temp= 1000              # Initial temperature
    minT= 1                 # Temperatute stop
    itrl= 10000            
    eta = 0.95
    k=1

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


# test data
test_cities_num=10
distances = [[0 if i == j else random.randint(1, 100) for j in range(test_cities_num)] for i in range(test_cities_num)]

best_path1,best_dist1 = BF(distances)
best_path2,best_dist2 = SA(distances)


print("BF最短路徑 : ",best_path1)
print("BF最短距離 : ",best_dist1)

print("SA最短路徑 : ",best_path2)
print("SA最短距離 : ",best_dist2)