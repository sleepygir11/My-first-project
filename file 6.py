class Animal:
   def __init__(self,name):
      self.name = name
   def speak(self):
      raise NotImplementedError("Subject must speak in their own way")

class Cat(Animal):
   def speak(self):
      return f"{self.name} says meow"
class Dog(Animal):
   def speak(self):
      return f'{self.name} says woof woof'
   
my_cat = Cat("Nigiro the Cat")
my_dog = Dog("Murata the Dog")
print(my_cat.speak())
print(my_dog.speak())
