from math import factorial

""" Tuple.
 Delimited by parantheses. Items separated by commas
 len(tuple). iteration with for. Concatenation with + operator
 & repition with * operator
 Nested tuples
 Tuple unpacking with nested tuples
 can convert list to tuple easily
 in and not in operators
 """

t = ("hello", 1.2, 3)
print(t[0])

a = ((1,2),(3,4))
print(type(a))
print(a[1][1])

b = [5,22,3,89]
print(min(b))

(a,(b,c)) = (3,(2,1))
print(a)
print(b)

a = tuple([55,1,7])
print(a)
print(1 in a)

s = tuple("hello")
print(s)

""" Range
"""
x = range(5)
y = range(1,5)
for i in y:
    print(i)

z = list(x)
print(z)

"""List
slicing, start & stop index
negative index
append method, insert method
Copying lists: all shallow copies
s.copy(), list(s), s[:]
repition using * operator
To locate substrings -
.index("str"), in operator, count("str")
del seq[index], .remove() - to remove element
.sort(), .sort(reverse=True)
y = sorted(x) - gives sorted list y.
Similarly reversed
"""

l = "how are you my dear".split()
print(l[0])
print(l[-2])
print(l[1:-1])
print(l[2:])
print("are" in l)

a = [0]*9
print(a)

x1 = [2,5,7]
x2 = [5,7,8]
print(x1 + x2)

"""Dict
d.copy()
dict() - to convert from tuple
"""

d = {}
print(type(d))

"""Set
Great to remove duplicates
enclosed in curly braces {}
arbitrary order
set.add()
enables set operations - union, intersection, difference, issubset, issuperset, isdisjoint
"""

s = set()
print(type(s))

""" List comprehensions
Can be run on lists, tuples etc.
Format: [expr(item) for item in iterable]
"""

words = "Today it is boring and I don't know what to do".split()
lc = [len(word) for word in words]
print(lc)

test = [len(str(factorial(x))) for x in range(10)]
print(test)

""" Set comprehensions
"""

test2 = {len(str(factorial(x))) for x in range(10)}
print(test2)

""" Dictionary comprehensions
"""

country_to_cap = {"Orissa":"Bhubaneswar","AP":"Hyderabad","Mizoram":"Aizawl"}
cap_to_country = {capital:country for country,capital in country_to_cap.items()}
print(cap_to_country)

words = ['I', 'am', 'very', 'bored']
wdict = {w[0]:w for w in words}
print(wdict)

""" List comprehensions with predicates
Format: [expr(item) for item in iterable if predicate(item)]
"""

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return  False

evensquares = {x:x*x for x in range(20) if is_even(x)}
print(evensquares)

""" Iterator
"""

iterable = ['SPring', 'Summer', 'WInter']
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))

# tests
xx = [0] * (52)
print(xx)

board_state = [0] * (3 * 3 + 3)
print(board_state)
# following line is like j on outer loop & i on inner loop
b = [(i, j) for j in range(3) for i in range(4)
                if board_state[i + j * 4] == 0]
print(b)