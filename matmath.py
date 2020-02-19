#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vayzz
#
# Created:     19/02/2020
# Copyright:   (c) vayzz 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np

def defineMat(): #definit la matrice d'encodage
    print("Voici la matrice qui va permettre d'encoder votre message: \n\
        A:      [ {} {} ]\n\
                [ {} {} ]".format('a11', 'a12', 'a21', 'a22'))
    casesMatrice = ['a11', 'a12', 'a21', 'a22']
    for i in range(0, 4):
        usr_i = input('%s = ' % casesMatrice[i])
        casesMatrice[i] = int(usr_i)
    m_Mat = np.array([[casesMatrice[0], casesMatrice[1]], [casesMatrice[2], casesMatrice[3]]])
    if np.linalg.det(m_Mat) != 0:
        print("Voici la matrice qui va permettre d'encoder votre message: \n\
            A:      [ {} {} ]\n\
                    [ {} {} ]".format(casesMatrice[0], casesMatrice[1], casesMatrice[2], casesMatrice[3]))
    else:
        print("det(A) = 0")
        print("Cela signifie que votre matrice n'a pas d'inverse donc pas utilisable pour le chiffrement de Hill.")
        input()
    return m_Mat

def inverserMat(Mat):
    return np.linalg.inv(Mat)