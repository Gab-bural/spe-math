#-------------------------------------------------------------------------------
# Name:        Nombres Premiers ?
# Purpose:            Determiner si un nombre est premier
#
# Author:      Gabriel BUREAU
#
# Created:     07/10/2017
# Copyright:   (c) Gabriel BUREAU 2017
# Licence:     <your licence>
# Version :    1.1.0
#-------------------------------------------------------------------------------
from math import *
import time

import os


#vars de test:
#     188748146801 |-> 0.0529s
#     2305843009213693951 |->    199.05s
#     23981195285473  |-> 0.546s
#     67280421310721 <=> (2^64+1)/274177   |->  0.919s
#     170141183460469231731687303715884105727 <=> M127 |-> Trop long
#     20988936657440586486151264256610222593863921 <=> (2^148+1)/17   |-> Trop long
#
#       Programme développé sous Python 3.8
#       isqrt - > permet d'obtenir un int (pas de passage a float)
#       ne fonctionne pas sans Python 3.8 ou gmpy2
#
#
#




def is_prime(x):     #Cette fonction permet de dire si x est premier
    if x == 2:
        return True
    y = isqrt(x)
    if x%2 == 0:
        return False
    for i in range(3, y+1, 2):
        if x % i == 0:
            return False
    return True

def ListOfPrimeNumbers(a):       # Crée la liste et la remplie à l'aide de is_prime()
    i = 1
    x = 3
    liste = [2]
    t0 = time.time()

    while(i < a):
        if is_prime(x):
            liste.append(x)
            i+=1
        x+=2

    print(liste)
    print("\n Il y a dans cette liste " + str(len(liste)) + " nombres premiers")
    t1 = time.time()
    print(str(t1-t0)+"secondes")

    return liste

while(True):        #Main

    print("///////////////////////////////////////////////////////")
    print("/Tapez 1 pour savoir si un nombre est premier         /")
    print("/Tapez 2 pour avoir une liste de [x] nombres premiers /")
    print("///////////////////////////////////////////////////////")
    try:
        u_input = int(input(""))
    except:
        print ("Veuillez rentrer 1 ou 2, si vous voulez quitter le programme, tapez \"quit\"")
        u_input = 3


    if u_input == 1:
        u_input = int(input("Quel nombre ? "))
        t0 = time.time()

        if is_prime(u_input):
            print("Le nombre " + str(u_input) + " est premier")

        else:
            print("Le nombre " + str(u_input) + " n'est pas premier")

        t1 = time.time()
        print(str(t1-t0)+"secondes")

    elif u_input == 2:

        u_input = int(input("Combien voulez vous calculer de nombre premiers ? "))
        ListOfPrimeNumbers(u_input)

    elif u_input == "3" or "quit":
        quit()
    else:
        pass