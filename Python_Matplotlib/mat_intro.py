import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,10,5,0,10]
# default plot
# plt.plot(x,y)
# plt.show()

# customize plot
plt.plot(x,y,marker='o',linestyle='--',color='red',label='My Custom Line')
plt.xlabel('X-Axis label')
plt.ylabel('Y-Axis label')
plt.title('Hafizur Rahman')
plt.legend()
plt.show()
