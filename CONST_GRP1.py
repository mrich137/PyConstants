'''
Created on Jul 1, 2014

@author: mrich
@module: Constants.CONST_GRP1
'''
# import base class
from ConstBaseClass import *

class CONST_GRP1(ConstBaseClass):
    """ Constant Group 1 """
    def __init__(self):
        """ Constructor to define group1 constants """
        # DEFINE CONSTANTS HERE
        self.const1 = "g1c1"
        self.const2 = "g1c2"
        
        
        ''' Uncomment this line to prevent adding more attributes '''
        #self._locked = 1
  
def main():
    """ main function for module debug """
    CG1 = CONST_GRP1()
    print CG1.items()
    CG1.printitems()
              
if __name__ == '__main__':
    main()