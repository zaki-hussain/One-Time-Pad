import secrets
import string

letters = string.ascii_lowercase

while True:
    try:
        length = int(input("\nThe key length should be at least as long as the length of the plaintext that will be "
                           "used.\nKey length: "))
        if length < 1:
            raise ValueError()
        else:
            break

    except ValueError:
        print("That value wasn't valid. Make sure to enter a positive integer.")

key = ""

for letter in range(length):
    key += letters[secrets.randbelow(25)]

while True:
    try:
        fileName = input(
            "\nEnter the name of the file that key should be written to (exclude the .txt): ").strip() + ".txt"
        with open(fileName, "w") as f:
            f.write(key)
        break
    except OSError:
        print("This isn't a valid file name. Try again.")

print("\nThe key with length " + str(length), "has been written to", fileName + "\n")
