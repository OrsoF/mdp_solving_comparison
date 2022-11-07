"""
 @brief Exemple1
 @author Calic Petar
 @date Nov 2020
 @version 1.1
 
 Cet exemple de test fait comparer trois resolutions d'un MDP tout simple'
 
"""

from MarmoteEx10 import *

temps = [0,0,0,0]

for i in range(10) :
    (tp0,tp1,tp2,tp3)=marmoteEx10()
    temps[0]+=tp0
    temps[1]+=tp1
    temps[2]+=tp2
    temps[3]+=tp3

temps[0]=temps[0]/10
temps[1]=temps[1]/10
temps[2]=temps[2]/10
temps[3]=temps[3]/10

print("construction, VI, PIM, GS")
print(temps)
