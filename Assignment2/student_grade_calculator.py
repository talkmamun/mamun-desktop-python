
# Name : AL MAMUN, Batch-14, 01614071297, talkmamun@gmail.com 
# Assignment 2

# Grade Calculator


def value_input(data):
    
  while True:
    try:
        marks = int(input(f"Enter {data} marks:: "))
        if marks < 0 or marks > 100:
            print("Wrong Entry! Enter marks between 0 and 100.")
        else:
            return marks
    except ValueError:
        print("Invalid Input! Please enter a numeric value.")
    

#======================================================================
name = input("\n\nEnter student name: ")  

print()
marks_math    =  value_input("math")
marks_english =  value_input("English") 
marks_python  =  value_input("Python") 


if (marks_math < 0 or marks_math > 100 or 
    marks_english < 0 or marks_english > 100 or 
    marks_python < 0 or marks_python > 100 ):
   
        print("\nInvalid marks. Please enter a value between 0 and 100.\n\n")
else:
        average_marks = (marks_math + marks_english + marks_python) / 3

        if average_marks >= 80: 
            grade = "A+"
        elif average_marks >= 70:
            grade = "A"
        elif average_marks >= 60:
            grade = "B"
        elif average_marks >= 50:
            grade = "C"
        else:
            grade = "F"



        print(f"\nStudent Name: {name}")
        print(f"Total Marks : { marks_math + marks_english + marks_python }")
        print(f"Average  : {average_marks:.2f}")
        print(f"Final Grade: {grade}\n\n")
