while True:
    while True:
        try:
            operation = int(input("Enter 1 to generate a key.\nEnter 2 to encrypt a message.\nPress 3 to decrypt a message.\nPress 4 to exit.\n"))
            if 1 <= operation <= 4:
                break
            else:
                raise ValueError()
        except ValueError:
            print("Make sure you enter a number between 1 and 4. Try again.\n")

    if operation == 1:
        import createKey
    
    elif operation == 2:
        import encrypt
    
    elif operation == 3:
        import decrypt
    
    elif operation == 4:
        break