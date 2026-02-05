from random import *
def to_binary(x):
    x=int(x)
    bits=""
    while x>0:
        bits=str(x%2)+bits
        x//=2
    if len(bits)<8:
        bits="0"*(8-len(bits))+bits
    return bits
def to_decimal(x):
    dec=0
    x=x[::-1]
    for i in range(len(x)):
        dec+=int(x[i])*2**i
    return dec

def xor(a,b):
    return (a+b)%2

def enc(message,key):
    encrypted=[]
    for i in range(len(message)):
        k=""
        for ii in range(len(message[i])):
            k+=str(xor(int(message[i][ii]),int(key[i][ii])))
        encrypted+=[k]
    return encrypted

def dec(message,key):
    return enc(message,key)

message=input("Enter the message: ")
message=[to_binary(ord(i))  for i in message]
key=["".join(str(randint(0,1)) for _ in range(8)) for _ in range(len(message))]
encryp=enc(message,key)
encrypted=""
for i in encryp:
    encrypted+=str(chr(to_decimal(i)))
print("THE ENCRYPTED MESSAGE IS:",encrypted)

decryp = dec(encryp, key)
decrypted = ""
for i in decryp:
    decrypted += chr(to_decimal(i))
print("THE DECRYPTED MESSAGE IS:",decrypted)