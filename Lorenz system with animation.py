import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np

a = 10 ; b = 28 ; c = 8/3 #From 'https://en.wikipedia.org/wiki/Lorenz_system'

y10 = 1 ; y20 = 1 ; y30 = 1
y1 = [y10] ; y2 = [y20] ; y3 = [y30]

def Y1(y1,y2): return a*(y2-y1)
def Y2(y1,y2,y3): return (b-y3)*y1-y2
def Y3(y1,y2,y3): return y1*y2-c*y3

tau = .02 ; T = np.arange(0,100,tau)
for t in T:
    y11 = Y1(y1[-1],y2[-1])
    y21 = Y2(y1[-1],y2[-1],y3[-1])
    y31 = Y3(y1[-1],y2[-1],y3[-1])
    
    y12 = Y1(y1[-1] + tau/2*y11 , y2[-1] + tau/2*y21)
    y22 = Y2(y1[-1] + tau/2*y11 , y2[-1] + tau/2*y21 , y3[-1] + tau/2*y31)
    y32 = Y3(y1[-1] + tau/2*y11 , y2[-1] + tau/2*y21 , y3[-1] + tau/2*y31)
    
    y13 = Y1(y1[-1] + tau/2*y12 , y2[-1] + tau/2*y22)
    y23 = Y2(y1[-1] + tau/2*y12 , y2[-1] + tau/2*y22 , y3[-1] + tau/2*y32)
    y33 = Y3(y1[-1] + tau/2*y12 , y2[-1] + tau/2*y22 , y3[-1] + tau/2*y32)
    
    y14 = Y1(y1[-1] + tau * y13 , y2[-1] + tau/2*y23)
    y24 = Y2(y1[-1] + tau/2*y13 , y2[-1] + tau/2*y23 , y3[-1] + tau/2*y33)
    y34 = Y3(y1[-1] + tau/2*y13 , y2[-1] + tau/2*y23 , y3[-1] + tau/2*y33)
    
    y1.append(y1[-1] + tau*(y11 + 2*y12 + 2*y13 + y14)/6)
    y2.append(y2[-1] + tau*(y21 + 2*y22 + 2*y23 + y24)/6)
    y3.append(y3[-1] + tau*(y31 + 2*y32 + 2*y33 + y34)/6)

data = [np.array([y1,y2,y3])]

fig = plt.figure(figsize=(12,6), facecolor='black')
plt.style.use('dark_background')

ax = fig.add_subplot(111,projection='3d')
ax.plot(y1,y2,y3, 'c-', linewidth=.3)
plt.title('Lorenz system')
#ax.set_aspect('equal')
#ax.set_xticklabels([])
#ax.set_yticklabels([])
#ax.set_zticklabels([])
ax.axis('off')
plt.show()

'''Animation'''
def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


fig = plt.figure()
ax = p3.Axes3D(fig)

lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

# Setting the axes properties
ax.set_xlim3d([min(y1), max(y1)])
ax.set_ylim3d([min(y2), max(y2)])
ax.set_zlim3d([min(y3), max(y3)])
ax.axis('off')

line_ani = animation.FuncAnimation(fig, update_lines, len(y1), fargs=(data, lines),
                                   interval=1, blit=False)

plt.show()



