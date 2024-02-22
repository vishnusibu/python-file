#function
#sybtax:
#  def function_name():
#     // code
#   return
'''
def add():
    print('good moring')

add()

def add(a,b):
   
    return(a+b)
print(add(10,5))
print(add(100,10050))
print(add(100,10515))
print(add(100,150))
print(add(100,1050))

def multiplication(a,b):
    return(a*b)
print(multi(100,5))
print(multi(100,111))
print(multi(122,133))
print(multi(144,88))
print(multi(-10,-11))

def add(a,b):
    return(a+b)
print(add('good',' boy'))

def add(a):
    return(a+' good boy')
a='python'
print(add(a))

def add(*a):
    print(a[0]+a[3])
add(100,200,300,400)
#arbitrary keyword argument
def add(**a):
    print(a['c'])
add(b='python',c='c++')

def name (a,b=7):
    print(a+b)
name(10,5)


def name (a,b):
    print(a+b)
b=10    
name(10,b)

def name (a,b):
    return(a+b)
print(name(10,11))

#function
a=4
b=10
def sub(x,y):
    print(a-b)
print(sub(a,b))

def sub(x,y):
    return x-y
print(sub(a,b))

a=101
b=11
7
def sub(x,y):
    return x**y
print(sub(a,b))


#method 1 
a=[1,6,11,100,7]

def sub(a):
    for i in a:
        print(i*i,end=' ')
    print()
sub(a)
#method 2
a=[1,6,11,100,7]
def sub(a):
    for i in range(len(a)):
        print(a[i]*a[i],end=' ')
    print()
sub(a)
#method 3
a=[1,6,11,100,7]
print([i*i for i in a])

name=['apple','cherry','orenge','gova']

def jj(name):
    for i in name:
        if i=='cherry':
            print(i,end='')
        print()
jj(name)

def jj(name):
    for i in name:
        if i!='cherry':
            print(i,end=' ')
jj(name)

def add(a,b):
    return a+b
print(add(a=5,b=6))

def add (a=5,b=6):
    return a+b
print(add())


def add (a=5,b=6):
    return a+b
print(add(10,12))

def add (a=5,b=6):
    return a+b
print(add(10))
'''
x=[7,8,1,9,10,100]
def maha(x):
    maha=0
    for i in x:
        maha += i
    print(maha)
maha(x)

x=[7,8,1,9,10,100,25,54,0]

def vishnu(x):
    l=0
    for i in x:
        if i>=0:
            l=l+1
    print(l)
    
vishnu(x)
        















