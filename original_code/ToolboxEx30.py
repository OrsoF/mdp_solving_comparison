#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:06:59 2021

@author: Calic PEtar
"""

import time
import mdptoolbox
import numpy as np

P = np.array(( ((0,0.875,0.0625,0.0625),(0,0.75,0,0.25 ),(0,0,0.5,0.5),(0,0,0,1)) , ((0.875,0,0.125,0),(0,0.75,0.125,0.125 ),(0.8,0,0.2,0),(0,0,0,1))  , ((0,0,1,0),(1,0,0,0 ),(0,1,0,0),(0,0,0,1))  ))

R = np.array(((0, 4000, 6000), (1000,4000 ,6000),(3000,4000,6000),(3000,4000,6000)))
R = R*-1    #car c est un problème de minimisation.
#print(P)
#print(R)



vi = mdptoolbox.mdp.ValueIteration(P, R,1,0.0001,1000)


start_time = time.time()
vi.run()
print("--- %s seconds ---" % (time.time() - start_time))

print(vi.policy)
print(vi.V)
print(vi.iter)
