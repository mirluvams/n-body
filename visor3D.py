#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

with open('nbody.dat') as f:
    lines = f.readlines()

data = []

for line in lines:
    if line[0] != '#':
        data.append(line)

n_particles = int(data[0])
M = float(data[1])
print(M)
data.pop(1)

N = len(data)
a = b = k = 0



fig = plt.figure()
while True:
    a = 1 + n_particles*k
    b = n_particles*(k+1)
    if b >= N:
        break
    #print(b,N)
    k = k + 1
    ax = fig.add_subplot(projection='3d')
    subset = np.arange(a,b+1,1)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.xlim([-M, M])
    plt.ylim([-M, M])
    ax.set_zlim([-M, M])
    
    for p in subset:
        ms,xs,ys,zs,vxs,vys,vzs = data[p].split()
        m = float(ms)
        x = float(xs)
        y = float(ys)
        z = float(zs)
        vx = float(vxs)
        vy = float(vys)
        vz = float(vzs)
        #print(x,y,z)
        ax.scatter(x, y, z)
    plt.savefig(f"video/squares-{k:03d}.png")
    plt.clf()
    print(k)
    

#print('N particles '+str(n_particles))







#plt.show()
