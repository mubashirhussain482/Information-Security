import hashlib  # Library used for SHA256 hashing
# Step 1: Select two small prime numbers
p=17
q=11
# Step 2: Calculate modulus n
n=p*q
# Step 3: Calculate Euler's Totient Function
phi=(p-1)*(q-1)
# Step 4: Choose public exponent e (coprime with phi)
e=7
# Step 5: Function to calculate private key d
def find_d(e,phi):
    # d must satisfy (e × d) mod phi = 1
    for d in range(1,phi):
        if (e*d)%phi==1:
            return d
# Calculate private key
d = find_d(e,phi)
# Public and private key pairs
public_key=(e,n)
private_key=(d,n)
# Step 6: Create SHA256 hash of message
def create_hash(message):
    # Convert message to bytes and generate SHA256 hash
    hash_object=hashlib.sha256(message.encode())
    # Convert hexadecimal hash to integer
    return int(hash_object.hexdigest(),16)
# Step 7: Sign message using private key
def sign_message(message,private_key):
    d,n=private_key
    # Generate hash of the message
    message_hash=create_hash(message)
    # Sign the hash using RSA formula
    signature=pow(message_hash,d,n)
    return signature
# Step 8: Verify signature using public key
def verify_signature(message,signature,public_key):
    e,n=public_key
    # Generate hash of received message
    message_hash=create_hash(message)
    # Decrypt signature using public key
    decrypted_hash=pow(signature,e,n)
    # Compare hashes
    return message_hash%n==decrypted_hash
# Step 9: Testing the Digital Signature
message="Mubashir Hussain"
# Sign original message
signature=sign_message(message,private_key)
print("Original Message:",message)
print("Signature:",signature)
# Verify original message
print("Verification (Original):",verify_signature(message,signature,public_key))
# Modify the message slightly
modified_message="Mmubashir Hussain"
# Verify modified message
print("Verification (Modified):",verify_signature(modified_message,signature,public_key))