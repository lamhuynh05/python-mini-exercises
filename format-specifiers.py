price1 = 3.14159
price2 = -987.65
price3 = 12.34

#decimal points
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

#space
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

#add zeros
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

# adjust
print(f"Price 1 is ${price1:<10}") #adjust to left 
print(f"Price 2 is ${price2:>10}") # right 
print(f"Price 3 is ${price3:^10}") # center

# display positive sign:
print(f"Price 1 is ${price1:+}") 
print(f"Price 2 is ${price2:+}") 
print(f"Price 3 is ${price3:+}") 

#separate thousand place:
price4 = 3000.14159
price5 = -9870.65
price6 = 1200.34

print(f"Price 4 is ${price4:,}") 
print(f"Price 5 is ${price5:,}") 
print(f"Price 6 is ${price6:,}")

print(f"Price 4 is ${price4:,.2f}") 
print(f"Price 5 is ${price5:,.2f}") 
print(f"Price 6 is ${price6:,.2f}")
