#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:39:46 2021
jouet31
@author: Calic Petar

"""

import numpy as np
from gurobipy import *
import time
import gym

env= gym.make("FrozenLake-v0")

dimSS = 16
dimSA = 4

Pi = np.zeros((dimSS,dimSS))
#Pi.tolist()

# 4 matrices d'action 16*16
P = np.array([Pi,Pi,Pi,Pi])
for a in range(dimSA):
    for i in range(dimSS):   
        liste = env.P[i][a]  #env.P[0] etat 1, les actions qu on peu faire depuis et leurs détails
        for tup in liste:
            P[a][i,tup[1]] = P[a][i,tup[1]] + tup[0]
            #P0.addToEntry(i,tup[1],tup[0])    

# matrice de reward 16*4
R = np.zeros((dimSS,dimSA))
for s in range(dimSS):
    for a in range(dimSA):
        liste = env.P[s][a]
        for tup in liste:
           # print(tup)
            R[s,a] = R[s,a] + tup[2]    #ADDTOENTRY DANS MARMOTE FAIT UNE SOMME
       # print('-')    
            


gamma = 0.9999
print("matrices de transitions:")
print(P)
print("matrices de rewards:")
print(R)

nbS = 16
nbA = 4
m = Model("frozenlake")     

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
m.setObjective(obj,GRB.MINIMIZE)  #pq c est un prb de min?

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