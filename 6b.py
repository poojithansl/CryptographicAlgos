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
    if s1==s2:
        return True
    else:
        return False
a,c,b=privkey(),privkey(),privkey()
A,C,B=pubkey(a),pubkey(c),pubkey(b)
s1,s2=getsesskey(a,C),getsesskey(c,A)
print "A to C key exchange;"+str(check(s1,s2))

s3,s4=getsesskey(b,C),getsesskey(c,B)
print "C to B key exchange;" + str(check(s1,s2))

