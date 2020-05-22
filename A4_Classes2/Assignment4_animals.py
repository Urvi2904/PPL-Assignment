#virtual funcns, abstract classes, base/derived class, interfaces, polymorphism ,modularity, hierarchy
import abc
from abc import ABC, abstractmethod
import operator

#----------------------------------------ANIMAL----------------------------------------

class Animal(ABC) :		#abstract class -- interfaces can have only empty methods, not applicable here.
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
	def getNose(self) :
		pass
	def getFurcolour(self) :
		pass
	def setFurcolour(self, colour) :
		pass
	def getBeak(self) :
		pass
	def getFeathercolour(self) :
		pass
	def setFeathercolour(self, colour) :
		pass
	def getScalecolour(self) :
		pass
	def setScalecolour(self, colour) :
		pass
	def move(self, x, y) :
		pass
	def speak(self) :
		pass
	def digest(self) :				#virtual functions
		pass
	def eat(self, food) :
		print(self.name + " ate the " + food)
		self.digest()

#-----------------------------------------------------MAMMAL---------------------------------

class Mammal(Animal) :
	def __init__(self, name) :
		self.legs = 4
		self.ears = 2
		self.nose = 1
		self.furcolour = "brown"
		Animal.__init__(self, name)
		print(self.name + " is a mammal.")
	def getNose(self) :
		return self.nose
	def getFurcolour(self) :
		return self.furcolour
	def setFurcolour(self, colour) :
		self.furcolour = colour

#----------------------------------------------------BIRD----------------------------------

class Bird(Animal) :
	def __init__(self, name) :
		self.legs = 2
		self.beak = 1
		self.feathercolour = "black"
		Animal.__init__(self, name)
		print(self.name + " is a bird.")
	def getBeak(self) :
		return self.beak
	def getFeathercolour(self) :
		return self.feathercolour
	def setFeathercolour(self, colour) :
		self.feathercolour = colour

#-----------------------------------REPTILE------------------------------------

class Reptile(Animal) :
	def __init__(self, name) :
		self.legs = 4
		self.nose = 1
		self.scalecolour = "green"
		Animal.__init__(self, name)
		print(self.name + " is a reptile.")
	def getNose(self) :
		return self.nose
	def getScalecolour(self) :
		return self.scalecolour
	def setScalecolour(self, colour) :
		self.scalecolour = colour


#--------------------------------------CAT-----------------------------------
class Cat(Mammal) :
	def __init__(self, name) :
		Mammal.__init__(self, name)
	def speak(self) :
		print("Meow")
	def move(self, x, y) :
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
class Cow(Mammal) :
	def __init__(self, name) :
		Mammal.__init__(self, name)
	def speak(self) :
		print("Moo")
	def move(self, x, y) :
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
class Crocodile(Reptile) :
	def __init__(self, name) :
		Reptile.__init__(self, name)
	def speak(self) :
		print("Grunt")
	def move(self, x, y) :
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
class Crow(Bird) :
	def __init__(self, name) :
		Bird.__init__(self, name)
	def speak(self) :
		print("Caw")
	def move(self, x, y) :
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
class Dog(Mammal) :
	def __init__(self, name) :
		Mammal.__init__(self, name)
	def speak(self) :
		print("Woof")
	def move(self, x, y) :
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
class Duck(Bird) :
	def __init__(self, name) :
		Bird.__init__(self, name)
	def speak(self) :
		print("Quack")
	def move(self, x, y) :
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
class Horse(Mammal) :
	def __init__(self, name) :
		Mammal.__init__(self, name)
	def speak(self) :
		print("Neigh")
	def move(self, x, y) :
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
class Lion(Mammal) :
	def __init__(self, name) :
		Mammal.__init__(self, name)
	def speak(self) :
		print("Roar")
	def move(self, x, y) :
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
class Parrot(Bird) :
	def __init__(self, name) :
		Bird.__init__(self, name)
	def speak(self) :
		print("Squawk")
	def move(self, x, y) :
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
class Snake(Reptile) :
	def __init__(self, name) :
		Reptile.__init__(self, name)
	def speak(self) :
		print("Hiss")
	def move(self, x, y) :
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
	a1 = Cat("Jerry")
	a1.main()

	a2 = Cow("Nandi")
	a2.main()

	a3 = Crocodile("Koko")
	a3.main()

	a4 = Crow("Kalia")
	a4.main()

	a5 = Dog("Snoopy")
	a5.main()

	a6 = Duck("Donald")
	a6.main()

	a7 = Horse("Philip")
	a7.main()

	a8 = Lion("Leo")
	a8.main()

	a9 = Parrot("Mithu")
	a9.main()

	a10 = Snake("Skeeter")
	a10.main()
