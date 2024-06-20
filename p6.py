"Reverse Number"
# num=1234
# reversed_number=0
# while num!=0:
#     digit=num%10
#     reversed_number=reversed_number*10+digit
#     num//=10
# print(f"reversed number is {reversed_number}")


# num=int(input("enter the num:"))
# if num<0:
#     print('Enter a positive number')
# else:
#     sum=0
#     while(num>0):
#         sum+=num
#         num -=1
#     print("the total sum is",sum)

"Class"
# class Bike:
#     def __init__(self,name,cc):
#      self.name=name
#      self.cc=cc
#     def sound(self):
#      print(f"{self.name} is loud")
# Duke=Bike("RC390",390)
# RE=Bike("Classic350",350)
# TVS=Bike("Moto",900)
# print(Duke.name)
# print(RE.name)
# print(TVS.name)
# TVS.sound()

# b=input("Enter the bike:")
# if b=="Duke":
#   Duke.Type()
# elif b=="RE":
#   RE.Type()
# else:
#   TVS.Type

"Inheritance"
# class human:  
#     def __init__(self,hobby,food):
#         self.hobby=hobby
#         self.food=food
#     def display(self):
#         print(f"he plays {self.hobby} and he likes {self.food}")
# class human2(human):
#     def __init__(self,hobby,food,language):
#         super().__init__(hobby,food)
#         self.fav_language=language
#     def display(self):
#         super().display() 
#         print(f"language he speaks {self.fav_language}")
# a1=input("Enter your Hobby:")
# a2=input("Enter your food:")
# a3=input("Enter your language:")
# user= human2(a1,a2,a3)
# user.display()
        