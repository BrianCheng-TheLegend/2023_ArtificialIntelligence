import csv
import matplotlib.pyplot as plt
file=open('train.csv')
reader = csv.reader(file)
# for r in reader:
#     print(r)

# # print(reader)
# i=0
# a=0.3
# for a in range(10):
#     i=0
#     for da in reader:
#         if(i !=0):
#             x=float(da[a])
#             y=i
#             if(da[11]=='1'):
#                 plt.plot(x,y,'x',color='r',alpha=a)
#             else:
#                 plt.plot(x,y,'o',color='b',alpha=a)
#         i+=1
#     plt.show()


# Specify the number of subplots (equal to the range of 'a')
num_subplots = 10

# Create a figure with multiple subplots
fig, axes = plt.subplots(nrows=num_subplots, ncols=1, figsize=(8, 6))

# Loop through each subplot
for a, ax in enumerate(axes):
    i = 0
    for da in reader:
        if i != 0:
            x = float(da[a])
            y = i
            if da[11] == '1':
                ax.plot(x, y, 'x', color='r', alpha=a / num_subplots)  # Adjust alpha based on the subplot index
            else:
                ax.plot(x, y, 'o', color='b', alpha=a / num_subplots)  # Adjust alpha based on the subplot index
        i += 1

    ax.set_title(f"Subplot {a+1}")  # Add subplot title if needed

# Adjust layout to prevent clipping of titles
plt.tight_layout()

# Show the figure
plt.show()

# for da in reader:
#     if(i !=0):
#         if(da[11]=='1'):
#             plt.plot(da[1],i,'x',color='r')
#         else:
#             plt.plot(da[1],i,'o',color='b')
#     i+=1
# plt.show()
file.close()