#Variables and datatypes
'''x=int(input("enter the number: ")) 
print(type(x))
print(x)'''

#Arithmetic
'''a=int(input("enter the number a: "))
b=int(input("enter the number b: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)'''

#Comparision
'''x=int(input("enter the number x: "))
y=int(input("enter the number y: "))
print(x==y)
print(x>y)
print(x<y)
print(x!=y)'''

#logical
'''x=int(input("enter the number x: "))
if(x%2==0 and x%3==0):
    print("Divisible by 2 and 3")
else:
    print(" Not Divisble by 2 and 3")'''

#Program to print the length of the string and convert it to Uppercase
'''s=input("Enter the String")
print(len(s))
print(s.upper())'''


#condition statements
'''x=int(input("enter the number x: "))
if(x>0):
    print("Positive")
elif(x<0):
    print("negative")
else:
    print("zero")'''        

#Looping from 1 to 10
'''for i in range(1,11): 
    print(i)'''

#Lists
'''l=["Apple","Lemon","Banana"]
print(l)
l.append("Orange")
print(l)'''

#Tuples (cant change values)
'''l=("hello","10",True)
print(l)
l.append("20")#eRROR'''

#Dictionary
'''d={
    "a":"BMW",
    "b":"Benz"
    }
print(d)
x=d.keys() 
print(x)
y=d["a"]
print(y)
d["c"]="Porsche" #print element
print(d)
del d["b"] #delete
print(d)'''
