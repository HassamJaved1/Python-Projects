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

pattern = ""
for i in range(0, 5):
    for j in range(0, 5):
        if i + 1 == j + 1:
            for times in range(0, i + 1):
                pattern = pattern + "*"
        print(pattern)
        pattern = ""


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


print(dt.datetime.now)


required_numbers = input(
    "Enter the numbers you want to add in the list and tuples separated by commas\n"
)

for index, value in enumerate(required_numbers):
    if index == 0:
        my_list = list(value)
    elif index % 2 == 0:
        my_list.append(value)

print(my_list)
print(tuple(my_list))


file_name = input("Enter the file name\n")

for index, character in enumerate(file_name):
    if character == ".":
        print(f"The file format is {file_name[index+1:]}")

color_list = ["Red", "Green", "White", "Black"]

print(color_list[0], color_list[-1])

exam_st_date = (11, 12, 2014)

# dd//MM/yyyy

date_list = list(exam_st_date)
print(f"{date_list[0]} / {date_list[1]} / {date_list[2]}")


value = input("enter value\n")

double_digits = value * 2
three_digits = value * 3

sum = int(value) + int(double_digits) + int(three_digits)

print(sum)


print(int.__doc__)
import calendar as c


# print(c.month(2024, 7))

date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

mylist1 = list(date1)
mylist2 = list(date2)

if mylist1[2] > mylist2[2]:
    resultdays = mylist1[2] - mylist2[2]


else:
    resultdays = mylist2[2] - mylist1[2]

number = 18
result = number - 17
if number > 17:
    result *= 2
    print(result)
else:
    print(result)


a = [1, 2, 3, 4, 5, 7, 4, 4, 9, 8]

count = 0

for number in a:
    if number == 4:
        count = count + 1

print(count)


vowels = ["a", "e", "i", "o", "u"]

char_to_check = input("Kindly enter the character you want to check\n")

(
    print("Yes the given character is a vowel")
    if char_to_check in vowels
    else print("No it is not a vowel")
)

key = "@"
histogram_pattern = [2, 4, 16, 8]

for everysinglePattern in histogram_pattern:
    print(key * everysinglePattern)
    print("\n")

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

dif = color_list_1.difference(color_list_2)
print(dif)


def duplicate(lst):
    try:
        lst2 = []
        seen = lst2
        for item in lst:
            if item in seen:
                return True
            seen.append(item)
        return False
    except:
        print("Error")


def number_from_user(lst):
    n = input("enter how many number you want to add in a list: ")
    for x in range(int(n)):
        number = input("enter number  to add in list: ")
        lst.append(5)


lst = []
number_from_user(lst)
if duplicate(lst):
    sum = 0
    print(sum)
else:
    adition = sum(lst)
    print(adition)
