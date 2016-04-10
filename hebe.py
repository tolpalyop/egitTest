# coding: utf-8
'''

@author: stuff
'''
from collections import deque

word = 'Python'
word[0]  # character in position 0

word[5]  # character in position 5
word[-1]  # last character

word[-2]  # second-last character
word[0:2]  # characters from position 0 (included) to 2 (excluded)

word[2:5]  # characters from position 2 (included) to 5 (excluded)
test = range(3, 6)
print "test is" + '... ermm', test
args = [3, 6]
print args
range(*args)            # call with arguments unpacked from a list

print word*3


if "P" in word:
    print "there's a P in", word

if "X" not in word:
    print "there's no X in", word


my_eyes = 'Blue'
my_hair = 'Brown'
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

str = "this is string example....wow!!!";

print str.ljust(50, '0')
print str.ljust(5, '0')
print str.rjust(50, '0')
print str.rjust(12, '0')

print r'C:\some\name'  # note the r before the quote

print """\
Usage: thingy [OPTIONS]
     multi
     lines!
"""

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')

a.insert(2, -1)
a.append(333)
a

a.index(333)

a.remove(333)
a

a.reverse()
a

a.sort()
a

a.pop()

a

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack


queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue       

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
    print b
    a, b = b, a+b

# x = int(raw_input("Please enter an integer: "))
x = 4;

if x < 0:
    x = 0
    print "negative so set to 0"
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'




words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)
    
    
    
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

words        
        
        
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]
        
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'
        
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num
        
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

# Now call the function we just defined:
fib(2000)

print "mark"

def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print f100                # write the result

    
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint        
   
   
#    This function can be called in several ways:
# 
#     giving only the mandatory argument: ask_ok('Do you really want to quit?')
#     giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
#     or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
     
#  Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:    
def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

#If you dont want the default to be shared between subsequent calls, you can write the function like this instead
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f2(1)
print f2(2)
print f2(3)

     
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword                



#
# When a final formal parameter of the form **name is present, it receives a 
# dictionary (see Mapping Types — dict) containing all keyword arguments except
#  for those corresponding to a formal parameter. This may be combined with a 
#  formal parameter of the form *name (described in the next subsection) which 
#  receives a tuple containing the positional arguments beyond the formal 
#  parameter list. (*name must occur before **name.) For example, if we define 
#  a function like this:
# 

def cheeseshop(kind, *arguments, **keywords):
    """ Test
    
    g
    """
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")        

#===============================================================================
# Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:
#===============================================================================
# This function returns the sum of its two arguments
lambda a, b: a+b

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)

#Another use is to pass a small function as an argument:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs



#filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true.
def fx(x): return x % 3 == 0 or x % 5 == 0

filter(fx, range(2, 25))

#map(function, sequence) calls function(item) for each of the sequence’s items and returns a list of the return values
def cube(x): return x*x*x

map(cube, range(1, 11))

#note number of sequences must match number of args
seq = range(8)
def add(x, y): return x+y

map(add, seq, seq)

#reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on. For example, to compute the sum of the numbers 1 through 10:
def addz(x,y): return x+y

reduce(addz, range(1, 11))
