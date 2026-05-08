# Step 1: Choose two small prime numbers
p=53
q=37
# Step 2: Compute n
n=p*q
# Step 3: Compute phi(n)
phi=(p-1)*(q-1)
# Step 4: Choose public key e (must be coprime with phi)
e=7
# Step 5: Find private key d (such that (e * d) % phi = 1)
def find_d(e,phi):
    for d in range(1,phi):
        if(e*d)%phi==1:
            return d
d = find_d(e,phi)
# Public and Private Keys
public_key=(e,n)
private_key=(d,n)
print("Public Key:",public_key)
print("Private Key:",private_key)
# ENCRYPT FUNCTION
def encrypt(message,public_key):
    e,n=public_key
    encrypted = []
    for char in message:
        m=ord(char)          # Convert character to number
        c=pow(m,e,n)       # RSA formula: c = m^e mod n
        encrypted.append(c)
    return encrypted
# DECRYPT FUNCTION
def decrypt(ciphertext,private_key):
    d,n=private_key
    decrypted=""
    for c in ciphertext:
        m=pow(c,d,n)       # RSA formula: m = c^d mod n
        decrypted+=chr(m)    # Convert number back to character
    return decrypted
message="Mubashir Hussain"
#Calling encrypt and decrypt function
encrypted_message=encrypt(message,public_key)
decrypted_message=decrypt(encrypted_message,private_key)
print("\nOriginal Message:",message)
print("Encrypted Message:",encrypted_message)
print("Decrypted Message:",decrypted_message)