#database{"key:","value"}, username and password = ""

def login(database, username, password):
  
# if the user and the password matches in the database, grant access, else deny access
  if username in database and database[username]== password:
    print("HEY YOU>>> Welcome back, admin!")
    return username 
  elif username in database and  database[username] != password:
    print("Really Invalid password,check your brain dummy.")
    return ""
  else:
    print( "WHATT...User not found, please register")
    return ""
   
def register (database, username):
  if username in database:
    print("Username allready registerd... dummy!!")
    return""
  else:
    print(f"Username {username} is registed andd you cannot change it. ")
    return"" 
