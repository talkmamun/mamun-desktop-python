#print 

print()

fruits = ["apple", "banana", "cherry","PQR","xyz"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("\nEnd\n\n==============================================\n")


for x in fruits:
  if x == "banana":
    continue
  print(x)

print("\n")

for x in range(6):
  print(x)