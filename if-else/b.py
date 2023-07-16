import math

input_marks = float(input("Enter your marks: "))

print(type(input_marks))

final_marks = (round(input_marks))

if(final_marks >= 90):
    print("Excellent!! YOu got Grade A")
elif(final_marks<90 & final_marks>=60):
    print("Good!! You got Grade B")
elif(final_marks<60 & final_marks>=35):
    print("You got Grade C")
else:
    print("You got Grade D")
