#BMI CALCULATOR IN PYTHON
height = float(input("Enter the  height in cm: "))
weight = float(input("Enter the weight in kg: "))
BMI = weight / (height/100)**2
if BMI <=18.5:
    print("\n you are underweight.")
elif BMI <=24.9:
    print("\n you are healthy.")
elif BMI <=29.9:
    print("\n you are overweight.")
else:
    print("\n you are obese.")
print("\n YOUR BODY MASS INDEX(BMI) IS: ", BMI)