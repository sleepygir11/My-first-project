def check_string_brackets(input_string):

   balance = 0
   for char in input_string:
      if char == '(':
         balance += 1
      elif char == ")":
         balance -= 1
      if balance < 0 :
         print("NO")
         return
   if balance == 0:
      print("YES")
   else:
      print("NO")  
check_string_brackets("")
check_string_brackets("((()()))")
check_string_brackets("()()()()")
check_string_brackets("()(()(((()(())()))))")
check_string_brackets(")()()")