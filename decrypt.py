import string

letters = string.ascii_lowercase

while True:
    ciphertext = input("Enter the message to be decrypted: ").lower()
    if ciphertext.isalpha:
        break
    else:
        print("Make sure you only include alphabet letters. Try again.\n")

while True:
    try:
        fileName = input("Enter the name of the file that contains the key (exclude the .txt): ").strip() + ".txt"
        with open(fileName, "r") as f:
                key = f.read()
        break
    except:
         print("This file doesn't exist. Try again.\n")

plaintext = ""

for i, letter in enumerate(ciphertext):
     plaintext += letters[(letters.index(letter) - letters.index(key[i])) % 26]
    
print("\nThe used portion of the key has been automatically deleted.\nDecrypted message: " + plaintext)

key = key[len(ciphertext):]

with open(fileName, "w") as f:
     f.write(key)