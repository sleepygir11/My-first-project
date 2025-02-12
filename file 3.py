def check_string_brackets():
   i = 1
   b = input("Введите скобочки")
   while i != len(b):
      if b[0] == ")":
         print("False")
         break
      elif b[i] == b[-i-1]:
         print("False")
         break
      else: 
         print("True")
         break
   i += 1

check_string_brackets()
      