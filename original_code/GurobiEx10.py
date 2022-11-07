#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:31:56 2021

@author:petar
"""
import numpy as np
#import pandas
from gurobipy import *

P = np.array((((0.6, 0.4), (0.5, 0.5)), ((0.2, 0.8), (0.7, 0.3))))
R = np.array(((4.5, 2), (-1.5, 3)))
gamma = 0.5
print("matrices de transitions:")
print(P)
print("matrices de rewards:")
print(R)

nbS = 2
nbA = 2
m = Model("MDPjouet10")     

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
m.setObjective(obj,GRB.MINIMIZE)

# Definition des contraintes
for i in range(nbS):
    for j in range(nbA):
        sums = 0
        for k in range(nbS):
            sums = sums + gamma*P[j][i,k]*v[k]
        m.addConstr( v[i] >= R[i,j] + sums, "Contrainte%d" % i) #r(s,a)+ \sum_{s'} p(s'|s,a) h(s')

# Resolution
m.optimize()

print("")                
print('Solution optimale:')
for i in range(nbS):
        print('v%d'%(i+1), '=', v[i])
#print('Valeur de la fonction objectif (somme des V(S)) :', m.objVal)