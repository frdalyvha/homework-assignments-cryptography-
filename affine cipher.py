def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def enc(message, key_a, key_b, alphabet):
    message = message.lower()
    alphabet = alphabet.lower()
    encrypted = ""
    m = len(alphabet)
    
    for i in message:
        if i not in alphabet:
            encrypted += i
        else:
            x = alphabet.find(i)
            encrypted += alphabet[(key_a * x + key_b) % m]
    return encrypted

def dec(message, key_a, key_b, alphabet):
    message = message.lower()
    alphabet = alphabet.lower()
    decrypted = ""
    m = len(alphabet)
    a_inv = mod_inverse(key_a, m)
    
    if a_inv is None:
        return "Cannot decrypt: invalid key_a"
    
    for i in message:
        if i not in alphabet:
            decrypted += i
        else:
            y = alphabet.find(i)
            decrypted += alphabet[(a_inv * (y - key_b)) % m]
    return decrypted


message = input("Enter the message you want to encrypt: ")
key_a = int(input("Enter key a (must be coprime with 26): "))
key_b = int(input("Enter key b (shift): "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if gcd(key_a, 26) != 1:
    print("Error: key_a must be coprime with 26!")
else:
    encrypted = enc(message, key_a, key_b, alphabet)
    print("Your encrypted message is:", encrypted)
    decrypted = dec(encrypted, key_a, key_b, alphabet)
    print("Your decrypted message is:", decrypted)