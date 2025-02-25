class Vehicle:
   def __init__(self,brand,model,year):
      self.brand = brand
      self.model = model
      self.year = year
   def start_engine(self):
      raise NotImplementedError("The message is unique for every vehicle")

class Car(Vehicle):
   def __init__(self,brand,model,year,num_doors):
      Vehicle.__init__(self,brand, model, year)
      self.num_doors = num_doors
   def start_engine(self):
      return f"The Car named {self.brand} is activated.It's been created in {self.year} and the model is \
           {self.model}. Btw, the number of the doors is {self.num_doors}"
    
class Motorcycle(Vehicle):
   def __init__(self,brand,model,year,has_sidecar):
      Vehicle.__init__(self,brand,model,year)
      self.has_sidecar = has_sidecar
   def start_engine(self):
      if self.has_sidecar == 1:
         return f"The Motorcycle named {self.brand} is activated.It's been created in {self.year} and  \
            the model is {self.model}.Btw, it has a sidecar"
      else:
         return f"The Motorcycle named {self.brand} is activated.It's been created in {self.year} and \ 
         the model is {self.model}.Btw, it has a sidecar"
My_Car = Car("BMW","black",2010, 4)
My_Moto = Motorcycle("Kawasaki","white",2018,0)
print(My_Car.start_engine())
print(My_Moto.start_engine())

         