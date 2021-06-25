# for
# while

# 1
# for letter in "PYTHON":
#     print(letter)

# 2
colors = ["red", "blue", "yellow"]
# print(colors[0])
# print(colors[1])
# print(colors[-1])
for col in colors:
    print(col)
 
# 3 Range

# for z in range(0, 100, 5):
#     print(z)
#     print("----")


# Exersice:
water_level_now = 0
level_to_stop = 7
sourse = True

print("water_level_now: " + str(water_level_now))
while  sourse == True:
    water_level_now += 1
    # sourse = False
    if water_level_now == level_to_stop:
        sourse = False

print("water_level_now: " + str(water_level_now))
