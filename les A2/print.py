# print("My pation is", end=" ")
# print("ICT")

# print("Next line")

# range(0, 5454)

# for

# Draw with X and O:

board = [[False,False,True],
[False,True,False],
[True,False,False]]


for item in board:
    line = ""
    for subitem in item:
        if subitem == True:
        #    line = line + "o"
             line +=  "o    "
        else:
             line +=  "X    "
    print(line);
    # print(item)


# if True:
#     print("o", end="")