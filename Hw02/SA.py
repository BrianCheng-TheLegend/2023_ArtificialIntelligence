### This code is for simulated annealing to find the best path with shortest distance
import math
import random

def SA(mat):







           #  0, 1, 2, 3, 4
distances =[[ 0, 1, 9,  8, 40], # 0
            [ 1, 0, 2, 35, 50], # 1
            [ 9, 2, 0, 30, 10], # 2
            [ 8, 35, 30, 0, 5], # 3
            [40, 50, 10, 5, 0]] # 4

# print(distances[0][0])

best_path,dest_dist = SA(distances)

print("最短路徑 : ",best_path)
print("最短距離 : ",dest_dist)