import csv
import matplotlib.pyplot as plt
file=open('train.csv')
reader = csv.reader(file)
# for r in reader:
#     print(r)

# ########################################################
# a = 0.2  # set alpha

# # Assuming that your CSV file has a header row, and the columns are in order x, y, z, and class_label
# with open('train.csv') as file:
#     reader = csv.reader(file)
#     header = next(reader)  # Skip the header row

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot

#     for da in reader:
#         x = float(da[10])
#         y = float(da[9])
#         z = float(da[8])
#         if x <= 2000:
#             if y<=2000:
#                 if z<=200:
#                     if da[11] == '1':
#                         ax.scatter(x, y, z, marker='x', color='r', alpha=a)
#                     else:
#                         ax.scatter(x, y, z, marker='o', color='b', alpha=a)

#     ax.set_xlabel(header[10])
#     ax.set_ylabel(header[9])
#     ax.set_zlabel(header[8])

#     plt.grid(True)
#     plt.show()
#     # plt.savefig("./figure/test.png")
#     plt.clf()
# ########################################################



## 2D plot for every two colums
#######################################################
a=0.2   #set alpha
for num in range(11):

    file=open('train.csv')
    reader = csv.reader(file)

    i=0

    for da in reader:
        if(i !=0):
            x=float(da[num])
            y=i
            if(da[11]=='1'):
                plt.plot(x,y,'x',color='r',alpha=a)
            else:
                plt.plot(x,y,'o',color='b',alpha=a)
        else:
            plt.xlabel(da[num])
            # plt.ylabel(da[num+1])
            plt.ylabel('i')
        i+=1

    plt.grid(True)
    plt.savefig("./figure/"+"old"+str(num+1)+'.png')
    plt.clf()
#######################################################




file.close()