'''
Abstract Class:

Abstract class is class where it constructs with one or more abstract methods.

Abstract method is normal method where it has no implementation.

Abstract class will be having a set of methods and those set of methods must be
be created within any child classess build from the "abstract class"

Usage:

In Python, abstract base classes provide a blueprint for concrete classes. 
They don't contain 
implementation. Instead, they provide an interface and make sure that 
derived concrete classes are properly implemented. Abstract base classes 
cannot be instantiated.
'''
#Example 1:

from abc import ABC, abstractmethod

class HomeAbstractRoom(ABC):
    def __init__(self,value):
        self.value = value
        pass

    @abstractmethod    
    def trialMethod(self):
        pass

class clusterHomeOne(HomeAbstractRoom):

    def trialMethod(self):
        print "Cluster One",self.value

class clusterHomeTwo(HomeAbstractRoom):
    
    def trialMethod(self):
        print "Cluster two",self.value

class clusterHomeThree(HomeAbstractRoom):

    def trialMethod(self):
        print "Cluster three",self.value


X = clusterHomeOne(1)
X.trialMethod()

Y = clusterHomeTwo(2)
Y.trialMethod()

Z = clusterHomeThree(3)
Z.trialMethod()


--------------------------------------------------------
# Concrete methods
------------------------------------------------------

from abc import ABC, abstractmethod

class HomeAbstractRoom():

    def __init__(self,value):
        self.value = value
    
    def trialMethod(self):
        print("Permission granted!")
        pass

class clusterMethodOne(HomeAbstractRoom):

    def trialMethod(self):
        super().trialMethod()
        print("Cluster method:"self.value)

X = clusterMethodOne(1)
X.trialMethod()

---------------------------------------------------------------------------


