#pip install bmi-python

# from bmi import Bmi
# #Bmi(182,72)
# e = Bmi.calculate_bmi(80, 1.80)
# print(e)


Height = float(input("Please enter your height in inches: "))
Weight = float(input("Please enter your weight in pound: "))
    
if Height <= 0 or Weight <= 0:
    print("Your input must not be zero or less.")
    
else:
            # Calculate BMI
    BMIIndex = round(Weight / (Height * Height) * 703, 2)

            # Print the output
    print("Your Body Mass Index is: ", BMIIndex)

    if BMIIndex < 18.5:
        print("Underweight.")
    elif BMIIndex <= 24.9:
        print("Normal.")
    elif BMIIndex <= 29.9:
        print("Overweight.")
    else:
        print("Obese.")
     