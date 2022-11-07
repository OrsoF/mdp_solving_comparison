#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:06:59 2021

@author: calic petar
"""

import time
import mdptoolbox
import numpy as np
#P, R = mdptoolbox.example.forest()
P = np.array(( ((1,0,0,0),(0.75,0.25,0,0 ),(0.25,0.5,0.25,0),(0,0.25,0.5,0.25)) , ((0.75,0.25,0,0),(0.25,0.5,0.25,0 ),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25))  , ((0.25,0.5,0.25,0),(0,0.25,0.5,0.25 ),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25)) , ((0,0.25,0.5,0.25),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25))   ))


R = np.array(((0, -1, -2, -5), (5,0 ,-3,-1000),(6,-1,-1000,-1000),(5,-1000,-1000,-1000)))
print(P)
#print(R)



vi = mdptoolbox.mdp.FiniteHorizon(P, R, 1, 4)
start_time = time.time()
vi.run()
print("--- %s seconds ---" % (time.time() - start_time))

#print(vi.policy)
print(vi.V)
