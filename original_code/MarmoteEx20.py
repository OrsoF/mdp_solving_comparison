#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 @brief exemple2
 @author Calic Petar
 @date Avril
 @version 1.1
 

"""
from pyMarmoteMDP import *
import time


#beta=0.5
critere = "max"
epsilon = 0.0001
maxIter = 1000

dimSS = 3
dimSA = 4
actionSpace =marmoteInterval(0,dimSA-1)
stateSpace = marmoteInterval(0,dimSS-1)

print("#")

#vector to store the dimension
trans=sparseMatrixVector(dimSA)

P0 = sparseMatrix(dimSS,dimSS)
P0.addToEntry(0,2,1)

P0.addToEntry(1,1,1)
P0.addToEntry(2,2,1)


trans[0] = P0

P1= sparseMatrix(dimSS, dimSS);
P1.addToEntry(0,1,1)

#P1.addToEntry(1,1,1)
#P1.addToEntry(2,2,1)

trans[1] = P1

P2 = sparseMatrix(dimSS, dimSS);
P2.addToEntry(1,0,1)

#P2.addToEntry(0,0,1)
#P2.addToEntry(2,2,1)

trans[2] = P2

P3 = sparseMatrix(dimSS, dimSS);

#P3.addToEntry(0,0,1)
#P3.addToEntry(1,1,1)

P3.addToEntry(2,0,0.3333)
P3.addToEntry(2,1,0.3333)
P3.addToEntry(2,2,0.3333)
trans[3] = P3


Reward  = sparseMatrix(dimSS, dimSA);
Reward.addToEntry(0,0,2)
Reward.addToEntry(0,1,1)
Reward.addToEntry(0,2,-1000)
Reward.addToEntry(0,3,-1000)

Reward.addToEntry(1,0,-1000)
Reward.addToEntry(1,1,-1000)
Reward.addToEntry(1,2,2)
Reward.addToEntry(1,3,-1000)

Reward.addToEntry(2,0,-1000)
Reward.addToEntry(2,1,-1000)
Reward.addToEntry(2,2,-1000)
Reward.addToEntry(2,3,3)


print("Debut de la construction MDP")
start_time = time.time()
mdp1 = averageMDP(critere, stateSpace, actionSpace, trans, Reward)
print("modele %s seconds ---" % (time.time() - start_time))
#mdp1 = discountedMDP(critere, stateSpace, actionSpace, trans, Reward,beta)
print("Fin de la construction MDP\n")

print("Affichage MDP")
mdp1.writeMDP()

print("Calcul iteration valeur")
#call the function to solve the MDP.       Ajout de time
start_time = time.time()
optimum = mdp1.valueIteration(epsilon, maxIter)
print("--- %s seconds ---" % (time.time() - start_time))

print("Calcul par iteration valeur modifiee")
start_time = time.time()
optimum2 = mdp1.policyIterationModified(epsilon, maxIter, 0.001,100)
print("--- %s seconds ---" % (time.time() - start_time))


  
#call the function to solve the MDP
#print("Calcul par iteration valeur Gauss Seidel")
#optimum3 = mdp1.valueIterationGS(epsilon, maxIter)


print("********************************")
print("Solution iteration valeur")
optimum.writeSolution()

print("Solution par iteration valeur modifiee") 
optimum2.writeSolution()

#print("Solution par iteration valeur Gauss Seidel")
#optimum3.writeSolution()

print("********************************")