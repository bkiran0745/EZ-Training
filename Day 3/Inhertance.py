class animal:
    def animal_level_1():
        return "Im animal method"
class dog(animal):
    def dog_level_2():
        return "Im dog method, Im inherited form class animal"
class puppy(dog):
    def puppy_level_3():
        return "Im puppy method,im inherited form class dog"
obj1 = puppy
print(obj1.animal_level_1())
print(obj1.dog_level_2())
print(obj1.puppy_level_3())