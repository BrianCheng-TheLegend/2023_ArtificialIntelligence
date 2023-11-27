import csv
import matplotlib.pyplot as plt
file=open('train.csv')
reader = csv.reader(file)
for r in reader:
    print(r)
# print(type(reader))

## 2D plot
a=0.2   #set alpha
for num in range(11):
    file=open('train.csv')
    reader = csv.reader(file)
    i=0
    for da in reader:
        if(i !=0):
            x=float(da[num])
            y=float(da[num+1])
            if(da[11]=='1'):
                plt.plot(x,y,'x',color='r',alpha=a)
            else:
                plt.plot(x,y,'o',color='b',alpha=a)
        i+=1
    plt.grid(True)
    plt.savefig("./figure/"+str(num+1)+'.png')
    plt.clf()
    # plt.show()




file.close()