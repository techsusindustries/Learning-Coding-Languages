# Basic account system using conditionals
adminuser = "admin"
adminpass = "password"

guestuser = "guest"
guestpass = "guestpassword"

user = input("Enter your username: ")
passwrd = input("Enter your password: ")

if (user == adminuser and passwrd == adminpass):
    print("Welcome, admin! You have full access.")
elif (user == guestuser and passwrd == guestpass):
    print("Welcome, guest! You have limited access.")
else:
    print("Access denied. Invalid username or password.")