--------------------------------------------------------------
#                 LIST COMPREHENSION -List comprehension is an elegant way to define and create list in Python.
--------------------------------------------------------------

# List comprehension is basically creating lists based on existing iterables.
# we iterate over an iterable and do something (optional!) with the items and then put them in a list.

-----------------------------------------------------------------------------------------

l1= [i for i in range(10)]

l1 = [i**2 for i in range(0,10,2)]

l2=[]


l1=[i for i in range(10) if i%2==0]


l1 =[i for i in range(10) if i > 5]

l1 = [str(i)*2 if i%2==0 else i for i in range(10)]

print(l1) # output: ['00', 1, '22', 3, '44', 5, '66', 7, '88', 9]

a='newgame'
expected = "NeWgAmE"
l1=''.join([a[i].upper() if i%2==0 else a[i] for i in range(len(a))])
print(l1)

--------------------------------------------------------------
#                 TUPLE COMPREHENSION
--------------------------------------------------------------

t1= (i for i in range(10))

l1=[1,2,4,'a','b']

t1=(i for i in l1 if type(i)==str)

# Though tuple comprehension is avail for tuple, final output will be in generator object. Do iterate to see the values.

--------------------------------------------------------------
#                 DICTIONARY COMPREHENSION
--------------------------------------------------------------

d4={i:i**2 for i in l1}


l1=[1,2,1,1,1,2,2,2,3,4,5,5]


d4={i:l1.count(i) for i in l1}


d4 ={i:l1.index(i) for i in l1}

--------------------------------------------------------------------
