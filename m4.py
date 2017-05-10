
from __future__ import print_function
import random

def abc(c):
# multis en 4 favos
    cbs = [
    		[1, 4, 2, 5],
    		[1, 4, 2, 9],
    		[1, 8, 2, 5],
    		[1, 8, 2, 9],
    		[1, 4, 2, 6],
    		[1, 4, 2, 7],
    		[1, 8, 2, 6],
    		[1, 8, 2, 7],
    		[2, 5, 3, 6],
    		[2, 5, 3, 7],
    		[2, 9, 3, 6],
    		[2, 9, 3, 7],
    		[2, 5, 3, 4],
    		[2, 5, 3, 8],
    		[2, 9, 3, 4],
    		[2, 9, 3, 8],
    		[3, 6, 1, 4],
    		[3, 6, 1, 8],
    		[3, 7, 1, 4],
    		[3, 7, 1, 8],
    		[3, 6, 1, 5],
    		[3, 6, 1, 9],
    		[3, 7, 1, 5],
    		[3, 7, 1, 9],
    	]

    l = [0,1,2]
    print(r[:],c)
    for e1,i in enumerate(cbs):
        p = random.sample(l[:3],2)
        if (2 in p):
            for j in i:
                print(c[j], end='-')
            print()


# LT 9 premiers favos
c= [0,18,5,13,8,7,11,17,6,4,15,1,5,16,12,2,18,3,10]
d = '10may2017'
r = [d,'r1c1']
abc(c)
c = [0]+random.sample(c[1:6],5)+c[6:]
abc(c)
