

print("Loop Example")

#Loop 

i = 0
while i<10:
    if i%2==0:
        print(i)
    i += 1

#-----------------------------------------------------

print("\nList Example")

list1 = [1, 2, "Three", 4, "OSTAD", True, False ]
print("list1 : " , list1)
list1.append("Python")
print("\nAfter appending 'Python':", list1)

list1[1] = "Two"
print( "\nlist1 replace 2 = Two : " , list1)

#list1.remove("three")  // Error: ValueError: list.remove(x): x not in list

list1.remove("Three")
print("Removed(Three):",list1)


print("\n")