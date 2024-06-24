thislist = ["apple", "banana", "cherry", "banana", "kiwi"]

for item in thislist:
    if item == 'banana':
        thislist.remove("banana")

print(thislist)
