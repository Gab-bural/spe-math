#-------------------------------------------------------------------------------
# Name:        String Parser
# Purpose:
#
# Author:      vayzz
#
# Created:     17/02/2020
# Copyright:   (c) vayzz 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from textwrap import wrap
import numpy as np #pip install numpy to work
import os


def getString():
    usr_input = input("Please type in your string: ")
    usr_input = usr_input.upper()
    return usr_input

def parseString(s):

    def isOdd(s):
        if len(s)%2!=0:
            return True
        else:
            return False

    stri = s.split(' ')
    stri_b = []
    final_string = ""
    for item in stri:
        if isOdd(item):
            buffer_item = item + '_'
            final_string += buffer_item
        else:
            final_string += item
    final_string = wrap(final_string, 2)
    print(final_string)
    return final_string






