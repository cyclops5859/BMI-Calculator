# Created by Cyclops!
print ("Welcome here you can calculate your Body Mass Index")

weight=float(input("Enter your weight in kilograms : "))
height=float(input("Enter your height in centimeters : "))

bmi=weight/((height/100)*(height/100))

print("Your Body Mass Index (BMI) is : ",round(bmi,2))
