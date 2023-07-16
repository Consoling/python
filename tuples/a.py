student = ('John', 'Smith', 'js1234', 'male', 18)

print(student.count('John'))
print(student.index("male"))

for x in student:
    print(x)

if 18 in student:
    print("Yes, 18 is in the student tuple")