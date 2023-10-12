import string

letters = string.ascii_lowercase

message = input("Enter the message to be encrypted: ").lower()

plaintext = ""

for letter in message:
    if letter.isalpha():
        plaintext += letter

while True:
    try:
        fileName = input("Enter the name of the file that contains the key (exclude the .txt): ").strip() + ".txt"
        with open(fileName, "r") as f:
                key = f.read()
        break
    except:
         print("This file doesn't exist. Try again.\n")
    
ciphertext = ""

for i, letter in enumerate(plaintext):
    ciphertext += letters[(letters.index(letter) + letters.index(key[i])) % 26]

print("\nThe used portion of the key has been automatically deleted.\nEncrypted message: " + ciphertext)

key = key[len(plaintext):]

with open(fileName, "w") as f:
     f.write(key)