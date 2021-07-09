# - procidural programming
# - object oriented programming

# event driven, .. etc


class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age



	def bark(self):
		print("Hoi!!")

	def barkEnglish(self):
		print("Hello!!")

	def die(self):
		self.age = 0
		print("the age has been reseted")


	def add_years(self, years_to_add):
		self.age += years_to_add
		print(years_to_add ," has been added")







dog = Dog("koko", 20)
dog2 = Dog("soso", 430)
dog3 = Dog("kkk", 99)


dog.bark()
dog.barkEnglish()

print(dog.name)

x = "cdc"
y = 5
z = x + y