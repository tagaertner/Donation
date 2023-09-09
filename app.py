from donation_pkg.homepage import show_homepage, show_donations
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
        if username in database:
          print("Username already exist. Please choose a different username")
        else:
          authorized_user = register(database, username)
          if authorized_user != "":
            database[username] = password
            print("Registration sucessfull, you can now login")
          #taks 6 donation functionality,user cannot donate if not loggin in, 
    elif option == "3":
      if authorized_user == "":
        print("You are not logged in.")
      else:
        donation_string = donate(authorized_user)
        donations.append(donation_string)
    elif option == "4":
        donation = show_donations(donations)
        if not donations:
          print("Currently, there are no donations.")
        else:
          for donation in donations:
            print(donation)
            
    elif option == "5":
      print("Goodbye..end program")
      break
    
if __name__ == "__main__":
  
  show_homepage()
  prompt_option()