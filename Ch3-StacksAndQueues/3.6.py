from datetime import datetime
import unittest

class Animal:
	def __init__(self):
		self.enter_date = None
		#self.name = name

	# def __str__(self):
	# 	return self.name

class Cat(Animal): pass
class Dog(Animal): pass

class AnimalShelter:
	def __init__(self):
		self.cats = []
		self.dogs = []

	def enqueue(self, animal):
		animal.enter_date = datetime.now()
		if type(animal) == Cat:
			self.cats.append(animal)
		elif type(animal) == Dog:
			self.dogs.append(animal)
		else:
			raise NameError("You must enqueue cats or dogs only!")

	def cat_dequeue(self):
		if not self.cats:
			raise IndexError("There are no cats")
		else:
			return self.cats.pop(0)

	def dog_dequeue(self):
		if not self.dogs:
			raise IndexError("There are no dogs")
		else:
			return self.dogs.pop(0)
        	#Every time we would write our own pop function(for a stack, for example) which
        	#would pop the element at the -1th position 

	def dequeueAny(self):
		if not self.cats and not self.dogs:
			raise NameError("Shelter is empty")
		elif not self.cats:
			return self.dog_dequeue()
		elif not self.dogs:
			return self.cat_dequeue()

		else:
			cat1 = self.cats[0]
			dog1 = self.dogs[0]

			if cat1.enter_date < dog1.enter_date:
				adopted = self.cat_dequeue()
			else:
				adopted = self.dog_dequeue()

		return adopted

#shelter = AnimalShelter()
# shelter.enqueue(Dog("Dog1"))
# shelter.enqueue(Cat("Cat1"))
# shelter.enqueue(Dog("Dog2"))
# shelter.enqueue(Cat("Cat2"))
# shelter.enqueue(Dog("Dog3"))
# shelter.enqueue(Cat("Cat3"))
class Test(unittest.TestCase):
     
    def test_enqueue(self):
        shelter = AnimalShelter()
        cat = Cat()
        dog = Dog()
        shelter.enqueue(cat)
        shelter.enqueue(dog)
        self.assertEqual(shelter.cats[0], cat)
        self.assertEqual(shelter.dogs[0], dog)
 
    def test_dequeue(self):
        shelter = AnimalShelter()
        cat1 = Cat()
        cat2 = Cat()
        dog1 = Dog()
        dog2 = Dog()
        shelter.enqueue(cat1)
        shelter.enqueue(cat2)
        shelter.enqueue(dog1)
        shelter.enqueue(dog2)
        self.assertEqual(shelter.cat_dequeue(), cat1)
        self.assertEqual(shelter.cat_dequeue(), cat2)
        self.assertEqual(shelter.dog_dequeue(), dog1)
        self.assertEqual(shelter.dog_dequeue(), dog2)
 
    def test_dequeue_any(self):
        shelter = AnimalShelter()
        cat1 = Cat()
        cat2 = Cat()
        dog1 = Dog()
        dog2 = Dog()
        shelter.enqueue(cat1)
        shelter.enqueue(dog1)
        shelter.enqueue(cat2)
        shelter.enqueue(dog2)
        self.assertEqual(shelter.dequeueAny(), cat1)
        self.assertEqual(shelter.dequeueAny(), dog1)
        self.assertEqual(shelter.dequeueAny(), cat2)
        self.assertEqual(shelter.dequeueAny(), dog2)
         
if __name__ == '__main__':
    unittest.main()












