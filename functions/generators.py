# generators are special function in python
# that can be used to generate sequence of values
# instead of returning the value into from a function once
# we put the value into a memory space 
# generators are fast compared to lists 

def cube(limit):
    for i in range(1,limit+1):
        yield i**3

def fib(limit):
    a,b = 0,1
    for i in range(limit):
        yield a
        a,b = b, a+b

# example call:

#cubes = cube(5)
#print(next(cubes))
#print(next(cubes))
#print(next(cubes))

for c in cube(10):
    print(c)

for f in fib(15):
    print(f, end = '| ')


# wap to generate a list of even sqr using generators
# wap to generates a list of acronyms from a list of words using generators

def even_sqr(limit):
    for i in range(1,limit+1):
        if i % 2 == 0:
            yield i**2
        
#example call
for a in even_sqr(10):
    print(a)