import secrets
import string

letters = string.ascii_lowercase

while True:
    try:
        length = int(input("The key length should be at least as long as the length of the plaintext that will be used.\nKey length: "))
        if length < 1:
            raise ValueError()
        else:
            break

    except ValueError:
        print("That value wasn't valid. Make sure to enter a positive integer.\n")

key = ""

for letter in range (length):
    key += letters[secrets.randbelow(25)]

while True:
    try:
        fileName = input("Enter the name of the file that key should be written to (exclude the .txt): ").strip() + ".txt"
        with open(fileName, "w") as f:
            f.write(key)
        break
    except:
        print("This isn't a valid file name. Try again.\n")

print("\nThe key with length " + str(length), "has been written to", fileName)