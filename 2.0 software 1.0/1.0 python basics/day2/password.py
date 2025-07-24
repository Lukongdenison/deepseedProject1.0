# password=input("Enter your password: ")
# lower_case=password.islower()
# upper_case=password.isupper()
# numeric=password.isdigit()

# if lower_case and upper_case and numeric:
#     print(" this Password is strong")
# else:
#     print("please enter strong password")



l = False
u = False
D = False

password = input("Enter your password: ")
for letter in password:
    if letter.islower():
        l = True
    elif letter.isupper():
        u = True
    elif letter.isdigit():
        D = True

if l and u and D:
    print(" strong password")
else:
    print("waek passwrd")
    