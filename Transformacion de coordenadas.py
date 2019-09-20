# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:05:19 2019

@author: Carlos Figueroa, Angelica Grajales
"""

import numpy as np
import matplotlib.pyplot as plt
P_Aorg = np.array([[1433.29], [-347.76], [-20.0]])
print (P_Aorg)

def R_z(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0.],
                     [np.sin(theta),  np.cos(theta), 0.],
                     [0., 0., 1.]])
theta = np.pi / 2.
R_AO = R_z(theta)
print (R_AO)

plt.figure()

# Drawing of system {0}
# Origin
plt.plot(0., 0., 'o')
# Axes
plt.arrow(0., 0., 100., 0., color = 'r')
plt.arrow(0., 0., 0., 100., color = 'g')

# Drawing of system {A}
# Origin
plt.plot(P_Aorg[0,0], P_Aorg[1,0], 'o')
# Axes
plt.arrow(P_Aorg[0,0], P_Aorg[1,0], 100. * np.cos(theta), 100. * np.sin(theta), color = 'r')
plt.arrow(P_Aorg[0,0], P_Aorg[1,0], -100. * np.sin(theta), 100. * np.cos(theta), color = 'g')

# Texts
plt.text(0., 0., '$O$')
plt.text(P_Aorg[0,0], P_Aorg[1,0], '$A$')
plt.text(0., 100., '$\{ O \}$')
plt.text(P_Aorg[0,0], P_Aorg[1,0] + 100., '$\{ A \}$')

# Axes settings
plt.xlabel('$x$ (mm)')
plt.ylabel('$y$ (mm)')
plt.axis('equal')
plt.show()

P_tableA = np.array([[0., 0., 0.], [660., 0., 0.], [660., 530., 0.], [0., 530., 0.]])
print (P_tableA)

plt.figure()

# Table vertices
Npoints = P_tableA.shape[0]
tableVert = np.zeros([Npoints + 1,3])
tableVert[:-1,:] = P_tableA
tableVert[-1,:] = P_tableA[0,:]
plt.plot(tableVert[:,0], tableVert[:,1], 'o-', alpha = 0.7)

# Drawing of system {A}
# Origin
plt.plot(0., 0., 'o')
# Axes
plt.arrow(0., 0., 100., 0., color = 'r')
plt.arrow(0., 0., 0., 100., color = 'g')

# Texts
plt.text(0., 0., '$A$')
plt.text(0., 100., '$\{ A \}$')

# Axis settings
plt.xlabel('$x$ (mm)')
plt.ylabel('$y$ (mm)')
plt.axis('equal')
plt.show()

P_tableO = P_Aorg + np.dot(R_AO, P_tableA.T)
print (P_tableO.T)

plt.figure()

# Drawing of system {0}
# Origin
plt.plot(0., 0., 'o')
# Axes
plt.arrow(0., 0., 100., 0., color = 'r')
plt.arrow(0., 0., 0., 100., color = 'g')

# Drawing of system {A}
# Origin
plt.plot(P_Aorg[0,0], P_Aorg[1,0], 'o')
# Axes
plt.arrow(P_Aorg[0,0], P_Aorg[1,0], 100. * np.cos(theta), 100. * np.sin(theta), color = 'r')
plt.arrow(P_Aorg[0,0], P_Aorg[1,0], -100. * np.sin(theta), 100. * np.cos(theta), color = 'g')

# Table vertices
Npoints = P_tableO.shape[1]
tableVert = np.zeros([Npoints + 1, 3])
tableVert[:-1,:] = P_tableO.T
tableVert[-1,:] = P_tableO[:,0].T
plt.plot(tableVert[:,0], tableVert[:,1], 'o-', alpha = 0.7)

# Texts
plt.text(0., 0., '$O$')
plt.text(P_Aorg[0,0], P_Aorg[1,0], '$A$')
plt.text(0., 100., '$\{ O \}$')
plt.text(P_Aorg[0,0], P_Aorg[1,0] + 100., '$\{ A \}$')

# Axes settings
plt.xlabel('$x$ (mm)')
plt.ylabel('$y$ (mm)')
plt.axis('equal')
plt.show()

P_B = np.array([[80., 140., 0.], 
                [85., 120., 0.], 
                [100., 100., 0.], 
                [120., 90., 0.],
                [135., 85., 0.],
                [150., 80., 0.],
                [165., 85., 0.],
                [180., 90., 0.],
                [200., 100., 0.],
                [215., 120., 0.],
                [220., 140., 0.],
                [180., 260., 0.],
                [480., 260., 0.],
                [600., 240., 0.],
                [600., 300., 0.],
                [180., 300., 0.],
                [200., 400., 0.],
                [180., 420., 0.],
                [120., 420., 0.],
                [100., 400., 0.],
                [120., 300., 0.],
                [100., 300., 0.],
                [90., 290., 0.],
                [100., 280., 0.],
                [90., 270., 0.],
                [100., 260., 0.],
                [120., 260., 0.],
                [80., 140., 0.]])
P_O = P_Aorg + np.dot(R_AO, P_B.T)
print (P_O.T)

plt.figure()

# Drawing of system {0}
# Origin
plt.plot(0., 0., 'o')
# Axes
plt.arrow(0., 0., 100., 0., color = 'r')
plt.arrow(0., 0., 0., 100., color = 'g')

# Drawing of system {A}
# Origin
plt.plot(P_Aorg[0,0], P_Aorg[1,0], 'o')
# Axes
plt.arrow(P_Aorg[0,0], P_Aorg[1,0], 100. * np.cos(theta), 100. * np.sin(theta), color = 'r')
plt.arrow(P_Aorg[0,0], P_Aorg[1,0], -100. * np.sin(theta), 100. * np.cos(theta), color = 'g')

# Table vertices
Npoints = P_tableO.shape[1]
tableVert = np.zeros([Npoints + 1, 3])
tableVert[:-1,:] = P_tableO.T
tableVert[-1,:] = P_tableO[:,0].T
plt.plot(tableVert[:,0], tableVert[:,1], 'o-', alpha = 0.7)

# Points
plt.plot(P_O[0,:], P_O[1,:], '.-', alpha = 0.7)

# Texts
plt.text(0., 0., '$O$')
plt.text(P_Aorg[0,0], P_Aorg[1,0], '$A$')
plt.text(0., 100., '$\{ O \}$')
plt.text(P_Aorg[0,0], P_Aorg[1,0] + 100., '$\{ A \}$')

# Axes settings
plt.xlabel('$x$ (mm)')
plt.ylabel('$y$ (mm)')
plt.axis('equal')
plt.show()