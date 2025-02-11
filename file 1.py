
class Pasq:
   def __init__(self, passwordy):
      self.passwordy = passwordy
   def check_password(self):
      dadada = input("Password?")
      if dadada == self.passwordy:
         print("Yes! Welcome.")
         True
      else:
         False
b = input()
paq = Pasq(b)
a = 0
while a != 2:
   if paq.check_password() is True:
      a=0
   else:
      paq.check_password()
      a+=1

      