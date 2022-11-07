#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:39:46 2021
jouet31
@author: Calic Petar

"""

import numpy as np
from gurobipy import *


P = np.array(( ((0,0.6,0.4,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0),(0,0,0,0,1,0,0,0,0),(0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,1)),((0,0,0,0.3,0.5,0.2,0,0,0),(0,1,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0),(0,0,0,0,1,0,0,0,0),(0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,1)),((0,0,0,0,0,0,0.15,0.85,0),(0,1,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0),(0,0,0,0,1,0,0,0,0),(0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,1)),((1,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0),(0,0,0,0,1,0,0,0,0),(0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,1,0,0),(1,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,1)),((1,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,0,0,1),(0,0,0,1,0,0,0,0,0),(0,0,0,0,1,0,0,0,0),(0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,1)),((1,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,1)),((1,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0),(0,0,0,0,1,0,0,0,0),(0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,1)),((1,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0),(0,0,0,0,1,0,0,0,0),(0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,1)) ))
pen = 10000000
R = np.array(( ((15, 10, 5, pen,pen,pen,pen,pen),(pen, pen, pen, 10,30,pen,pen,pen), (pen, pen, pen, pen,15,pen,pen,pen), (pen, pen, pen, pen,pen,10,pen,pen),  (pen, pen, pen, pen,pen,20,pen,pen),(pen, pen, pen, pen,pen,60,pen,pen),(pen, pen, pen, pen,pen,pen,5,pen), (pen, pen, pen, 5,pen,pen,pen,15),(pen, pen, pen, pen,0,pen,pen,0)) ))  

gamma = 0.9999
print("matrices de transitions:")
print(P)
print("matrices de rewards:")
print(R)

nbS = 9
nbA = 8
m = Model("MDPjouet30")     

# declaration variables de decision
v = []
for i in range(nbS):
    v.append(m.addVar(vtype=GRB.CONTINUOUS)) 

    
# maj du modele pour integrer les nouvelles variables
m.update()

obj = LinExpr();

for i in range(nbS):
    obj += v[i]/nbS   
# definition de l'objectif
m.setObjective(obj,GRB.MAXIMIZE)

# Definition des contraintes
for i in range(nbS):
    for j in range(nbA):
        sums = 0
        for k in range(nbS):
            sums = sums + gamma*P[j][i,k]*v[k]
        m.addConstr( v[i] <= R[i,j] + sums, "Contrainte%d" % i) #r(s,a)+ \sum_{s'} p(s'|s,a) h(s')

# Resolution
m.optimize()

print("")                
print('Solution optimale:')
for i in range(nbS):
        print('v%d'%(i+1), '=', v[i])
#print('Valeur de la fonction objectif (somme des V(S)) :', m.objVal)