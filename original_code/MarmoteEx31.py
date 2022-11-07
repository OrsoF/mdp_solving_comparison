"""
 @brief exemple 31
 @author Calic Petar
 @date 05/21
 @version 1.1

"""
from pyMarmoteMDP import *
import time

critere = "min"
epsilon = 0.0001
maxIter = 1000
peno = +10000000000;

dimSS = 9
dimSA = 8
actionSpace =marmoteInterval(0,dimSA-1)
stateSpace = marmoteInterval(0,dimSS-1)

print("#")

#vector to store the dimension
trans=sparseMatrixVector(dimSA)

P0 = sparseMatrix(dimSS,dimSS)
P0.addToEntry(0,1,0.6);
P0.addToEntry(0,2,0.4);
P0.addToEntry(1,1,1);  
P0.addToEntry(2,2,1);
P0.addToEntry(3,3,1);
P0.addToEntry(4,4,1);
P0.addToEntry(5,5,1);
P0.addToEntry(6,6,1);
P0.addToEntry(7,7,1);
P0.addToEntry(8,8,1);
trans[0] = P0

P1 = sparseMatrix(dimSS,dimSS)
P1.addToEntry(0,3,0.3);
P1.addToEntry(0,4,0.5);
P1.addToEntry(0,5,0.2);
P1.addToEntry(1,1,1);  
P1.addToEntry(2,2,1);
P1.addToEntry(3,3,1);
P1.addToEntry(4,4,1);
P1.addToEntry(5,5,1);
P1.addToEntry(6,6,1);
P1.addToEntry(7,7,1);
P1.addToEntry(8,8,1);
trans[1] = P1

P2= sparseMatrix(dimSS, dimSS);
P2.addToEntry(0,6,0.15);
P2.addToEntry(0,7,0.85);
P2.addToEntry(1,1,1);  
P2.addToEntry(2,2,1);
P2.addToEntry(3,3,1);
P2.addToEntry(4,4,1);
P2.addToEntry(5,5,1);
P2.addToEntry(6,6,1);
P2.addToEntry(7,7,1);
P2.addToEntry(8,8,1);
trans[2] = P2

P3 = sparseMatrix(dimSS, dimSS);
P3.addToEntry(1,0,1);
P3.addToEntry(7,0,1);
P3.addToEntry(0,0,1);  
P3.addToEntry(2,2,1);
P3.addToEntry(3,3,1);
P3.addToEntry(4,4,1);
P3.addToEntry(5,5,1);
P3.addToEntry(6,6,1);
P3.addToEntry(8,8,1);
trans[3] = P3

P4 = sparseMatrix(dimSS, dimSS);
P4.addToEntry(1,8,1);
P4.addToEntry(2,8,1);
P4.addToEntry(0,0,1);  
P4.addToEntry(3,3,1);
P4.addToEntry(4,4,1);
P4.addToEntry(5,5,1);
P4.addToEntry(6,6,1);
P4.addToEntry(7,7,1);
P4.addToEntry(8,8,1);
trans[4] = P4


P5 = sparseMatrix(dimSS, dimSS);
P5.addToEntry(3,8,1);
P5.addToEntry(4,8,1);
P5.addToEntry(5,8,1);
P5.addToEntry(1,1,1);  
P5.addToEntry(0,0,1);
P5.addToEntry(2,2,1);
P5.addToEntry(6,6,1);
P5.addToEntry(7,7,1);
P5.addToEntry(8,8,1);
trans[5] = P5

P6 = sparseMatrix(dimSS, dimSS);
P6.addToEntry(6,8,1);
P6.addToEntry(8,8,1);   
P6.addToEntry(2,2,1);
P6.addToEntry(0,0,1);
P6.addToEntry(3,3,1);
P6.addToEntry(4,4,1);
P6.addToEntry(5,5,1);
P6.addToEntry(1,1,1);
P6.addToEntry(7,7,1);
trans[6] = P6

