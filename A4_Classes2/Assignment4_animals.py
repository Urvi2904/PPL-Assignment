import operator

#----------------------------------------ANIMAL----------------------------------------

class animal(object) :
	def __init__(self, name) :
		self.position = (0, 0)
		self.name = name
		self.eyes = 2
		self.eyecolour = "black"
		print("-----------------------------------------------------------------")
	def getLegs(self) :
		return self.legs
	def getEyes(self) :
		return self.eyes
	def getEars(self) :
		return self.ears
	def getEyecolour(self) :
		return self.eyecolour
	def setEyecolour(self, colour) :
		self.eyecolour = colour
	def move(self, x, y) :
		self.locomotion(x, y)
	def digest(self) :
		pass
	def eat(self, food) :
		print(self.name + " ate the " + food)
		self.digest()

#-----------------------------------------------------MAMMAL---------------------------------

class mammal(animal) :
	def __init__(self, name) :
		self.legs = 4
		self.ears = 2
		self.nose = 1
		self.furcolour = "brown"
		animal.__init__(self, name)
		print(self.name + " is a mammal.")
	def getNose(self) :
		return self.nose
	def getFurcolour(self) :
		return self.furcolour
	def setFurcolour(self, colour) :
		self.furcolour = colour

#----------------------------------------------------BIRD----------------------------------

class bird(animal) :
	def __init__(self, name) :
		self.legs = 2
		self.beak = 1
		self.feathercolour = "black"
		animal.__init__(self, name)
		print(self.name + " is a bird.")
	def getBeak(self) :
		return self.beak
	def getFeathercolour(self) :
		return self.feathercolour
	def setFeathercolour(self, colour) :
		self.feathercolour = colour

#-----------------------------------REPTILE------------------------------------

class reptile(animal) :
	def __init__(self, name) :
		self.legs = 4
		self.nose = 1
		self.scalecolour = "green"
		animal.__init__(self, name)
		print(self.name + " is a reptile.")
	def getNose(self) :
		return self.nose
	def getScalecolour(self) :
		return self.scalecolour
	def setScalecolour(self, colour) :
		self.scalecolour = colour


#--------------------------------------CAT-----------------------------------
class cat(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Meow")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		if x >= y :
			print(self.name, "walked to", self.position)
		else :
			print(self.name, "climbed to", self.position)

	def main(self) :
		print(self.name + " is a cat with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		self.setFurcolour("white")
		print(self.name + " is a cat with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("mouse")
		self.move(4, 3)

#---------------------------------------------COW--------------------------------
class cow(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Moo")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		if x >= y :
			print(self.name, "walked to", self.position)
		else :
			print(self.name, "climbed to", self.position)

	def main(self) :
		print(self.name + " is a cow with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("brown")
		print(self.name + " is a cow with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("grass")
		self.move(2, 0)

#---------------------------------------CROCODILE-------------------------------------
class crocodile(reptile) :
	def __init__(self, name) :
		reptile.__init__(self, name)
	def speak(self) :
		print("Grunt")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		if x >= y :
			print(self.name, "swam to", self.position)
		else :
			print(self.name, "climbed to", self.position)

	def main(self) :
		print(self.name + " is a crocodile with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("black")
		self.setScalecolour("brown")
		print(self.name + " is a crocodile with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("fish")
		self.move(4, 3)

#------------------------------------------CROW---------------------------------------
class crow(bird) :
	def __init__(self, name) :
		bird.__init__(self, name)
	def speak(self) :
		print("Caw")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		print(self.name, "flew to", self.position)

	def main(self) :
		print(self.name + " is a crow with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFeathercolour("black")
		print(self.name + " is a crow with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("rat")
		self.move(4,4)

#---------------------------------------------DOG------------------------------------
class dog(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Woof")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		if x >= y :
			print(self.name, "walked to", self.position)
		else :
			print(self.name, "climbed to", self.position)

	def main(self) :
		print(self.name + " is a dog with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("golden")
		print(self.name + " is a dog with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("chicken")
		self.move(3, 5)

#--------------------------------------DUCK--------------------------------------------
class duck(bird) :
	def __init__(self, name) :
		bird.__init__(self, name)
	def speak(self) :
		print("Quack")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		if x >= y :
			print(self.name, "waddled to", self.position)
		else :
			print(self.name, "flew to", self.position)

	def main(self) :
		print(self.name + " is a duck with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("red")
		self.setFeathercolour("brown")
		print(self.name + " is a duck with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("corn")
		self.move(2, 4)

#-----------------------------------------------HORSE---------------------------------
class horse(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Neigh")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		if x >= y :
			print(self.name, "galloped to", self.position)
		else :
			print(self.name, "climbed to", self.position)

	def main(self) :
		print(self.name + " is a horse with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("white")
		print(self.name + " is a horse with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("apple")
		self.move(1, 4)

#-------------------------------------------LION-----------------------------------
class lion(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Roar")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		if x >= y :
			print(self.name, "walked to", self.position)
		else :
			print(self.name, "climbed to", self.position)

	def main(self) :
		print(self.name + " is a lion with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		print(self.name + " is a lion with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("meat")
		self.move(2, 6)

#--------------------------------------------PARROT--------------------------------
class parrot(bird) :
	def __init__(self, name) :
		bird.__init__(self, name)
	def speak(self) :
		print("Squawk")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		print(self.name, "flew to", self.position)

	def main(self) :
		print(self.name + " is a parrot with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFeathercolour("red")
		print(self.name + " is a parrot with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("chilli")
		self.move(0, 7)

#------------------------------------------SNAKE--------------------------------------------
class snake(reptile) :
	def __init__(self, name) :
		reptile.__init__(self, name)
	def speak(self) :
		print("Hiss")
	def locomotion(self, x, y) :
		self.position = tuple(map(operator.add, self.position, (x, y)))
		print(self.name, "slithered to", self.position)

	def main(self) :
		print(self.name + " is a snake with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		self.setScalecolour("green")
		self.setScalecolour("yellow")
		print(self.name + " is a snake with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("mouse")
		self.move(2,1)

#-----------------------------------------------------------------------------------------------

if __name__ == "__main__" :
	a1 = cat("Jerry")
	a1.main()

	a2 = cow("Nandi")
	a2.main()

	a3 = crocodile("Koko")
	a3.main()

	a4 = crow("Kalia")
	a4.main()

	a5 = dog("Snoopy")
	a5.main()

	a6 = duck("Donald")
	a6.main()

	a7 = horse("Philip")
	a7.main()

	a8 = lion("Leo")
	a8.main()

	a9 = parrot("Mithu")
	a9.main()

	a10 = snake("Skeeter")
	a10.main()
