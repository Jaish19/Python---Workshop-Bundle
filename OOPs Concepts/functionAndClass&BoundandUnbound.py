-----------------------------------------------------------------------------
# defining the functions by passing an arguments:
-----------------------------------------------------------------------------
def fucn(a,b):
	c=a+b
	print c

func(5,8)

-----------------------------------------------------------------------------
# defining the functions with default arguments:
-----------------------------------------------------------------------------

def func(a,b=5):
	c=a+b
	print c

func(5,8)

------------------------------------------------------------------------------
# Defining the functions with return statement:
---------------------------------------------------------------------------------
# The return statement causes your function to exit and hand back a value to its caller.

def func(a,b=5):
	c=a+b
	return c
reVal=func(5,8)
print reVal


-----------------------------------------------------------------------------
# defining the class:
-----------------------------------------------------------------------------

class abc(object):
    def a(self,val):
        print "Hi A!!",val
    def b(self,val2):
        print 'Hi B!!'
        
obj=abc()
obj.a(5)
obj.b()


-----------------------------------------------------------------------------

# objects: states and behaviour of the classs.
# class:states and behaviour of an object

# constructor: will help to create an object very effectively
-----------------------------------------------------------------------------

class alphabets(object):
	def __init__(self,a,b):
		self.a=a
		self.b=b
		pass
	def A(self):
		print self.a + self.b

	def B(self):
		print self.a*self.b

bb=alphabets(5,9)
bb.A()
bb.B()


--------------------------------------------------------------------------------
'''
#DESTRUCTOR : 

A destructor is called when an object is deleted or destroyed

Destructor is used to perform the clean-up activity before destroying the object, such as closing database connections or filehandle. 
'''
class Student:
  
    # Initializing class named Student
    def __init__(self):
        print('The class named Student was created.')
  
    # Calling destructor
    def __del__(self):
        print('The destructor is called. Student is deleted.')
        
    def activity(self):
        print("working")
  
sObj = Student() 
del sObj


-----------------------------------------------------------------------------
# Bound and unbound method
-------------------------------------------------------------------------------
# Bound

class check():
        def __init__(self):
                pass
        def method(self,a,b):
                pass
instance = check()
print instance.method # print bound method instance
instance.method(1,2) # normal call or bound method

------------------------------------------------

# Unbound methd


class check():
        def __init__(self):
                pass
        def method(self,a,b):
                pass

print check.method # print unbound method instance
instance = check()
check.method(instance,1,2) # this call is the same as...
f= check.method
f(instance,1,2) # this one...

----------------------------------------
