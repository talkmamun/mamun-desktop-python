

#----------------- Tuple ------------------------------

tuple1 = 1, 2, "Three", "Three",  4, "OSTAD", "OSTAD", True, False 

print("\n\nTuple : ", tuple1, "\n", id(tuple1) ,"\n" )

#tuple1.append("Banana")  # AttributeError: 'tuple' object has no attribute 'append'

# tuple1.extend(["Banana2", "Mango2"])  // not allow 

tuple1 = tuple1 + ("Banana", "Mango")  

print("\n\nTuple : ", tuple1, "\n\n Len & ID :  ", len(tuple1), "  " , id(tuple1)   ,"\n\n" )

print("Count of OSTAD in Tuple : ", tuple1.count("OSTAD"), "\n\n")

tuple1 = 1, 2,  4 , 3
print("tuple1 : ", sorted(tuple1), "\n\n")
print("Maximum value in Tuple : ", max(tuple1),  sum(tuple1) , "\n\n")

