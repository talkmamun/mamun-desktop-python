
# Name : AL MAMUN, Batch-14, 01614071297, talkmamun@gmail.com 
# Assignment 2

# Student Grade Calculator

name = input("\n\nEnter student name: ")  

marks_math    = int(input("Enter Math marks: "))
marks_english = int(input("Enter English marks: "))
marks_python  = int(input("Enter Python marks: "))



if (marks_math    < 0 or marks_math    > 100 or 
    marks_english < 0 or marks_english > 100 or 
    marks_python  < 0 or marks_python  > 100):
   
        print("\nInvalid marks. Please enter a value between 0 and 100.\n\n")
else:
        average_marks = (marks_math + marks_english + marks_python) / 3

        if average_marks >= 80: 
            grade = "A+"
        elif average_marks >= 70:
            grade = "A"
        elif average_marks >= 60:
            grade = "A-"
        elif average_marks >= 50:
            grade = "B"
        elif average_marks >= 40:
            grade = "C"
        else:
            grade = "F"



        print(f"\nStudent Name: {name}")
        print(f"Average Marks: {average_marks:.2f}")
        print(f"Final Grade: {grade}\n\n")

