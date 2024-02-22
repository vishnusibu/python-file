#Function
#recursion
# it call itself
'''
def sum1():
    ........
    ........
    sum1()
    ........
    sum1()
'''
num=3
def fact (a):
    if a==1:
        return 1
    else:
        return(a*fact(a-1))
print(fact(num))

num=6
def maha(a):
    if  a==2:
        return 2
    else:
        return(a*maha(a-1))
print(maha(num))

fibo=6
def vishnu(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return(vishnu(a-1)+vishnu(a-2))
print(vishnu(fibo))
