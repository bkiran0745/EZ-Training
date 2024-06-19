class Animal:
    def speck():
        return "Animal is speaking"
class Dog(Animal):
    def speck():
        return "Dog is barking"
class Cat(Animal):
    def speck():
        return "Cat is memoe"
animal = Animal
dog = Dog
cat = Cat
print(animal.speck())
print(dog.speck())
print(cat.speck())