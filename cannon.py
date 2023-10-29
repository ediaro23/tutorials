
#define a simple environment
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from math import pi, cos, sin

g = 9.81
m = 1
c = 0.2


def cost(z0):
    return z0[2]**2 + z0[3]**2

import math

def canondynamics(t,z):
    dx = z[2]
    dy = z[3]
    v = math.sqrt((dx*dx + dy*dy)) 
    #First-order form (derivative of position states is velocity states)
    dz = np.zeros(z.shape)
    dz[:2] = z[2:];
    fx = -c*dx*v
    fy = -c*dx*v - m*g 
    dz[2] = fx
    dz[3] = fy
    return dz



def forwardynamics(z0):
    res = solve_ivp(canondynamics, [0,100], z0, dense_output=False)
    y = res["y"]
    trajx, trajy = y[0,:], y[1,:]    
    idx = -1
    for i, (dx,dy) in enumerate(zip(trajx,trajy)):
        if dy <0.:
        # if y < ground_surface(x):
            idx = i+1
            break
    # return trajx, trajy
    coefficients = np.polyfit(trajx[:idx], trajy[:idx], 20)
    poly_func = np.poly1d(coefficients)
    return poly_func, trajx[:idx], trajy[:idx]
        

def plot_trajectory(z0, target):
    poly_func, trajx, trajy = forwardynamics(z0)
    x = np.linspace(0, 100,1000) 
    x_up = [el for el in x if poly_func(el) > 0.]
    plt.plot(x_up, poly_func(x_up), label='trajectory for z0 =' + str(z0))  
    plt.plot(trajx, trajy, label='trajectory for z0 =' + str(z0))  
    plt.scatter(target[0],target[1])
    plt.plot([x[0],max(x_up[-1],target[0])],[0,0], label='y = f(x)')  #ground
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
    


target = [9.5, 0.]


th0 = 45*(pi/180); #shooting angle
v0 = 60
dx0 = v0*cos(th0);
dy0 = v0*sin(th0);

z0 = np.array([0,0,dx0,dy0])
plot_trajectory(z0, target)