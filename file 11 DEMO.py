dictionary = {
   1 : "A", 1 : "E", 1: "I", 1: "O",1: "U", 1: "L", 1: "N", 1: "S", 1: "T", 1 : "R",
   2 : "DG",
   3 : "BCMP",
   4 : "FHVWY",
   5 : "K",
   8 : "JX",
   10: "QZ"}
text = input().upper()
sum = 0
for letter in text:
   for point_value, letters in dictionary.items():
      if letter in letters:
         sum += point_value
print(sum)