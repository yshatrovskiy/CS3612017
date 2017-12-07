# pylint: disable-all

# NOTE : Python 2.7 does not require parenthesis to print
# Python 3 does however


# Excercise 1
print (5/3)
print 5%3
print 5.0 / 3
print 5/3.0
print 5.2%3

#Exercise 2
print 2000.3**200
print 1.0 + 1.0 - 1.0
print 1.0 + 1.0e20 - 1.0e20

#Exercise 3
print float(123)
print float('123')
print float('123.23')
print int(123.23)
print int('123.23')
print int(float('123.23'))
print str(12)
print str(12.2)
print bool('a')
print bool(0)
print bool(0.1)

#Exercise 4
print range(5)
print type(range(5))


#Exercise 5
numFound = 0
x = 11
while numFound < 20:
    if x % 2 == 0 and x % 7 == 0 and x % 11 == 0:
        print x
        numFound = numFound + 1
    x = x + 1


# Exercise 6A
def printme(n):
    if(n < 2):
        return False
    x = 2
    isPrime = True
    while(x < n):
        if((n % x) == 0):
            isPrime = False
        x = x + 1
    return isPrime

# 2,3,5,7,11,13,17,19,23
print printme(2)
print printme(1)
print printme(0)
print printme(-1)
print printme(191)
print printme(192)
print printme(193)
print printme(197)


# Exercise 6B
def betterprime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True 
    k = 1
    value = 0
    isprime = False
    while value <= n and isprime == False:
        value = 6 * k
        if((value + 1) == n) or ((value - 1) == n):
            isprime = True
        k = k + 1
    return isprime

print betterprime(2)
print betterprime(3)
print betterprime(5)
print betterprime(7)
print betterprime(11)
print betterprime(-1)
print betterprime(191)
print betterprime(192)
print betterprime(193)
print betterprime(197)

#Exercise 7
rlist = ['a','b','c','d','e']

def printelements(rlist):
    count = 0
    print rlist
    for i in rlist:
        count = count + 1
        print i
printelements(rlist)

def reverseList(r):
    newList = []
    for i in r:
        newList.insert(0, i)
    for x in newList:
        print x
reverseList(rlist)

def customLength(lList):
    itemCount = 0
    for i in lList:
        itemCount = itemCount + 1
    return itemCount

print customLength(rlist)

#Exercise 8
a = ['a','b','c','d','e']
b = a
print a
b[1] = 'Change One'
# A[1] also changed since they are both pointing to the same object
print a

c = a[:]
print c
c[2] = 'Change Two'
print a
#No change because it creates a shallow copy

def set_first_elem_to_zero(l):
    l[0] = 0
    return l

print a
set_first_elem_to_zero(a)
print a


# Exercise 9
sets = [[3, 4], [5, 6], [9, 10], [45, 65]]
print sets

def innerList(l):
    newList=[]
    for p in l:
        for x in range(2):
            newList.append(p[x])
    return newList
  
otherList = innerList(sets)
print otherList


# Exercise 10
import matplotlib.pyplot as plt
import math
import numpy as np

x = np.linspace(0, 2, 1024)
y = ( (np.sin(x-2)**2) * (np.e**(-x**2)))
plt.plot(x,y)
plt.ylabel('Time')
plt.xlabel('Speed')
plt.title('Exercise 10: Time vs. Speed')
plt.show()


# Exercise 11
def almostFactorial(list):
    if (list is not None):
        if len(list) > 0:
            product = 1
            for i in list:
                product = product * i
            return product
  
inputlistOne = [1, 2, 3, 4]
inputlistNone = []
print almostFactorial(inputlistOne)
print almostFactorial(inputlistNone)

inputlistTwo = [7, 8, 9, 10, 11, 12]
inputlistThree = None

def almostFactorialRec(inputlist):
  if (inputlist is not None):
    if(len(inputlist) == 0):
      return 1
    else:
      return inputlist[len(inputlist)-1] * almostFactorialRec(inputlist[:-1])

print almostFactorialRec(inputlistTwo)
print almostFactorialRec(inputlistThree)


# Exercise 12
def fibo(n):
    if n >= 0 and n < 38:
        if n==0: 
            return 0
        elif n == 1:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)
    else:
        return "Number out of range"
print fibo(-1)   
print fibo(14)
print fibo(38)



# Exercise 13
import re
with open('emails.txt') as file:
    lines = file.read()
    match = re.findall(r'[\w\"\.-@]*[\w\"\.-]+@[\w\.-]+\.[\w]+', lines)
    print (match)