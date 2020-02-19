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
import conversions as cv


def encode(vectorList, Mat):
    result_str = ''
    for vector in vectorList:
        vectorF = np.array([[int(vector[0])], [int(vector[1])]])
        R = Mat.dot(vectorF)
        if R.shape == (2, 1):
            y1 = R[0]
            y2 = R[1]
            y1 = y1%27
            y2 = y2%27
            vect = [y1, y2]
            result_str += cv.convertNumToText(vect)
        else:
            print("Il y a une erreur quelque part.")
            break
    return result_str