P7 = sparseMatrix(dimSS, dimSS);
P7.addToEntry(7,6,1);
P7.addToEntry(0,0,1);  #/* fill in the other transitions to have a stochastic matrix */    
P7.addToEntry(3,3,1);
P7.addToEntry(4,4,1);
P7.addToEntry(5,5,1);
P7.addToEntry(6,6,1);
P7.addToEntry(1,1,1);
P7.addToEntry(8,8,1);
P7.addToEntry(2,2,1);
trans[7] = P7


Reward  = sparseMatrix(dimSS, dimSA);
Reward.addToEntry(0,0,15);
Reward.addToEntry(0,1,10);
Reward.addToEntry(0,2,5);
Reward.addToEntry(0,3,peno);
Reward.addToEntry(0,4,peno);
Reward.addToEntry(0,5,peno);
Reward.addToEntry(0,6,peno);
Reward.addToEntry(0,7,peno);

Reward.addToEntry(1,0,peno);
Reward.addToEntry(1,1,peno);
Reward.addToEntry(1,2,peno);
Reward.addToEntry(1,3,10);
Reward.addToEntry(1,4,30);
Reward.addToEntry(1,5,peno);
Reward.addToEntry(1,6,peno);
Reward.addToEntry(1,7,peno);

Reward.addToEntry(2,0,peno);
Reward.addToEntry(2,1,peno);
Reward.addToEntry(2,2,peno);
Reward.addToEntry(2,3,peno);
Reward.addToEntry(2,4,15);
Reward.addToEntry(2,5,peno);
Reward.addToEntry(2,6,peno);
Reward.addToEntry(2,7,peno);

Reward.addToEntry(3,0,peno);
Reward.addToEntry(3,1,peno);
Reward.addToEntry(3,2,peno);
Reward.addToEntry(3,3,peno);
Reward.addToEntry(3,4,peno);
Reward.addToEntry(3,5,10);
Reward.addToEntry(3,6,peno);
Reward.addToEntry(3,7,peno);

Reward.addToEntry(4,0,peno);
Reward.addToEntry(4,1,peno);
Reward.addToEntry(4,2,peno);
Reward.addToEntry(4,3,peno);
Reward.addToEntry(4,4,peno);
Reward.addToEntry(4,5,20);
Reward.addToEntry(4,6,peno);
Reward.addToEntry(4,7,peno);

Reward.addToEntry(5,0,peno);
Reward.addToEntry(5,1,peno);
Reward.addToEntry(5,2,peno);
Reward.addToEntry(5,3,peno);
Reward.addToEntry(5,4,peno);
Reward.addToEntry(5,5,60);
Reward.addToEntry(5,6,peno);
Reward.addToEntry(5,7,peno);

Reward.addToEntry(6,0,peno);
Reward.addToEntry(6,1,peno);
Reward.addToEntry(6,2,peno);
Reward.addToEntry(6,3,peno);
Reward.addToEntry(6,4,peno);
Reward.addToEntry(6,5,peno);
Reward.addToEntry(6,6,5);
Reward.addToEntry(6,7,peno);

Reward.addToEntry(7,0,peno);
Reward.addToEntry(7,1,peno);
Reward.addToEntry(7,2,peno);
Reward.addToEntry(7,3,5);
Reward.addToEntry(7,4,peno);
Reward.addToEntry(7,5,peno);
Reward.addToEntry(7,6,peno);
Reward.addToEntry(7,7,15);

Reward.addToEntry(8,0,peno);
Reward.addToEntry(8,1,peno);
Reward.addToEntry(8,2,peno);
Reward.addToEntry(8,4,peno);
Reward.addToEntry(8,5,peno);
Reward.addToEntry(8,6,0);
Reward.addToEntry(8,7,peno);




print("Debut de la construction MDP")
start_time = time.time()
mdp1 = totalRewardMDP(critere,stateSpace,actionSpace,trans,Reward)
print("--mod- %s seconds ---" % (time.time() - start_time))
#mdp1 = discountedMDP(critere, stateSpace, actionSpace, trans, Reward,gamma)

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