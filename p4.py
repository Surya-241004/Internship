# def add_numbers(a,b):
#     return a+b


# a,b=map(int,input().split())
# result=add_numbers(a,b)
# print(result)


# l=[1,"daf",3,4]
# print(l)
# print(*l)


# def mul(*args):
#     result=0
#     for num in args:
#         result+=num
#     return result
# print(mul(2,3,4,5))


# def student_info(**kwargs):
#     for key,value in kwargs.items():
#         print(key+":"+value)
# student_info(name="wasd",age="231")

# num=407 
# if num==1:
#     print(num,"is not a prime number")
# elif num>1:
#     #check the factors 
#     for i in range(2,num):
#         if(num%i)==0:
#             print(num,"is not a prime number")
#             print(i,"times",num//i,"is",num)
#             break
#     else:
#         print(num,"is a prime number")

# def is_armstrong(num):
#     original_num=num
#     armstrong_sum=0
#     num_digits=len(str(num))

#     while num>0:
#         digit=num%10
#         armstrong_sum+=digit**num_digits
#         num//=10
#     if original_num==armstrong_sum:
#         print("It is armstrong number")
#     else:
#         print("It is not")

# n=int(input("Enter the number: "))
# is_armstrong(n)



