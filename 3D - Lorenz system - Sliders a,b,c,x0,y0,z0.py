import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.animation as anime
from matplotlib.widgets import Slider

def Lorenz(a,b,c,y10,y20,y30):

    #global y1,y2,y3
    
    y1 = [y10] ; y2 = [y20] ; y3 = [y30]
    
    def Y1(y1,y2): return a*(y2-y1)
    def Y2(y1,y2,y3): return (b-y3)*y1-y2
    def Y3(y1,y2,y3): return y1*y2-c*y3

    tau = .02 ; T = np.arange(0,50,tau)

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
        
    return y1,y2,y3

fig = plt.figure(figsize=(6, 6), facecolor='black')
plt.style.use('dark_background')
ax = p3.Axes3D(fig)
ax.set_xlim3d([-40, 40])
ax.set_ylim3d([-40, 40])
ax.set_zlim3d([0, 60])
ax.axis('off')
line, = ax.plot([],[],'c-',linewidth=.1)

a_slider_ax = fig.add_axes([0.13, .060, .7, .02])
a_slider_ax.tick_params(axis='y', colors='red')
a_slider = Slider(a_slider_ax, 'a', valmin = 0, valmax = 40, valinit = 10)
a_slider.label.set_size(10)

b_slider_ax = fig.add_axes([0.13, .030, .7, .02])
b_slider_ax.tick_params(axis='y', colors='green')
b_slider = Slider(b_slider_ax, 'b', valmin = 0, valmax = 40, valinit = 28)
b_slider.label.set_size(10)

c_slider_ax = fig.add_axes([0.13, .000, .7, .02])
c_slider_ax.tick_params(axis='y', colors='blue')
c_slider = Slider(c_slider_ax, 'c', valmin = 0, valmax = 40, valinit = 8/3)
c_slider.label.set_size(10)

x0_slider_ax = fig.add_axes([0.13, 1.060-.11, .7, .02])
x0_slider_ax.tick_params(axis='y', colors='red')
x0_slider = Slider(x0_slider_ax, r'$x_0$', valmin = -30, valmax = 30, valinit = 1)
x0_slider.label.set_size(10)

y0_slider_ax = fig.add_axes([0.13, 1.030-.11, .7, .02])
y0_slider_ax.tick_params(axis='y', colors='green')
y0_slider = Slider(y0_slider_ax, r'$y_0$', valmin = -30, valmax = 30, valinit = 1)
y0_slider.label.set_size(10)

z0_slider_ax = fig.add_axes([0.13, 1.000-.11, .7, .02])
z0_slider_ax.tick_params(axis='y', colors='blue')
z0_slider = Slider(z0_slider_ax, r'$z_0$', valmin = -30, valmax = 30, valinit = 1)
z0_slider.label.set_size(10)

yy1 = [[x0_slider.val]] ; yy2 = [[y0_slider.val]] ; yy3 = [[z0_slider.val]] 
def animate(j):
    
    global yy1,yy2,yy3
    
    a = a_slider.val ; b = b_slider.val ; c = c_slider.val
    
    ys = Lorenz(a,b,c,x0_slider.val,y0_slider.val,z0_slider.val)
    
    yy1.append(ys[0]) ; yy2.append(ys[1]) ; yy3.append(ys[2])
    
    yy1[j].append(yy1[j][-1])
    yy2[j].append(yy2[j][-1])
    yy3[j].append(yy3[j][-1])
    
    x = yy1[j]
    y = yy2[j]
    z = yy3[j]

    line.set_data([x, y])
    line.set_3d_properties(z)
    
    return line,

anim = anime.FuncAnimation(fig, animate, frames=None, interval=1)
plt.show()
