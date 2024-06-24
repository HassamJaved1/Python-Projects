thislist = ["apple", "banana", "cherry", "banana"]

for item in thislist:
    if item == 'banana':
        thislist.remove("banana")

print(thislist)
thislist = ["apple", "banana", "cherry", "banana"]

for items in thislist:
  if items in 'banana':
    thislist.remove("banana")

print(thislist)
