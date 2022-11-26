rom os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    test=arr[m+1:]
    test.reverse()
    res=arr[0:m+1]+test
    arr[:]=res[:]
    return arr
