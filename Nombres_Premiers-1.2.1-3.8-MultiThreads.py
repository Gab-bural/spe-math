#-------------------------------------------------------------------------------
# Name:        Nombres Premiers ?
# Purpose:            Determiner si un nombre est premier
#
# Author:      Gabriel BUREAU
#
# Created:     07/10/2017
# Copyright:   (c) Gabriel BUREAU 2017
# Licence:     <your licence>
# Version :    1.2.1
#-------------------------------------------------------------------------------
from math import *
import time
import concurrent.futures

#vars de test:
#     188748146801 |-> 0.037s
#     1234567891234529    |-> 2.78s
#     2305843009213693951 |->    141.45s
#     23981195285473  |-> 0.384s
#     67280421310721 <=> (2^64+1)/274177   |->  0.637s
#     170141183460469231731687303715884105727 <=> M127 |-> Trop long
#     20988936657440586486151264256610222593863921 <=> (2^148+1)/17   |-> Trop long
#
#       Programme dÃ©veloppÃ© sous Python 3.8
#       isqrt - > permet d'obtenir un int (pas de passage a float)
#       ne fonctionne pas sans Python 3.8 ou gmpy2
#
#      Ce programme utilise l'hyperthreading : calculs en multithreads dÃ©synchronisÃ©s
#
#


def is_prime(x, s=3, inc=2):     #Cette fonction permet de dire si x est premier, avec s nombre de depart (par defaut 3) et inc l'incrementation a chaue tour (par defaut 2 : on saute les nombres impairs)
    if x == 2:
        return True
    y = isqrt(x)
    if x%2 == 0:
        return False
    if x%10 == 5:
        return False
    for i in range(s, y+1, inc):
        if x % i == 0:
            return False
    return True


def ListOfPrimeNumbers(a):       # CrÃ©e la liste et la remplie Ã  l'aide de is_prime()
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

def is_primeHP(x):  #
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        p0 = executor.submit(is_prime, x, 3, 16)
        p1 = executor.submit(is_prime, x, 5, 16)
        p2 = executor.submit(is_prime, x, 7, 16)
        p3 = executor.submit(is_prime, x, 9, 16)
        p4 = executor.submit(is_prime, x, 11, 16)          # On cree 8 threads
        p5 = executor.submit(is_prime, x, 13, 16)          # On decoupe le travail en 8 avec inc = 16 :
        p6 = executor.submit(is_prime, x, 15, 16)          # 2*8 = 16; 3 + 16 = 19, 19 > 17
        p7 = executor.submit(is_prime, x, 17, 16)
    if p0.result() and p1.result() and p2.result() and p3.result() and p4.result() and p5.result() and p6.result() and p7.result():
        return True
    else:
        return False






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
        if u_input <= 19:
            if is_prime(u_input):
                print("Le nombre " + str(u_input) + " est premier")

            else:
                print("Le nombre " + str(u_input) + " n'est pas premier")

        else:
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