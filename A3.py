h = float(input("Height in meters: "))
w = float(input("weight in kg: "))

BMI = w / (h**2)
print("BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI > 18.4 and BMI <= 24.9:
    print("You are normal")
elif BMI > 25 and BMI <= 30:
    print("You are over weight")
else:
    print("You are Obese")