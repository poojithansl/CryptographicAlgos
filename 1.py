import hashlib
def hash_short(message, length=16):
        return hashlib.sha1(message).hexdigest()[:length/4]
def check(m1,m2,k):
    if hash_short(m1,k)==hash_short(m2,k):
        print "True"
        print m2 
m1="sai lakshmi poojitha nandigam"
fp=open('Data/nietzsche.txt','r')
lines=fp.readlines()
cnt=0
k=input("Length:")
for line in lines:
    #print line
    words=line.split()
    for i in range(len(words)):
        for x in range(1,len(words)-i-1):
            m2=words[i:i+x]             #All Ngrams
            m2=" ".join(m2)
            if check(m1,m2,k):
                print m2
                break
    
    
