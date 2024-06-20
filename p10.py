"Polymorphism"
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
# class Cow(Animal):
#     def speak(self):
#         return "Moo"
# def make_animal_speak(animal):
#     print(animal.speak())
# god=Dog()
# cat=Cat()
# cow=Cow()
# make_animal_speak(god)
# make_animal_speak(cat)
# make_animal_speak(cow)


# class Complexnumber:
#     def __init__(self,real,imaginary):
#         self.real=real
#         self.imaginary=imaginary
#     def __sub__(self,b):
#         return f"{self.real-b.real}+{self.imaginary-b.imaginary}i"
# c1=Complexnumber(2,2)
# c2=Complexnumber(1,2)
# print(c1-c2)

"*->Encapsulation*"

"Overloading:"
# class Demo:
#     def add(self,*args):
#         total=0
#         for i in args:
#             total=total+i
#         return total
# d= Demo()
# print(d.add(2,3))    
# print(d.add(10,20))

