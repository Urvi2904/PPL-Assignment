#abstraction, encapsulation, public and private access specifiers
import operator

#--------------------------------------CAT-----------------------------------
class Cat() :					#encapsulation
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "green"
		self.__furcolour = "brown"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def setFurcolour(self, colour) :
		self.__furcolour = colour
	def speak(self) :
		print("Meow")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		if x >= y :
			print(self.__name, "walked to", self.__position)
		else :
			print(self.__name, "climbed to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
		pass
	def eat(self, food) :			#abstraction
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a cat with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		self.setFurcolour("white")
		print(self.__name + " is a cat with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("mouse")
		self.move(4,3)

#---------------------------------------------COW--------------------------------
class Cow() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "black"
		self.__coatcolour = "white"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getCoatcolour(self) :
		return self.__coatcolour
	def setCoatcolour(self, colour) :
		self.__coatcolour = colour
	def speak(self) :
		print("Moo")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		if x >= y :
			print(self.__name, "walked to", self.__position)
		else :
			print(self.__name, "climbed to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
                pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()


	def main(self) :
		print(self.__name + " is a cow with " + self.getCoatcolour() + " coat and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setCoatcolour("brown")
		print(self.__name + " is a cow with " + self.getCoatcolour() + " coat and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("grass")
		self.move(2,0)

#---------------------------------------CROCODILE-------------------------------------
class Crocodile() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 4
		self.__eyes = 2
		self.__nose = 1
		self.__eyecolour = "yellow"
		self.__scalecolour = "green"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getScalecolour(self) :
		return self.__scalecolour
	def speak(self) :
		print("Grunt")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		if x >= y :
			print(self.__name, "swam to", self.__position)
		else :
			print(self.__name, "climbed to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
		pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a crocodile with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("black")
		print(self.__name + " is a crocodile with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("fish")
		self.move(4, 3)

#------------------------------------------CROW---------------------------------------
class Crow() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 2
		self.__eyes = 2
		self.__beak = 1
		self.__eyecolour = "black"
		self.__feathercolour = "black"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getBeak(self) :
		return self.__beak
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFeathercolour(self) :
		return self.__feathercolour
	def setFeathercolour(self, colour) :
		self.__feathercolour = colour
	def speak(self) :
		print("Caw")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		print(self.__name, "flew to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
                pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a crow with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFeathercolour("black")
		print(self.__name + " is a crow with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("rat")
		self.move(4,4)

#---------------------------------------------DOG------------------------------------
class Dog() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "black"
		self.__furcolour = "brown"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def setFurcolour(self, colour) :
		self.__furcolour = colour
	def speak(self) :
		print("Woof")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		if x >= y :
			print(self.__name, "walked to", self.__position)
		else :
			print(self.__name, "climbed to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
                pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a dog with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("golden")
		print(self.__name + " is a dog with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("chicken")
		self.move(3,5)

#--------------------------------------DUCK--------------------------------------------
class Duck() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 2
		self.__eyes = 2
		self.__beak = 1
		self.__eyecolour = "black"
		self.__feathercolour = "white"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getBeak(self) :
		return self.__beak
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFeathercolour(self) :
		return self.__feathercolour
	def setFeathercolour(self, colour) :
		self.__feathercolour = colour
	def speak(self) :
		print("Quack")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		if x >= y :
			print(self.__name, "waddled to", self.__position)
		else :
			print(self.__name, "flew to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
                pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a duck with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("red")
		self.setFeathercolour("brown")
		print(self.__name + " is a duck with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("corn")
		self.move(2,4)

#-----------------------------------------------HORSE---------------------------------
class Horse() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "black"
		self.__furcolour = "brown"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def setFurcolour(self, colour) :
		self.__furcolour = colour
	def speak(self) :
		print("Neigh")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		if x >= y :
			print(self.__name, "galloped to", self.__position)
		else :
			print(self.__name, "climbed to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
		pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a horse with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("white")
		print(self.__name + " is a horse with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("apple")
		self.move(1,4)

#-------------------------------------------LION-----------------------------------
class Lion() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "green"
		self.__furcolour = "golden"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def speak(self) :
		print("Roar")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		if x >= y :
			print(self.__name, "walked to", self.__position)
		else :
			print(self.__name, "climbed to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
                pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a lion with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		print(self.__name + " is a lion with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("meat")
		self.move(2,6)

#--------------------------------------------PARROT--------------------------------
class Parrot() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__legs = 2
		self.__eyes = 2
		self.__beak = 1
		self.__eyecolour = "black"
		self.__feathercolour = "green"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getBeak(self) :
		return self.__beak
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFeathercolour(self) :
		return self.__feathercolour
	def setFeathercolour(self, colour) :
		self.__feathercolour = colour
	def speak(self) :
		print("Squawk")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		print(self.__name, "flew to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
                pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a parrot with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFeathercolour("red")
		print(self.__name + " is a parrot with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("chilli")
		self.move(0,7)

#------------------------------------------SNAKE--------------------------------------------
class Snake() :
	def __init__(self, name) :
		print("-----------------------------------------------------------------")
		self.__eyes = 2
		self.__nose = 1
		self.__eyecolour = "green"
		self.__scalecolour = "brown"
		self.__position = (0, 0)
		self.__name = name
	def getEyes(self) :
		return self.__eyes
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getScalecolour(self) :
		return self.__scalecolour
	def setScalecolour(self, colour) :
		self.__scalecolour = colour
	def speak(self) :
		print("Hiss")
	def __locomotion(self, x, y) :
		self.__position = tuple(map(operator.add, self.__position, (x, y)))
		print(self.__name, "slithered to", self.__position)
	def move(self, x, y) :
		self.__locomotion(x, y)
	def __digest(self) :
		pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()

	def main(self) :
		print(self.__name + " is a snake with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		self.setScalecolour("green")
		print(self.__name + " is a snake with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("mouse")
		self.move(2,1)

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
