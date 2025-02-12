def my_coords():
   x = int(input("Введите координату X"))
   y = int(input("Введите координату Y"))
   if x >= 1 and y >= 1:
      print('I quarter, четверть')
   elif x >= 1 and y <= -1:
      print("IV quarter, четверть")
   elif x <= -1 and y >= 1:
      print("II quarter, четверть")
   elif x <= -1 and y <= -1 :
      print("III quarter, четверть")
   else :
      print("Эта точка лежит на координатной прямой")
my_coords()

            
   

