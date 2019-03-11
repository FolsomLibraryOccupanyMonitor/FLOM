import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

#Program to generate and use rsa encryption


#encrypt_message function is set on all rasberry pi's

#decrypt_message function is set on the backend of our server

#Generate public key given to all
def generate_public_key(key):
	publickey = key.publickey() # pub key export for exchange
	return publickey

#Generate private key
def encrypt_message(message, publickey):
	encrypted = publickey.encrypt(message, 32)
	return encrypted

def decrypt_message(message, key):
	decrypted = key.decrypt(ast.literal_eval(str(message)))
	return decrypted

message = raw_input("Enter a message:")
random_generator = Random.new().read

#Generates random number for key generation
random = RSA.generate(1024, random_generator)

#generates public key for all rasberry keys
pub_key = generate_public_key(random)
print(message)

#encrypts message on rasberry pi which is sent to server (http request)
e_message = encrypt_message(message,pub_key)
print(e_message)

#decrypts message on the servers end using the random number generated
d_message = decrypt_message(e_message,random)
print(d_message)