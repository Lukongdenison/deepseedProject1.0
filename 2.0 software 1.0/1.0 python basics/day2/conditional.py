# # # age= input("Enter your age: ")
# # # if age>= 18:
# # #      print("You can vote.")
# # # else:      
# # #      print("wait for next elections")


# # # age=input("please enter your age")
# # # if int(age) >= 16:
# # #     print("You can play basketball.")

# # # else:
# # #     print("You need to be at least 16 to play basketball.")

# # #excercise
# # marks=input("enter your marks:")
# # if int(marks) >= 80:
# #     print("You got an A")
# # elif int(marks) > 70 and int(marks) <= 80:
# #     print("You got a B+")
# # elif int(marks) > 60 and int(marks) <= 70:
# #     print("You got a C")
# # elif int(marks) > 50 and int(marks) <= 60:
# #     print("You got a D  ")
# # else:
# #     print("you have failed")

# # # This code checks the user's grade and prints the corresponding letter grade based on the input.

# #simple calculator
# first_number=float(input("Enter First number:"))
# second_number=float(input("enter second number"))
# operator=input("Enter operator")
# result=0
# if operator=="+":
#     result=first_number+second_number
#     print(f"result is : {result}")
# elif operator=="-":
#     result=first_number-second_number
#     print(f"result is : {result}")
# elif operator=="*":
#     result=first_number*second_number
#     print(f"result is : {result}")
# elif operator=="?":
#     if second_number!=0:
#         result=first_number/second_number
#     print(f"result is ;{result}")
# else:
#     print(f"division by 0 is not allowed")


#leap year problem
year=int(input("enter the year:"))
if year%4 !=0:
    if year%100!=0:
        if year%400==0:
            print("its a leap year")

    print(" not a leap year")
