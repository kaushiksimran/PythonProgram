height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height**2)

if bmi < 18.5:
    print("you are underweight")
elif bmi < 24.9:
    print("you have a normal weight")
elif bmi < 29.9:
    print("you are overweight")
elif bmi < 34.9:
    print("you are an obese")
else:
    print("you are clinically obese")
