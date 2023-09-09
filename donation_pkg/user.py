#database{"key:","value"}, username and password = ""

def login(database, username, password):
  
# taks 4:if the user and the password matches in the database, grant access, else deny access
  if username in database and database[username]== password:
    print("HEY YOU>>> Welcome back, admin!")
    return username 
  elif username in database and  database[username] != password:
    print("Really Invalid password,check your brain dummy.")
    return ""
  else:
    print( "WHATT...User not found, please register")
    return ""

#task 5 defined funtion and executed logic to prevent duplicate login info 
def register(database, username):
  if username in database:
    print("Username allready registerd... dummy!!")
    return""
  else:
    print(f"Username {username} is registed and you cannot change it. ")
    return username
  
#task6: define function and execute logic and set vaule that will show how much is donated
def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = f"{username} donated ${donation_amt}"
    print(f"Thank you for your donation, {username}!")
    return donation_string
   
     
