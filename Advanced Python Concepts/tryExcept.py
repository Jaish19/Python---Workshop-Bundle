'''
Finally block:

 The finally block will be executed no matter if the try block raises an error or not. This can be useful to close objects and clean up resources.
ERROR TYPES:

AttributeError  Raised when attribute assignment or reference fails.
IndexError  Raised when the index of a sequence is out of range.
ImportError Raised when the imported module is not found.
KeyError    Raised when a key is not found in a dictionary.
NameError   Raised when a variable is not found in local or global scope.
ValueError  Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError   Raised when the second operand of division or modulo operation is zero.
TypeError   Raised when a function or operation is applied to an object of incorrect type.
AssertionError  Raised when an assert statement fails.


EOFError    Raised when the input() function hits end-of-file condition.
FloatingPointError  Raised when a floating point operation fails.
GeneratorExit   Raise when a generator's close() method is called.
KeyboardInterrupt   Raised when the user hits the interrupt key (Ctrl+C or Delete).
MemoryError Raised when an operation runs out of memory.
NotImplementedError Raised by abstract methods.
OSError Raised when system operation causes system related error.
OverflowError   Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError  Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError    Raised when an error does not fall under any other category.
StopIteration   Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError Raised by parser when syntax error is encountered.
IndentationError    Raised when there is incorrect indentation.
TabError    Raised when indentation consists of inconsistent tabs and spaces.
SystemError Raised when interpreter detects internal error.
SystemExit  Raised by sys.exit() function.
UnboundLocalError   Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError    Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError  Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError  Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError   Raised when a Unicode-related error occurs during translating.
'''
----------------------------------------------------------------

# Example 1:

# Python program to handle simple runtime error
 
a = [1, 2, 3]
try: 
    print "Second element = %d" %(a[1])
 
    # Throws error since there are only 3 elements in array
    print "Fourth element = %d" %(a[3]) 
 
except IndexError:
    print "An error occurred"

finally:
    print "Finished the above case successfully..."
'''
#output:
    Second element = 2
An error occurred
'''
---------------------------------------------------------------

# Example 2:

# Program to handle multiple errors with one except statement
try : 
    a = 3
    if a < 4 :
 
        # throws ZeroDivisionError for a = 3 
        b = a/(a-3)
     
    # throws NameError if a >= 4
    print "Value of b = ", b
 
# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print "\nError Occurred and Handled"

'''
OUTPUT:

Value of b =  
Error Occurred and Handled
'''
-------------------------------------------------------------------

# Example 3 Raising an exception

# Program to depict Raising Exception
 
try: 
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not

'''
The output of the above code will simply line printed as “An exception” but a Runtime error will also occur in the last due to raise
statement in the last line. So, the output on your command line will look like
output:
Traceback (most recent call last):
  File "003dff3d748c75816b7f849be98b91b8.py", line 4, in 
    raise NameError("Hi there") # Raise Error
NameError: Hi there
'''
----------------------------------------------------------------

# Example 4:

from __future__ import division
def isDivide(x,y):
    try:
        if x >= 1:
            if x > y:
                print abs(x/y)
            elif y > x:
                print abs(y/x)
            else:
                raise ZeroDivisionError
    except ZeroDivisionError as e:
        print (e.message)
    else:
        print ("inside else")
    finally:
        print ("inside finally")
        # raise ZeroDivisionError

if __name__ == '__main__':
    isDivide(1, 10)
    # isDivide(10, 0)



#METHOD 2
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)


# METHOD 3


