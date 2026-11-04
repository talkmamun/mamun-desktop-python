

#-----------------------------------------------------

print("\nList Example")

list1 = [1, 2, "Three", 4, "OSTAD", True, False ]
print("list1 : " , list1)
list1.append("Python")
print("\nAfter appending 'Python' : ", list1)

list1[1] = "Two" # Replace 2 with Two
print( "\nList1 replace 2 = Two : " , list1)

#list1.remove("three")  // Error: ValueError: list.remove(x): x not in list

if "Three" in list1:
   # print("Yes, 'Three' is in the fruits list1")
   list1.remove("Three")
   print("Removed(Three):",list1)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print("\nthislist : ", thislist)


print("List range ")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print("thislist : " , thislist, "\n")
print("thislist[2:5] : " , thislist[2:5])
print("thislist[:4] : " , thislist[:4])
print("thislist[2:] : " , thislist[2:])
print("thislist[-4:-1] : " , thislist[-4:-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:5] = ["blackcurrant", "watermelon"]

print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2 ,"kiwi" )

thislist.extend(["watermelon", "grapes","papaya"])
thislist.append(["watermelon2", "grapes2","papaya2"])

print("After APPEND & EXTEND:", thislist)



print("\n")