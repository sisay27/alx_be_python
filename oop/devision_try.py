num1 = int(input("inter the first number: "))
num2 = int(input("inter the second number: "))
try:
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("error!")
