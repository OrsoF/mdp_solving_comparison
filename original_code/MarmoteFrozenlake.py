"""
 @brief frozen lake
 @author Calic Petar
 @date 30/06
 @version 1.1

"""

from pyMarmoteMDP import *
import time
import gym
import numpy as np

env= gym.make("FrozenLake-v0")

critere = "max"
epsilon = 0.0001
maxIter = 1000
peno = -10000000000


dimSS = 16
dimSA = 4
actionSpace =marmoteInterval(0,dimSA-1)
stateSpace = marmoteInterval(0,dimSS-1)

print("#")

#vector to store the dimension
trans=sparseMatrixVector(dimSA)

#les matrices d'action 16*16

#matrice pour l action 0
P0 = sparseMatrix(dimSS,dimSS)
for i in range(dimSS):   
    liste = env.P[i][0]  #env.P[0] etat 1, les actions qu on peu faire depuis et leurs détails
    for tup in liste:
        P0.addToEntry(i,tup[1],tup[0])
        
trans[0] = P0

#matrice d action 1
P1 = sparseMatrix(dimSS,dimSS)
for i in range(dimSS):   
    liste = env.P[i][1]  #env.P[0] etat 1, les actions qu on peu faire depuis et leurs détails
    for tup in liste:
        P1.addToEntry(i,tup[1],tup[0])

trans[1] = P1

#matrice action2
P2 = sparseMatrix(dimSS,dimSS)
for i in range(dimSS):   
    liste = env.P[i][2]  #env.P[0] etat 1, les actions qu on peu faire depuis et leurs détails
    for tup in liste:
        P2.addToEntry(i,tup[1],tup[0])
        
trans[2] = P2

#matrice action 3
P3 = sparseMatrix(dimSS,dimSS)
for i in range(dimSS):   
    liste = env.P[i][3]  #env.P[0] etat 1, les actions qu on peu faire depuis et leurs détails
    for tup in liste:
        P3.addToEntry(i,tup[1],tup[0])

trans[3] = P3



# matrice de reward 16*4
Reward = sparseMatrix(dimSS, dimSA)
for s in range(dimSS):
    for a in range(dimSA):
        liste = env.P[s][a]
        for tup in liste:
            #print(tup)
            Reward.addToEntry(s,a,tup[2])   #comment représenter les rew à cause des proba
        #print("end " , s , "*" , a)

env.render()

#pq on choisit le criitère total?
print("Debut de la construction MDP")
start_time = time.time()
mdp1 = totalRewardMDP(critere,stateSpace,actionSpace,trans,Reward)
print("-la modélisation prend - %s seconds ---" % (time.time() - start_time))


print("Fin de la construction MDP\n")

print("Affichage MDP")
mdp1.writeMDP()

print("Calcul iteration valeur")
#call the function to solve the MDP.       Ajout de time
start_time = time.time()
optimum = mdp1.valueIteration(epsilon, maxIter)
print(" Le calcul de la solution prend %s seconds ---" % (time.time() - start_time))



print("********************************")
print("Solution iteration valeur")

print("********************************")
pi = [0,3,3,3,0,0,0,0,3,1,0,0,0,2,1,0]

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
    if (obs==15):
        print("*****objectif atteint")
        gainFinal+=1
    else: 
        print("*****objectif NON atteint")
print("Pourcentage de reussite:",gainFinal/20*100, "%")    

