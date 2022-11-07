#Copyright 2019 Emmanuel Hyon, Alain Jean-Marie
"""
 @brief exemple 4
 @author Calic Petar
 @date mai 2021
 @version 1.1

"""
from pyMarmoteMDP import *
import time


#beta=0.5
critere = "max"
epsilon = 0.0001
maxIter = 1000
N = 4

dimSS = 4
dimSA = 4
actionSpace =marmoteInterval(0,dimSA-1)
stateSpace = marmoteInterval(0,dimSS-1)

print("#")

#vector to store the dimension
trans=sparseMatrixVector(dimSA)

P0 = sparseMatrix(dimSS,dimSS)
P0.addToEntry(0,0,1)
P0.addToEntry(1,0,0.75)
P0.addToEntry(1,1,0.25)
P0.addToEntry(2,0,0.25)
P0.addToEntry(2,1,0.5)
P0.addToEntry(2,2,0.25)
P0.addToEntry(3,1,0.25)
P0.addToEntry(3,2,0.5)
P0.addToEntry(3,3,0.25)
trans[0] = P0

P1= sparseMatrix(dimSS, dimSS);
P1.addToEntry(0,0,0.75)
P1.addToEntry(0,1,0.25)
P1.addToEntry(1,0,0.25)
P1.addToEntry(1,1,0.5)
P1.addToEntry(1,2,0.25)
P1.addToEntry(2,1,0.25)
P1.addToEntry(2,2,0.5)
P1.addToEntry(2,3,0.25)
P1.addToEntry(3,1,0.25)
P1.addToEntry(3,2,0.5)
P1.addToEntry(3,3,0.25)
trans[1] = P1

P2 = sparseMatrix(dimSS, dimSS);
P2.addToEntry(0,0,0.25)
P2.addToEntry(0,1,0.5)
P2.addToEntry(0,2,0.25)
P2.addToEntry(1,1,0.25)
P2.addToEntry(1,2,0.5)
P2.addToEntry(1,3,0.25)
P2.addToEntry(2,1,0.25)
P2.addToEntry(2,2,0.5)
P2.addToEntry(2,3,0.25)
P2.addToEntry(3,1,0.25)
P2.addToEntry(3,2,0.5)
P2.addToEntry(3,3,0.25)
trans[2] = P2

P3 = sparseMatrix(dimSS, dimSS);

P3.addToEntry(0,1,0.25)
P3.addToEntry(0,2,0.5)
P3.addToEntry(0,3,0.25)
P3.addToEntry(1,1,0.25)
P3.addToEntry(1,2,0.5)
P3.addToEntry(1,3,0.25)
P3.addToEntry(2,1,0.25)
P3.addToEntry(2,2,0.5)
P3.addToEntry(2,3,0.25)
P3.addToEntry(3,1,0.25)
P3.addToEntry(3,2,0.5)
P3.addToEntry(3,3,0.25)
trans[3] = P3


Reward  = sparseMatrix(dimSS, dimSA);
Reward.addToEntry(0,0,0)
Reward.addToEntry(0,1,-1)
Reward.addToEntry(0,2,-2)
Reward.addToEntry(0,3,-5)

Reward.addToEntry(1,0,5)
Reward.addToEntry(1,1,0)
Reward.addToEntry(1,2,-3)
Reward.addToEntry(1,3,-1000)

Reward.addToEntry(2,0,6)
Reward.addToEntry(2,1,-1)
Reward.addToEntry(2,2,-1000)
Reward.addToEntry(2,3,-1000)

Reward.addToEntry(3,0,5)
Reward.addToEntry(3,1,-1000)
Reward.addToEntry(3,2,-1000)
Reward.addToEntry(3,3,-1000)



print("Debut de la construction MDP")
mdp1 = finiteHorizonMDP(critere, stateSpace, actionSpace, trans, Reward,N)
print("Fin de la construction MDP\n")

print("Affichage MDP")
mdp1.writeMDP()

print("Calcul iteration valeur")
#call the function to solve the MDP.       Ajout de time
start_time = time.time()
optimum = mdp1.valueIteration(epsilon, maxIter)
print("--- %s seconds ---" % (time.time() - start_time))



print("********************************")
print("Solution iteration valeur")
optimum.writeSolution()

print("********************************")