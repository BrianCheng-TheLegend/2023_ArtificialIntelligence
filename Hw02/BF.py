### this code is for Brute force to find the best path with shortest distance
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
    


           #  0, 1, 2, 3, 4
distances =[[ 0, 1, 9,  8, 40], # 0
            [ 1, 0, 2, 35, 50], # 1
            [ 9, 2, 0, 30, 10], # 2
            [ 8, 35, 30, 0, 5], # 3
            [40, 50, 10, 5, 0]] # 4


best_path,dest_dist = BF(distances)

print("最短路徑 : ",best_path)
print("最短距離 : ",dest_dist)
