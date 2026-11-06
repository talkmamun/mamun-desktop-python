

#-----if 


#print("Enter yours Marks : ")
#Student_mark=int(input())

print("\n\n") 


Student_mark = int(input("Enter your marks (0-100): "))


if    Student_mark <=32:
    print("Grade point : F " ) 
elif    Student_mark  <= 39:
      print("Grade point : D " )
elif    Student_mark  <= 49:
      print("Grade point : C " )

elif    Student_mark  <= 59:
      print("Grade point : B  3.0 " )
elif    Student_mark  <= 69 :
      print("Grade point : A -  3.5" )

elif    Student_mark  <= 79 :
      print("Grade point : A  4.0" )
else: 
      print("Grade point : A+   5.0" )

print("") 