FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit=(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return fahrenheit
tempreture=float(input("Enter the temperature to convert: "))
scale=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
def main():
    if scale =="C":
        print(f"{tempreture}°C is {convert_to_fahrenheit(tempreture)}°F")
    elif scale =="F":
        print(f"{tempreture}°F is {convert_to_celsius(tempreture)}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")
    
main()

