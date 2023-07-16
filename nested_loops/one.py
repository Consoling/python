rows =  int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")


for i in range (rows):
    for j in range (cols):
        print(symbol,end="")
    print()