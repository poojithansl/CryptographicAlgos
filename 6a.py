import random
p=input("Enter p")
g=input("Enter g")
#dIFFIEhellman
def pubkey(m):
    pub_key=pow(g,m)%p
    return pub_key
def privkey():
    m=random.randrange(1000)
    return m
def getsesskey(m,pubkey):
    return pow(pubkey,m)%p
def check(s1,s2):
    return s1==s2
        
a,b=privkey(),privkey()
A,B=pubkey(a),pubkey(b)
s1,s2=getsesskey(a,B),getsesskey(b,A)
print check(s1,s2)

