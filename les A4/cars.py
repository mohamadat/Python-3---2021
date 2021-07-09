class Car:
	def __init__(self, model, color, nmr, accedint):
		self.model =  model
		self.color =  color
		self.nmr =  nmr
		self.accedint =  accedint


		self.health = 100
		self.speed = 0
		self.return_deg = 0
		self.state = False


	def start_engin(self):
		self.state = True


	def stop_engin(self):
		self.state = False



	def add_speed(self):
		if self.state == True:
			self.speed += 5
		else:
			print("Non Functional!")


	def stop(self):
		self.speed -= 5


	def Turn_right(self):
		self.return_deg += 5


	def Turn_left(self):
		self.return_deg -= 5


	def info(self):
		print("model is:", self.model );
		print("state is:", self.state );
		print("speed is:", self.speed );
		print("color is:", self.color );
		print("nmr is:", self.nmr );
		print("return degree is:", self.return_deg );




car = Car("tesla", "Black", "999", 0)
car.start_engin()
# car.start()
car.add_speed()
car.add_speed()
car.add_speed()

car.Turn_left()
car.Turn_left()

car.info()

# ------------------------
print("------------------------")

car2 = Car("Volvo", "red", "r4234-c", 6)

car2.info()



