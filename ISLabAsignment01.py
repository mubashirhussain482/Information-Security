# Encrypt function
def caesar_encrypt(text,shift):
    encrypted_text=""
    for letter in text:
        # For lowercase letters
        if letter>='a' and letter<='z':
            encrypted_text+=chr((ord(letter)+shift-97)%26+97)
        # For uppercase letters
        elif letter>='A' and letter<='Z':
            encrypted_text+=chr((ord(letter)+shift-65)%26+65)
        # For spaces and special characters
        else:
            encrypted_text+=letter
    return encrypted_text
# Decrypt function
def caesar_decrypt(ciphertext,shift):
    decrypted_text=""
    for letter in ciphertext:
        if letter>='a' and letter <='z':
            decrypted_text += chr((ord(letter)-shift-97)%26+97)
        elif letter>='A' and letter<='Z':
            decrypted_text+=chr((ord(letter)-shift-65)%26+65)
        else:
            decrypted_text+=letter
    return decrypted_text
# Main program
text="I am Mubashir and I have 500$ in my account and My gmail account is malikmubashirhussain482@gmail.com"
shift=4
encrypted=caesar_encrypt(text,shift)
#Encrypt method call
print("Encrypted Text:",encrypted)
#Decrypt method call
decrypted=caesar_decrypt(encrypted,shift)
print("Decrypted Text:",decrypted)