#! /usr/bin/python3
import getopt, sys
import sys
import segypy

from test1 import *
b=[1,2,3]
c=[2,3,4]

args = '-a -b -cfoo -d bar a1 a2'.split()
args
optlist, args = getopt.getopt(args, 'abc:d:')
optlist
print(args)

print("hello, the asnswer"+str(add_vectors(b,c)))
#plot1()
#plot2()
