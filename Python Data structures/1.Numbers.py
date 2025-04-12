# Assigning the values in python

a=10

a=20  # Now the a value will be updated a 10 to 20

b= 10.0/10  # will give float values

a,b,c = 10,'stringOne',12.2

x,y,z = a,b,c  # Swapping the values


del a  # deleting the variable

del x


# 2. Absolute values will generate only the positive integers

c=-99
d= 10

abs(-99/10) 

abs(-99+10.0)

b = round(a, 2)

#cohersion 

outVal = int(a) + float(b)

# 3. Exponential

a=5
b=2

a**2   # a^2

a**3   # a^3

a**b   #5^2

# 4. type operator

var_one = 5

var_two = 'Python'

var_three= 22.6

var_four = '9.7'

var_five = [1,2,5,8,9,6,'a','b']

type(var_one)  # will give type of variable like str, int or something



--------------------------------------------------------------------------
#DATA TYPES
-=------------------------------------------------------------------

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

int(100)

str("Halooo Python")

float(10.25)

complex(100j)

bool(2)

bytes(2)

memoryview(bytes(2))

range(5)
#display the data type of x:
print(type(x)) 











