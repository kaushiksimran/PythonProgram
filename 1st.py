from PIL import Image

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2 #dividing by 100 to convert it from cm to m.
print(f"You BMI is {BMI}")
if BMI <= 18.4:
    print("You are underweight.")
    img = Image.open('D:\graphicsDesigning\BMI.jpg')
    img.show()
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

