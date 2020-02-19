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
import encodingChart as eC
import conversions as cv

def convertLetterToNum(l):
    for i in range(0, len(eC.encodingChart)):
        if l == eC.encodingChart[i]:
            return i

def convertTextToNum(s):
    vectorlist = []
    for i in range(0, len(s)):
        x1 = cv.convertLetterToNum(s[i][0])
        x2 = cv.convertLetterToNum(s[i][1])
        vectorword = [x1, x2]
        vectorlist.append(vectorword)
    return vectorlist  #chaque vecteur represente un mot; un mot etant 2 lettres

def convertNumToText(vector):
    y1 = eC.encodingChart[int(vector[0])]
    y2 = eC.encodingChart[int(vector[1])]
    result_str = str(y1)+str(y2)
    return result_str