from donation_pkg.homepage import show_homepage
from donation_pkg.user import login, register, donate

database = {"admin":"password123",}
donations =[]
authorized_user = ""

def show_homepage():
  if authorized_user == "":
    print("You must be logged in to donate.\n")
  else: 
    print(f"Logged in as: {authorized_user}\n")

def prompt_option ():
  global authorized_user
#task 3 Handle user input
  while True:
    option = input(f"Choose an option:\n")
  

    if option == "1":
      #task 4 login: user login, connected to user.py
      #bonus 1: username case-insensitive
      username = input("Please enter your user name\n").lower()
      password = input("Please enter your password\n")
      
      authorized_user = login(database, username, password)
      
      if authorized_user:
        print("login successful")
      else:
        print("User not found. Pleas register")
        #task 5 registration add user to database and create password, connected to user.py
        # bonus 1: 
    elif option == "2":      
        username = input("Enter your user name NOW\n").lower()
        password = input("Enter your password NOW\n")
        authorized_user = register(database, username)
        if authorized_user != "":
          database.add_user(username, password)
    elif option == "3":
      print("TODO: Write Donate functonality")
    elif option == "4":
      print("TODO: write Show Donations Functionailty")
    elif option == "5":
      print("Goodbye..end program")
      break
    
if __name__ == "__main__":
  
  show_homepage()
  prompt_option()