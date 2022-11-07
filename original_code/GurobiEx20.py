#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:33:49 2021
Exemple jouet 20
@author: calic Petar
"""

import numpy as np
from gurobipy import *

P = np.array(( ((0,0,1),(0,1,0 ),(0,0,1)) , ((0,1,0),(0,1,0 ),(0,0,1)) , ((1,0,0),(1,0,0 ),(0,0,1)), ((1,0,0),(0,1,0),(0.3333,0.3333,0.3334))  ))
R = np.array(((2, 1, -1000, -1000), (-1000, -1000,2,-1000),(-1000,-1000,-1000,3)))

gamma = 1

print("matrices de transitions:")
print(P)
print("matrices de rewards:")
print(R)

'''
si n est la taille de l'espace d'état il y a n+1 variables de décision
le scalaire g et h(s) avec s les n etats.
g terme de la valeure moyenne
pour résoudre le systeme:
min g
sous contrainte
h(s) >= r(s,a) -g + \sum_{s'} p(s'|s,a) h(s') pour tout s et a
'''

nbS = 3
nbA = 4
m = Model("MDPjouet20")     


# declaration variables de decision
v = []
for i in range(nbS):
    v.append(m.addVar(vtype=GRB.CONTINUOUS)) 

g = []
g.append(m.addVar(vtype=GRB.CONTINUOUS))

# maj du modele pour integrer les nouvelles variables
m.update()

obj = LinExpr();

obj = g[0]


# definition de l'objectif
m.setObjective(obj,GRB.MINIMIZE)

# Definition des contraintes
for i in range(nbS):
    for j in range(nbA):
        sums = 0
        for k in range(nbS):
            sums = sums + gamma*P[j][i,k]*v[k]
        m.addConstr( v[i] >= R[i,j] -g[0] + sums, "Contrainte%d" % i) #r(s,a) -g + \sum_{s'} p(s'|s,a) h(s')


# Resolution
m.optimize()

print("")                
print('Solution optimale:')
for i in range(nbS):
        print('v%d'%(i+1), '=', v[i])
#print('Valeur de la fonction objectif (somme des V(S)) :', m.objVal)
