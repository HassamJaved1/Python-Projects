import datetime as dt
import re

import numpy as np


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


pattern = r"ABCD"
text = "This is a test string with ABCD in it."
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")


my_file = open("hello.txt", "w")

my_file.write("Hello World!")

my_file.close()

my_file = open("hello.txt", "r")

print(my_file.read())


arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for number in nums:
            if val == number:
                # pop the value
                nums.pop(val)
                count = count + 1

        for i in range(count):
            nums.append("_")

        return nums


myObj = Solution()

print(myObj.removeElement([3, 2, 2, 3], 3))
