import hashlib

#This is a test to figure out how this works
def signup():
    
    email = input("Enter your email: ")
    passw = input("Enter password: ")
    conf_passw = input("Confirma password: ")

    if conf_passw == passw:
        hash1 = hashlib.sha256(conf_passw.encode())
        hash_hex = hash1.hexdigest()
        with open("mail.txt","w") as f:
            f.write(email + "\n")
            f.write(hash_hex)
        f.close
        print("Your registration is correct")
    else:
        print("Password is not the same \n")
def login():
    email = input("Enter your email: ")
    passw = input("Enter your password: ")
    
    with open("mail.txt", "r") as f:
        doc_email, doc_passw = f.read().split("\n")
    
    hash2 = hashlib.sha256(passw.encode())
    passw_hashed = hash2.hexdigest()
    
    if email == doc_email and passw_hashed == doc_passw:
        print("Login successful")
    else:
        print("Login failed")

while True: 
    print("Login system")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Option not available")
    
