number = int (input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    result = i* number
    print(f"{number} * {i} = {result}")
    i= i+1