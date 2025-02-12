
def ask_password():
   a = 0
   password = input()
   b = input()
   if b != password:
      while a != 2:
         input("Password?")
         a += 1
   else:
      print("Great job!")
ask_password()
   