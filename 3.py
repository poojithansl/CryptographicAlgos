import math
import random
def perfpow(n):
    if n<=1:return True
    for x in range(2,int(math.sqrt(n))+1):
        p=x
        while p<=n:
            p=x*p
            if p==n:
                return True
    return False
def checkwitness(a,r,d,n):
    if pow(a,d)%n==1:
        return False
    for i in range(r):
        if pow(a,2**i*d,n)==n-1:
            return False
    return True
def getrd(n):
    d=n-1
    r=0
    while d%2==0:
        d=d/2
        r+=1
    return r,d
def isprime(n,t=100):
    if n==2:
        return True
    if n%2==0 or perfpow(n):
        return False
    #n-1=2^r*d r>=1,d->odd
    r,d=getrd(n)
    #print 2**r*d,n-1
    for i in range(t):
        a=random.randrange(2,n-1)
        if checkwitness(a,r,d,n):
            return False
    return True
    
def getwitnessliars(n,t=100):
    witness,liar=[],[]
    r,d=getrd(n)
    for i in range(t):
        #a=random.randrange(2,n-1)
        for a in range(2,n-1):
            if checkwitness(a,r,d,n):
                witness.append(a)
            else:
                liar.append(a)
    print "StrongWitnesses:"
    print set(witness)
    print "StrongLiars:"
    print set(liar)
    return

def smallestprime(n):
    t=n+1
    while 1:
        #print t,isprime(t)
        if isprime(t)==True:
            print "SmallestPrimeGreater than n is "+ str(t)
            break
        t+=1
    return


n=input("Enter a number:")
if isprime(n):
    print "The Number is Prime"
else:
    print "The Number is Composite"
smallestprime(n)
getwitnessliars(n)
