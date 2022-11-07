#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:37:18 2021
Jouet30
@author: cCalic Petar
"""

import numpy as np
from gurobipy import *

P = np.array(( ((0,0.875,0.0625,0.0625),(0,0.75,0,0.25 ),(0,0,0.5,0.5),(0,0,0,1)) , ((0.875,0,0.125,0),(0,0.75,0.125,0.125 ),(0.8,0,0.2,0),(0,0,0,1))  , ((0,0,1,0),(1,0,0,0 ),(0,1,0,0),(0,0,0,1))  ))
R = np.array(((0, 4000, 6000), (1000,4000 ,6000),(3000,4000,6000),(3000,4000,6000)))

gamma = 0.9999

print("matrices de transitions:")
print(P)
print("matrices de rewards:")
print(R)

nbS = 4
nbA = 3
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