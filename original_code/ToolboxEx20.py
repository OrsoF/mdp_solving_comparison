#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:01:53 2021

@author: Calic Petar
"""
import time
import mdptoolbox
import numpy as np

P = np.array(( ((0,0,1),(0,0,0 ),(0,0,0)) , ((0,1,0),(0,0,0 ),(0,0,0)) , ((0,0,0),(1,0,0 ),(0,0,0)), ((0,0,0.3333),(0,0,0.3333 ),(0,0,0.3333))  ))
P1 = np.array(( ((0,0,1),(0,1,0 ),(0,0,1)) , ((0,1,0),(0,1,0 ),(0,0,1)) , ((1,0,0),(1,0,0 ),(0,0,1)), ((1,0,0),(0,1,0),(1/3,1/3,1/3))  ))

R = np.array(((2, 1, -1000, -1000), (-1000, -1000,2,-1000),(-1000,-1000,-1000,3)))
print(P1)
print(R)



#vi = mdptoolbox.mdp.ValueIteration(P1, R ,0.90,0.0001,1000)
start_time = time.time()
vi1 = mdptoolbox.mdp.RelativeValueIteration(P1, R,0.0001,1000)
print("---modele %s seconds ---" % (time.time() - start_time))
start_time = time.time()
vi1.run()
print("--- %s seconds ---" % (time.time() - start_time))

print(vi1.policy)
#print(vi1.V)
print(vi1.average_reward)
print(vi1.iter)