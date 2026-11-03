
thislist = ["apple", "banana", "cherry"]


print("List :", thislist)

i=0 
while i<len(thislist):
     print(i, "  ", thislist[i])
     i+=1
     
print()


i=0
for x in  thislist:
    print(i, " " , x)
    i=i+1
    
    
print()
for i in range(len(thislist)):
    print(i, "  " , thislist[i])


print()

for i in  range(3):
    print( i, "  " , thislist[i])
  

  
print()

for i in  range(0,3,1):
    print( i, "  " , thislist[i])

    

print()  # reverse Order 

for i in  range(2,-1,-1):
    print( i, "  " , thislist[i])




