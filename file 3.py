def check_string_brackets():
   b = input("Введите скобочки")
   if len(b)%2 == 1:
      print("False")
   elif b[0] == ")":
      print("False")
   elif b[0] == b[-1]:
      print("No")
   else:
      print("OK")
check_string_brackets()
      