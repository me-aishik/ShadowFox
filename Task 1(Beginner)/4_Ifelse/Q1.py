h = float(input("Enter your height in meters: "))
w = int(input("Enter your weight in kg: "))
bmi = w / (h ** 2)
if bmi >= 30:
    print("You are obese.")
elif 25 <= bmi < 30:
    print("You are overweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
else:
    print("You are underweight.")   