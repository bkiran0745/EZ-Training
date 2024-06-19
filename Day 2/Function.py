#postional argument
def sumOfNumbers(a,b):
    return a + b
c = sumOfNumbers(23,34)
print(c)   

#key word argument
def mySelf(name,age):
    print("My name is",name,"and I am",age,"years old.")
    return None
mySelf("Rahul",age=25)

#default argument
def goodMorning(name,age=25):
    print("Good morning",name,"you are",age,"years old.")
    return None
goodMorning("siri",222)