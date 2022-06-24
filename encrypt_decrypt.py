from cryptography.fernet import Fernet

# asks if the key needs to be changed
changeKey=input("Do you want change key ? 1 = yes / 2 = no :") 
# yes and save it to file
if changeKey=="1":
    key = Fernet.generate_key() 
    with open('filekey.key', 'wb') as filekey: 
        filekey.write(key)
    print("The encryption key has changed !") 
    print(key.decode('utf8'))
# no and will recover the key in the file
elif changeKey =="2":     
    with open('filekey.key', 'rb') as filekey: 
        key = filekey.read() 
    print(key.decode('utf8'))

# function encrypt          
def encrypt(key):
    fernet = Fernet(key) 
    with open('chat.jpg', 'rb') as original_file: 
        original = original_file.read() 
    encrypted = fernet.encrypt(original) 
    with open('chat.jpg', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted) 

# function decrypt          
def decrypt(key):
    fernet = Fernet(key) 
    with open('chat.jpg', 'rb') as encrypted_file: 
        encrypted = encrypted_file.read() 
    decrypted = fernet.decrypt(encrypted) 
    with open('chat.jpg', 'wb') as dec_file: 
        dec_file.write(decrypted) 

print(key.decode('utf8'))

choice=input("Do you want encrypt/decrypt ? 1 = encrypt / 2 = decrypt :") 
# yes and save it to file
if choice=="1":
    encrypt(key)
# no and will recover the key in the file
elif changeKey =="2":     
    decrypt(key)
