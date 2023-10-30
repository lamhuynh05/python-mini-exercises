unit = input("What is your unit of choice (C/F): ")
temp = float(input("What is the temperature: "))

# f to c:
if unit == "F" or unit == "f": # ** when using operator restate the variable 
    temp = round((temp - 32) * 5/9, 2)
    print(f"The temperature in Celsius is: {temp} °C")

# c to f:
elif unit == "C" or unit == "c":
    temp = round((temp * 9)/5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp} °F")

else:
    print(f"{unit} is an invalid unit")