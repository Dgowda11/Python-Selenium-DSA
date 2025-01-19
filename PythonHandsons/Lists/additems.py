
thislist = ["apple", "banana", "cherry"]
thislist.append("Orange")
print(thislist)
#
# thislist.insert(1,"Watermelon")
tropical  = ("Mango","Strwberry","BUtterfruit")
thislist.extend(tropical)   #Use extend method to add items for another list to current one
print(thislist)
thislist.remove("Strwberry")
print(thislist)
thislist.pop() # Not specifying the index it will remove the last element
print(thislist)
del thislist[3]
print(thislist)
# del thislist
thislist.clear()
print(thislist)
