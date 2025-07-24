# # #concartenation and interpolation in python
# # first_name = "John"
# # last_name = "Doe"
# # #concatenation
# # full_name=first_name+last_name
# # print(f"My name is {full_name}")
# # #interpolation

# # #length of a string
# # message= "hello world"
# # print( len(message))


# # #f-stri
# # print(f "hello, {name}! you are {age} years old.")
# # print(f "your score is {score:1f}%")
# # #fomat() method
# # print("hello, {}! you are {} years old.".format(name,age))
# # #%formatting (older style)
# # print("hello, %s! you are %d years old." % (name, age))


# #string examples
# email= "user@example.com"
# if "@" in email and "." in email:
#     username = email.split("@")[0]
#     domain = email.split("@")[1]
#     print(f"Username: {username }")
#     print(f"Domain: {domain}") 
# else:
#     print("Invalid email format")
# # # string manipulation and formatting in Python
# # Text analyzer
# text = "The quick brown fox jumps over the lazy dog"
# print(f"Text: {text}")
# print(f"Length: {len(text)} characters")
# print(f"Words: {len(text.split())} words")
# print(f"Uppercase: {text.upper()}")
# print(f"Title case: {text.title()}")
# print(f"Contains 'fox': {'fox' in text}")

message= "greetings"
message_lower=message.lower()
message_upper=message.upper()
print( f"uppercase is {message_upper}")
print(f"lowercase is {message_lower}")


