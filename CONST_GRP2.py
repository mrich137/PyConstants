'''
Created on Jul 1, 2014

@author: mrich
@module: CONST_GRP2
'''
# import base class
from ConstBaseClass import *

class CONST_GRP2(ConstBaseClass):
    """ Constant Group 1 """
    def __init__(self):
        """ Constructor to define group1 constants """
        # DEFINE CONSTANTS HERE
        self.const1 = "g2c1"
        self.const3 = "g2c3"
        
        ''' Uncomment this line to prevent adding more attributes '''
        self._locked = 1

def main():
    """ Main function for module debug """
    CG2 = CONST_GRP2()
    print CG2.items()
    CG2.printitems()
              
if __name__ == '__main__':
    main()
