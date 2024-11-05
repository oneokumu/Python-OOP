class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

# Function demonstrating polymorphism
def animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
cat = Cat()
dog = Dog()

# Demonstrate polymorphism by passing instances of Cat and Dog to the animal_sound function
animal_sound(cat)
animal_sound(dog)
