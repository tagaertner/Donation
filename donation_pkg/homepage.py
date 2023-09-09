#task 2 creat homepage
def show_homepage():
  
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login    | 2.    Register         |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations  |")
    print("------------------------------------------")
    print("|               5. Exit                   |")
    print("------------------------------------------")

def show_donations(donations):
  print("\n -- All Donations --")
  if not donations:
    print("No donations so far..")
  else:
    for donation in donations:
      print(donation)
      

show_homepage()