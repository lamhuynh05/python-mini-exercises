body_weight = float(input("What is your body weight in kg?: "))
unit_of_choice = input("What would you like to convert your weight to (lbs/stone): ")

if unit_of_choice == "lbs":
    weight_lbs = body_weight * 2.2
    unit = "lbs"
    print(f"Your weight is {round(weight_lbs, 2)} {unit}")

elif unit_of_choice == "stone":
    weight_stone = body_weight * 0.16
    unit = "stones"
    print(f"Your weight is {round(weight_stone, 2)} {unit}")

else:
    print(f"{unit_of_choice} is not a valid unit")