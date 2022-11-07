#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:01:53 2021

@author: Petar
"""
import time
import mdptoolbox.example
import numpy as np
#P, R = mdptoolbox.example.forest()
P = np.array((((0.6, 0.4), (0.5, 0.5)), ((0.2, 0.8), (0.7, 0.3))))
R = np.array(((4.5, 2), (-1.5, 3)))
gamma = 0.5
epsilon = 0.0001
it = 700

print(R)    #beta grand converge lentement
start_time = time.time()
vi = mdptoolbox.mdp.ValueIteration(P, R, gamma, epsilon, it)
print("--vi- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
pi = mdptoolbox.mdp.PolicyIteration(P, R, gamma, max_iter=it)
print("--pi- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
vigs = mdptoolbox.mdp.ValueIterationGS(P,R,gamma,epsilon,it)
print("--vigs- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
pl = mdptoolbox.mdp._LP(P, R, gamma)
print("--pl- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
vi.run()
print("--- %s seconds ---" % (time.time() - start_time))
print(vi.policy)
print(vi.V)
print("iteration",vi.iter)

start_time = time.time()
pi.run()
print("--- %s seconds ---" % (time.time() - start_time))
print(pi.policy)
print(pi.V)
print("iteration",pi.iter)

start_time = time.time()
vigs.run()
print("--- %s seconds ---" % (time.time() - start_time))
print(vigs.policy)
print(vigs.V)
print("iteration",vigs.iter)

start_time = time.time()
pl.run()
print("--- %s seconds ---" % (time.time() - start_time))
print(pl.policy)
print(pl.V)
print("iteration",pl.iter)

