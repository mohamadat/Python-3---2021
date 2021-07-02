board = ([False,False,True],
[False,True,False],
[True,False,False])


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

    