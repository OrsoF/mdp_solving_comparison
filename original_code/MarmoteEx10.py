#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Marmote and MarmoteMDP and pyMarmoteMDP are free softwares: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#Marmote is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with MarmoteMDP. If not, see <http://www.gnu.org/licenses/>.

#Copyright 2019 Emmanuel Hyon, Alain Jean-Marie
"""
 @brief Exemple1
 @author Calic Petar
 @date Nov 2020
 @version 1.1
 
 Cet exemple de test fait créer un MDP tout simple

"""
from pyMarmoteMDP import *
import time

def marmoteEx10():
    beta=0.5
    critere = "max"
    epsilon = 0.0001
    maxIter = 700

    dimSS = 2
    dimSA = 2
    actionSpace = marmoteInterval(0,dimSS-1)
    stateSpace = marmoteInterval(0,dimSA-1)

    print("#")

    #vector to store the dimension
    trans=sparseMatrixVector(dimSA)

    P0 = sparseMatrix(dimSS)
    P0.addToEntry(0,0,0.6)
    P0.addToEntry(0,1,0.4)
    P0.addToEntry(1,0,0.5)
    P0.addToEntry(1,1,0.5)
    trans[0] = P0

    P1 =sparseMatrix(dimSS)
    P1.addToEntry(0,0,0.2)
    P1.addToEntry(0,1,0.8)
    P1.addToEntry(1,0,0.7)
    P1.addToEntry(1,1,0.3)
    trans[1] = P1

    Reward  = sparseMatrix(dimSS, dimSA);
    Reward.addToEntry(0,0,4.5)
    Reward.addToEntry(0,1,2)
    Reward.addToEntry(1,0,-1.5)
    Reward.addToEntry(1,1,3)

    print("Debut de la construction MDP")
    start_time = time.time()
    mdp1 = discountedMDP(critere, stateSpace, actionSpace, trans, Reward,beta)
    build_time=(time.time() - start_time)
    print("modele --- %s seconds ---" % build_time)
    print("Fin de la construction MDP\n")

    print("Affichage MDP")
    mdp1.writeMDP()

    print("Calcul iteration valeur")
    #call the function to solve the MDP.       Ajout de time
    start_time = time.time()
    optimum = mdp1.valueIteration(epsilon, maxIter)
    vi_time=(time.time() - start_time)
    print("--- %s seconds ---" % vi_time )

    print("Calcul par iteration valeur modifiee")
    start_time = time.time()
    optimum2 = mdp1.policyIterationModified(epsilon, maxIter, 0.001, 100)
    pim_time=(time.time() - start_time)
    print("--- %s seconds ---" % pim_time)

    #call the function to solve the MDP
    print("Calcul par iteration valeur Gauss Seidel")
    start_time = time.time()
    optimum3 = mdp1.valueIterationGS(epsilon, maxIter)
    gs_time=time.time() - start_time
    print("--- %s seconds ---" % gs_time)

    #print("********************************")
    #print("Solution iteration valeur")
    #optimum.writeSolution()

    #print("Solution par iteration valeur modifiee") 
    #optimum2.writeSolution()

    #print("Solution par iteration valeur Gauss Seidel")
    #optimum3.writeSolution()

    print("********************************")
    return (build_time,vi_time,pim_time,gs_time)

marmoteEx10()