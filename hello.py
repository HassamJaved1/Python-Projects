import datetime as dt


thislist = ["apple", "banana", "cherry", "banana"]

for item in thislist:
    if item == "banana":
        thislist.remove("banana")


print(thislist)
thislist = ["apple", "banana", "cherry", "banana"]

for items in thislist:
    if items in "banana":
        thislist.remove("banana")

print(thislist)

print(dt.datetime.now())


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello():
        print("Hello, my name is ")


Rafay = Student("Rafay", 21)
Student.sayHello()
print(Rafay.name)
print(Rafay.age)
