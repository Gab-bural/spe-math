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
import stringparser as sp
import encode as e
import decode as d
import conversions as cv
import matmath as mm
import encodingChart as eC

from textwrap import wrap
import numpy as np #pip install numpy to work
import os

def main():

    usr_input = input("Voulez vous encoder ou decoder?(E/D)")
    usr_input = usr_input.upper()

    if usr_input == 'E':
        s = sp.getString()
        vectorList = cv.convertTextToNum(sp.parseString(s))
        Mat = mm.defineMat()
        print(e.encode(vectorList, Mat))
        input()
    elif usr_input == 'D':
        s = sp.getString()
        vectorList = cv.convertTextToNum(sp.parseString(s))
        Mat = mm.defineMat()
        print(d.decode(vectorList, Mat))
        input()
    else:
        print("Veuillez reessayer")
        input()


if __name__ == '__main__':
    main()
