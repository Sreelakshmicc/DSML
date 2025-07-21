import matplotlib.pyplot as plt
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("2LINE PLOTTED GRAPH")

x=[1,2,6,18]
y=[3,10,12,20]
x1=[1,2,6,18]
y1=[4,6,11,22]

plt.plot(x,y,marker='o',linestyle=':',color='red',mec='green',mfc='green',label="LINE 1")
plt.plot(x1,y1,marker='o',linestyle='solid',color='black',mec='yellow',mfc='yellow',label="LINE 2")
plt.legend()
plt.show()
