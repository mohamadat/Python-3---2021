# Filter the Emails for some word[s]

from text import *

# Answer: filter("ji jiof js  sdoifj sd fds ")
# The word "x" has been found 3 times.

# first step define variables
# Sec step wordk-alogrithm. functions, methos, behaviour .. etc



def filter(email, x, lang):
	count = email.count(x)
	if lang == "en":
		print("The word \" ", x ," \" has been found ", count ," times")
	else:
		print("Het woord \" ", x ," \" is ", count ," voorgekomen!")


# Answer:
# email = "gregergerg  secret gf secret fsd ds apple f vgregergerg  secret sd "
x = "and"
filter(text, x, "en")








# Steps
# 1- input


# 2- process


# 3- output [print]