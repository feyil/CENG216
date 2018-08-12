import numpy as np
import matplotlib.pyplot as plt
import math

def f(y1,y2):
    y1_t = y2
    y2_t = (-9.81)*math.sin(y1)
    return y1_t, y2_t

def euler(t0,t1,h):
    t = np.arange(t0, t1+h/2,h)
    y1 = np.empty_like(t)
    y2 = np.empty_like(t)
    y1[0] = math.pi/2
    y2[0] = 0
    for i, ti in enumerate(t[:-1]):
        y1_t, y2_t = f(y1[i],y2[i])
        y1[i+1] = y1[i] + h*y1_t
        y2[i+1] = y2[i] + h*y2_t
    return t,y1,y2

t,y1,y2 = euler(0,10,0.01)
plt.plot(t,y1,t,y2)
#plt.plot(y1,y2)
plt.show()
