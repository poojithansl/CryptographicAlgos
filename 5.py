import math  #h=g^x
h=input("h: ")
g=input("g: ")
p=input("p: ")
m=math.ceil(math.sqrt(p))
m=int(m)
aj=[0]*m
for i in range(m):
    aj[i]=pow(g,i*m)
ainvm=pow(g,p-2,p)
gamma = h
for i in range(m):
    if gamma in aj:
    	j = aj.index(gamma)
        print (j*m)+i
        break
    gamma=(gamma*ainvm)%p

