# # # # # # # # # # # # #looping
# # # # # # # # # # # # #starting point
# # # # # # # # # # # # #condition
# # # # # # # # # # # # #increment/decrement

# # # # # # # # # # # # names=["will", "kate", "deni", "dgdgdg mbom", "ytty mbom"]
# # # # # # # # # # # # #to print the names
# # # # # # # # # # # # print(names[0])
# # # # # # # # # # # # print(names[1])
# # # # # # # # # # # # print(names[2])
# # # # # # # # # # # # print(names[3])
# # # # # # # # # # # # print(names[4])
# # # # # # # # # # # # #or 
# # # # # # # # # # # # for name in names:
# # # # # # # # # # # #     print(name)
# # # # # # # # # # # #     if name.endswith("mbom"):
# # # # # # # # # # # #         print(f"we have caught you:{name}")
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print(f"welcome to the team {name}")

# # # # # # # # # # # names=["will", "kate", "deni", "dgdgdg mbom", "ytty mbom"]
# # # # # # # # # # # #to print the names
# # # # # # # # # # # print(names[0])
# # # # # # # # # # # print(names[1])
# # # # # # # # # # # print(names[2])
# # # # # # # # # # # print(names[3])
# # # # # # # # # # # print(names[4])
# # # # # # # # # # # count=1
# # # # # # # # # # # for name in names:
# # # # # # # # # # #     print(f"{count}. {name}")
# # # # # # # # # # #     count = count + 1

# # # # # # # # # # #range function
# # # # # # # # # # for i in range(7):
# # # # # # # # # #     print(i)
# # # # # # # # # for i in range(1,11):
# # # # # # # # #     print(i)
# # # # # # # # for i in range(1,13,2):
# # # # # # # #     print(i)

# # # # # # # #countdown
# # # # # # # for i in range(10,0,-1):
# # # # # # #     print(f"countdown: {i}")
# # # # # # #     print("Happy New Year!")

# # # # # # #while loops
# # # # # # while True:
# # # # # #     print(f"madness")

# # # # # count=1
# # # # # while count <=5:
# # # # #     print(f"count is:{count}")
# # # # #     count += 1  # Increment the count by 1
 

# # # # #user input loop
# # # # user_input=""
# # # # while user_input!="quit":
# # # #     user_input=input("enter 'quit' to exit: ")
# # # #     if user_input!="quit":
# # # #         print(f"You entered: {user_input}")

# # # #break
# # # print("find the first even numbers")
# # # for number in range(1, 10):
# # #     if number %2== 0:
# # #         print (f"found even number: {number}")
# # #         break
# # #     print(f"{number} is odd")
 

# # #skip to next iteration
# # print("\nPrinting only odd numbers:")
# # for number in range(1, 10):
# #     if number % 2 == 0:
# #         continue  # Skip even numbers
# #     print(f"Odd number: {number}")


# # Multiplication table
# print("Multiplication Table:")
# for i in range(1, 4):  # Rows
#     for j in range(1, 4):  # Columns
#         result = i * j
#         print(f"{i} x {j} = {result}")
#     print()  # Empty line after each row



   #pattern printing
print("triangle pattern:")
for row in range(1,6):
    for star in range (row):
        print("*", end="")
    print()