def enc(message,key,alphabet):
    message=message.lower()
    alphabet=alphabet.lower()
    encrypted=""
    for i in message:
        if i not in alphabet:
            encrypted+=i
        else:
            encrypted+=alphabet[(alphabet.find(i)+key)%26]   
    return encrypted

def dec(message,key,alphabet):
    message=message.lower()
    alphabet=alphabet.lower()
    decrypted=""
    for i in message:
        if i not in alphabet:
            decrypted+=i
        else:
            decrypted+=alphabet[(alphabet.find(i)-key)%26]   
    return decrypted


message=input("Enter the message you want to encrypt: ")
key=int(input("Enter how many shifts you want to do: "))
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted=enc(message,key,alphabet)
print("Your encrypted message is:",encrypted)
decrypted=dec(encrypted,key,alphabet)
print("Your decrypted message is:",decrypted)