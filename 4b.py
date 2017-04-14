import random
import hashlib
import string


def key_generator():
	return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(256))

def commit(msg,key):
	return hashlib.sha256(msg+key).hexdigest()

def verify(com,key,msg):
	if(hashlib.sha256(msg+key).hexdigest() == com):
		print "verified"
	else:
		print "Not verified"

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

def modmulinv(e,z):
	d = 0
	x1 = 0
	x2 = 1
	y1 = 1
	temp_b = z

	while e > 0:
	    t1 = temp_b/e
	    t2 = temp_b - t1 * e
	    temp_b = e
	    e = t2
	    
	    x = x2- t1* x1
	    y = d - t1 * y1
	    
	    x2 = x1
	    x1 = x
	    d = y1
	    y1 = y

	if temp_b == 1:
	    return d + z 

def rsa_generatekey():
	p=9769
	q=9781
	n = p*q
	z = (p-1)*(q-1)
	g = 0
	while g!=1:
		e = random.randrange(1,z)
		g = gcd(z,e)
	d = modmulinv(e, z)
	return ((e,n),(d,n))

def rsa_encrypt(com,key):
	e, n = key
	cipher = [pow(ord(x),e,n) for x in com]
	#print cipher
	return cipher

def rsa_verify(cipher,com,key):
	d, n = key
	# print d,n
	# print cipher
	plain = [chr(pow(num,d,n)) for num in cipher]
	# print com
	if (com == ''.join(plain)):
		print "RSA-Verified"
	else:
		print "RSA-not Verified"



def main():
	#message
	msg = raw_input("Enter a message:")
	#random key
	key = key_generator()
	#print "key is",key
	#print "msg is",msg
	#committing message
	com = commit(msg,key)
	#verifying message
	verify(com,key,msg)

	#RSA-encryption
	#key_pair
	sk,pk = rsa_generatekey()
	#encryption
	cipher = rsa_encrypt(com,sk)
	#Decryption & Verification
	rsa_verify(cipher,com,pk)


if __name__ == '__main__':
	main()