'''
Created on Jul 1, 2014

@author: mrich
@module: test
@parent: 

This is an example of how the constants are imported
and accessed in an external file
'''

from CONST_GRP1 import *
from CONST_GRP2 import *

CG1 = CONST_GRP1()

print CG1.items()
CG1.printitems()

CG2 = CONST_GRP2()
print CG2.items()
CG2.printitems()

