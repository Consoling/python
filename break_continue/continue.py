phone_number = "123-345-567"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")
print()