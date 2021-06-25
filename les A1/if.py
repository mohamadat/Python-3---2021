# lab:
# fname = input("Enter your first name please...")
# lname = input("Enter your lname please...")
# age = input("Enter your age please...") 
# (18 - 65)
# email = input("Enter your email please...")
#  (@)

# request is valid
# request is not valid


# print("Welcome " + fname)


# conditional statments
# if len(fname) < 20:
#     print("thats a good name")
#     print("...App End...")
# else:
#     print("thats a bad name")

# print("...App End...")

# (18 - 65)
leeftijd = 70

# if leeftijd < 65:
#     if leeftijd > 18:
#         print("valid")

# if leeftijd < 65 and leeftijd > 18:
#     print("valid")

if 18 < leeftijd < 65:
    print("valid")
elif leeftijd > 18:
    print("All respect")

else:
    print("not valid")



# if leeftijd > 18 or leeftijd == 18:
#     print("adult")

answer = False;

if leeftijd == 18:
    answer = True;

# answer = leeftijd == 18 ? True : False
answer = True if leeftijd == 18 else False

print("answer: ",answer)

# falsy values
# ""
# 0
# []

if leeftijd:
    print("true");
else:
    print("false")

# logical operators:
# and or not
# True False

