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
import matmath as mm
import numpy as np
import conversions as cv

def decode(vectorList, Mat):
    inv_Mat = mm.inverserMat(Mat)
    final_string = ""
    for vector in vectorList:
        vectorY = np.array([[vector[0]],[vector[1]]])
        vectorX = inv_Mat.dot(vectorY)
        x1 = vectorX[0]%27
        x2 = vectorX[1]%27
        vect = [x1, x2]
        result_str = cv.convertNumToText(vect)
        final_string+=result_str
    return final_string

