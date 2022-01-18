# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

###############################################################


#!/bin/python

import math
import os
import random
import re
import sys

############# Before ###########################################

if __name__ == '__main__':
    n = int(raw_input().strip())


    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and 2<= n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and 6<= n <= 20:
        print('Weird')
    elif n % 2 == 0 and n >= 20:
        print('Not Weird') 

# 🐻＜FB
# まず偶数と奇数に大きく二つに分けるべし！可読性上がるし偶数を繰り返し書かなくていい
# 変数は左に置くべし！



############# After ##############################################

if __name__ == '__main__':
    n = int(raw_input().strip())


    if n % 2 == 1:
        print('Weird')
    
    if n % 2 == 0:
        if  n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        else:
            print('Not Weird') 




