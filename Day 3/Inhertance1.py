#inheritance
#type of inheritence
#multilevel inheritence
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

#multeple inhertance
class father:
    def parent_method():
        return "is the fsther"
class mother:
    def parent_method1():
        return "is the mother"
class child(father,mother):
    def child_method():
        return "is the child"
obj1=child
print(obj1.parent_method())
print(obj1.parent_method1())


#type of inheritence

#single inheritence
class parent:
    def parent_method():
        return "In parent method"
class child(parent):
    def child_method():
        return "In child method"
obj1=child
print(obj1.child_method())
print(obj1.parent_method())