#Bit commitment
import hashlib
import uuid
def commit(msg):
    key=uuid.uuid4().hex    #RandomlyGeneratedKey
    #print key,"KEY"
    m=key.encode()+msg.encode()
    #print m
    return hashlib.sha256(m).hexdigest(),key
    
def verify(com,key,msg):
    m=key.encode()+msg.encode()
    #print m
    #print com,"com"
    #print hashlib.sha256(m).hexdigest(),"newhash"
    if com==hashlib.sha256(m).hexdigest():
        print "Verified"
        return True
    else:
        print "OOPS"
        return False
msg=raw_input("Enter your Message:")
com,key=commit(msg)
print key,"Key"
print "Hash of your message is "+ com
verify(com,key,msg)



