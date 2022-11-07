#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:06:59 2021

@author: Calic Petar
"""

import time
import mdptoolbox
import numpy as np
import gym

env= gym.make("FrozenLake8x8-v0")

dimSS = 64
dimSA = 4
#pen = 100000

env.render()

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
            
print("P0:",P[0])
print(R)



start_time = time.time()
vi = mdptoolbox.mdp.ValueIteration(P, R,1,0.0001,1000) #gamma =  doit etre signalé
print("temps de modélisation--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
vi.run()
print("temps de calcul %s seconds ---" % (time.time() - start_time))

print("Pi:",vi.policy)
print("V:",vi.V)
print("nombre d itérations:",vi.iter)

pi = vi.policy

print("Simulation de la politique")
gainFinal=0
for i in range(20):
    fin=False
    obj=False
    obs=env.reset()  
    while not fin:
        i=i+1
        obsE=obs
        action=int(pi[obs])
        obs,gain,fin,info= env.step(action)
        #env.render()
    if (obs==63):
        print("*****objectif atteint")
        gainFinal+=1
    else: 
        print("*****objectif NON atteint")
print("Pourcentage de reussite:",gainFinal/20*100, "%")    

