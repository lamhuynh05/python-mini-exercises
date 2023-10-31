name = "Lam"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
# add padding to the words by 10
print("Hello, my name is {:<10}. Nice to meet you".format(name))
# {:10} same as {:<10}
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))
# center


number1 = 3.14159
print("The number pi is {:.2f}".format(number1))

number2 = 1000
print("The number is {:.3f}".format(number2))
print("The number is {:,}".format(number2)) # add comma to thousanth place
print("The number is {:b}".format(number2)) # binary format
print("The number is {:o}".format(number2)) # octal
print("The number is {:x}".format(number2)) # hexidecimal
print("The number is {:E}".format(number2)) # scientific notation 