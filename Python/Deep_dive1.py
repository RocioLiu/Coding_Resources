### Multi-Line Statements and String ###

## Implicit
a = [1, 2, 3]

a = [1, 2,
     3, 4, 5]

a = [1, #item 1
     2]

a = (1 #1
    ,2 #2
    ,3)

a = {'key1': 1 # value for key 1
    ,'key2': 2 # value for key 2
    }

def my_func(a, #commit...
            b, #commit...
            c):
    print(a, b, c)

my_func(11,22,33)


## Explicit
a = 10
b = 20
c = 30

if a > 5 \
        and b > 10 \
        and c > 20:
    print('yes')

# Multi-line string
a = '''This is a string'''
a
a = '''This 
is a string'''
a
print(a)

a = '''This 
    is a string 
            that is created over multiple lines'''
print(a)

def my_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a

print(my_func())


def my_func():
    a = '''a multi-line string
that is not indented in the second line'''
    return a

print(my_func())