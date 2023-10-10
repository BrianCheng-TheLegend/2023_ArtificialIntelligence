import numpy as np

def BF(mat):
    num_of_cities =len(mat)
    


    return best_path,dest_dist


distances = np.array(
#  0, 1, 2, 3, 4
[[ 0, 1, 9, 8, 40], # 0
[ 1, 0, 2, 35, 50], # 1
[ 9, 2, 0, 30, 10], # 2
[ 8, 35, 30, 0, 5], # 3
[40, 50, 10, 5, 0]  # 4
])



best_path,dest_dist = BF(distances)

print("最短路徑 : ",best_path)
print("最短距離 : ",dest_dist)
