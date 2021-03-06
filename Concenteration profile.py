# -*- coding: utf-8 -*-
"""Classic Diffusion & Cahn-Hilliard Equation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13NlutLrTU7PpSGt_dhOaanoE8z6IVSZR
"""

import numpy as np
import matplotlib.pyplot as plt
di = 1
dt = 1
i_ini = 0
t_ini = 0
i_fin = 100
t_fin = 1000
rows = int((t_fin-t_ini)/dt)
columns = int((i_fin-i_ini)/di)
c = np.zeros((rows, columns))
for i in range(rows):
    c[i][0] = 1
#print(c)
D = 1
plt.figure(1) #number of figure
for time in range(rows-1):
    for space in range(1, columns-1):
        #print(space, time)
        #print(c[time+1][space], c[time][space], D*dt/(di*di)*(c[time][space+1] - 2*c[time][space] + c[time][space-1]))
        c[time+1][space] = c[time][space] + D*t_fin/(i_fin*i_fin)*(c[time][space+1] - 2*c[time][space] + c[time][space-1])
    #plt.plot(x_ax.transpose(), c[time+1])
for time in range(0,rows,50):
  y_ax = []
  x_ax = []
  for space in range(columns):
    x_ax.append(space)
    y_ax.append(c[time][space])
  plt.plot(x_ax,y_ax)
#print(c)

import numpy as np
import matplotlib.pyplot as plt
di = 1
dt = 1
i_ini = 0
t_ini = 0
i_fin = 100
t_fin = 10000
rows = int((t_fin-t_ini)/dt)
columns = int((i_fin-i_ini)/di)
c = np.zeros((rows, columns))
for i in range(rows):
    c[i][0] = 1
#print(c)
D = 0.1
plt.figure(1) #number of figure
for time in range(rows-1):
    for space in range(1, columns-1):
        #print(space, time)
        #print(c[time+1][space], c[time][space], D*dt/(di*di)*(c[time][space+1] - 2*c[time][space] + c[time][space-1]))
        c[time+1][space] = c[time][space] + D*t_fin/(i_fin*i_fin)*(c[time][space+1] - 2*c[time][space] + c[time][space-1])
    #plt.plot(x_ax.transpose(), c[time+1])
for time in range(0,rows,50):
  y_ax = []
  x_ax = []
  for space in range(columns):
    x_ax.append(space)
    y_ax.append(c[time][space])
  plt.plot(x_ax,y_ax)

import numpy as np
import matplotlib.pyplot as plt
di = 1
dt = 1
i_ini = 0
t_ini = 0
i_fin = 100
t_fin = 500
rows = int((t_fin-t_ini)/dt)
columns = int((i_fin-i_ini)/di)
c = np.zeros((rows, columns))
for i in range(rows):
    c[i][0] = 1
#print(c)
D = 10
plt.figure(1) #number of figure
for time in range(rows-1):
    for space in range(1, columns-1):
        #print(space, time)
        #print(c[time+1][space], c[time][space], D*dt/(di*di)*(c[time][space+1] - 2*c[time][space] + c[time][space-1]))
        c[time+1][space] = c[time][space] + D*t_fin/(i_fin*i_fin)*(c[time][space+1] - 2*c[time][space] + c[time][space-1])
    #plt.plot(x_ax.transpose(), c[time+1])
for time in range(0,rows,20):
  y_ax = []
  x_ax = []
  for space in range(columns):
    x_ax.append(space)
    y_ax.append(c[time][space])
  plt.plot(x_ax,y_ax)

import numpy as np
import matplotlib.pyplot as plt
di = 1
dt = 1
i_ini = 0
t_ini = 0
i_fin = 100
t_fin = 1000
rows = int((t_fin-t_ini)/dt)
columns = int((i_fin-i_ini)/di)
c = np.zeros((rows, columns))
for i in range(rows):
    c[i][0] = 1
    
#print(c)
D = 1
plt.figure(1) #number of figure
for time in range(rows-1):
    for space in range(1, columns-1):
        #print(space, time)
        #print(c[time+1][space], c[time][space], D*dt/(di*di)*(c[time][space+1] - 2*c[time][space] + c[time][space-1]))
        c[time+1][space] = c[time][space] + D*t_fin/(i_fin*i_fin)*(c[time][space+1] - 2*c[time][space] + c[time][space-1])
    c[time][columns-1] = c[time][columns-1-di]
    #plt.plot(x_ax.transpose(), c[time+1])
for time in range(0,rows,50):
  y_ax = []
  x_ax = []
  for space in range(columns):
    x_ax.append(space)
    y_ax.append(c[time][space])
  plt.plot(x_ax,y_ax)
#print(c)

import numpy as np
import matplotlib.pyplot as plt
di = 1
dt = 1
i_ini = 0
t_ini = 0
i_fin = 100
t_fin = 10000
rows = int((t_fin-t_ini)/dt)
columns = int((i_fin-i_ini)/di)
c = np.zeros((rows, columns))
for i in range(rows):
    c[i][0] = 1
#print(c)
D = 0.1
plt.figure(1) #number of figure
for time in range(rows-1):
    for space in range(1, columns-1):
        #print(space, time)
        #print(c[time+1][space], c[time][space], D*dt/(di*di)*(c[time][space+1] - 2*c[time][space] + c[time][space-1]))
        c[time+1][space] = c[time][space] + D*t_fin/(i_fin*i_fin)*(c[time][space+1] - 2*c[time][space] + c[time][space-1])
    c[time][columns-1] = c[time][columns-1-di]
    #plt.plot(x_ax.transpose(), c[time+1])
for time in range(0,rows,50):
  y_ax = []
  x_ax = []
  for space in range(columns):
    x_ax.append(space)
    y_ax.append(c[time][space])
  plt.plot(x_ax,y_ax)

import numpy as np
import matplotlib.pyplot as plt
di = 1
dt = 1
i_ini = 0
t_ini = 0
i_fin = 100
t_fin = 500
rows = int((t_fin-t_ini)/dt)
columns = int((i_fin-i_ini)/di)
c = np.zeros((rows, columns))
for i in range(rows):
    c[i][0] = 1
#print(c)
D = 10
plt.figure(1) #number of figure
for time in range(rows-1):
    for space in range(1, columns-1):
        #print(space, time)
        #print(c[time+1][space], c[time][space], D*dt/(di*di)*(c[time][space+1] - 2*c[time][space] + c[time][space-1]))
        c[time+1][space] = c[time][space] + D*t_fin/(i_fin*i_fin)*(c[time][space+1] - 2*c[time][space] + c[time][space-1])
    c[time][columns-1] = c[time][columns-1-di]
    #plt.plot(x_ax.transpose(), c[time+1])
for time in range(0,rows,20):
  y_ax = []
  x_ax = []
  for space in range(columns):
    x_ax.append(space)
    y_ax.append(c[time][space])
  plt.plot(x_ax,y_ax)

