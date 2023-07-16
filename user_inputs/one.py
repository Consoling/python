name = input("What's your name? : ")

age = int(input("Umm okay and What's your age by the way ? : ")) # casted to int from string

height = float(input("And your height ? : ")) # casted to float from string

age += 1

print("Marvellous !! Creating your profile...")
print("Hello, " + name + "!")
print("You are " + str(age) + " years old!") # casted to string from int
print("You are " + str(height) + " cm tall!") # casted to string from float
print("Congrats!! Your profile got created successfully")