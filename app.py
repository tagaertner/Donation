from donation_pkg.homepage import show_homepage

database = {"admin:","password123"}
donations =[]
authorized_user = ""

def show_homepage():
  if authorized_user == "":
    print("You must be logged in to donate.\n")
  else: 
    print(f"Logged in as: {authorized_user}\n")

def prompt_option ():

#task 3 Handle user input
  while True:
    option = input(f"Choose an option:\n")
    
    if option == "1":
      print("TODO: write login functioantly")
    elif option == "2":
      print("TODO: Write Register Functionaltiy")
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