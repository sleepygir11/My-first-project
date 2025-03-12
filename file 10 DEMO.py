masha=[]
sasha = {}
def to_dict(lst):
   for listik in lst:
      masha.append(listik)
   a = 0
   while a != len(masha):
      sasha.update({masha[a]: masha[a]})
      a += 1
   print(sasha)
to_dict(input().split(" "))