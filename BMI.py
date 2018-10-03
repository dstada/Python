weight = int(input("What is your weight (kg)? "))
length = int(input("What is your length (cm)? "))
age = int(input("What is your age? "))

bmi = weight / ((length/100)*(length/100))
bmi_afg = round(bmi, 2)
print("Your BMI: {}".format(bmi_afg))

# Data per sex:
# too light | too heavy | obese
girls = [
    [6, 13.92, 17.34, 19.65],
    [7, 14.00, 17.75, 20.51],
    [8, 14.16, 18.35, 21.57],
    [9, 14.42, 19.07, 22.81],
    [10, 14.78, 19.86, 24.11],
    [11, 15.25, 20.74, 25.42],
    [12, 15.83, 21.68, 26.67],
    [13, 16.43, 22.58, 27.76],
    [14, 17.01, 23.34, 28.57],
    [15, 17.52, 23.94, 29.11],
    [16, 17.95, 24.37, 29.43],
]

boys = [
    [6, 14.03, 17.55, 19.78],
    [7, 14.06, 17.92, 20.63],
    [8, 14.20, 18.44, 21.60],
    [9, 14.41, 19.10, 22.77],
    [10, 14.69, 19.84, 24.00],
    [11, 15.03, 20.55, 25.10],
    [12, 15.47, 21.22, 26.02],
    [13, 15.98, 21.91, 26.84],
    [14, 16.54, 22.62, 27.63],
    [15, 17.13, 23.29, 28.30],
    [16, 17.70, 23.90, 28.88],
]


if age >= 17:
    if bmi <= 15.00:
        print("Very severely underweight!")
    elif bmi < 16.00:
        print("Severely underweight!")
    elif bmi < 18.50:
        print("Underweight!")
    elif bmi < 25.00:
        print("Normal (healthy weight)")
    elif bmi < 30.00:
        print("Obese Class I (Moderately obese!)")
    elif bmi < 35.00:
        print("Obese Class II (Severely obese!)")
    elif bmi < 40.00:
        print("Obese Class III (Very severely obese!)")
    else:
        print("Very severely obese!")
elif age < 6:
    print('You\'re too young for a reliable BMI.')
    print("Try it again in {} years.".format(6 - age))
else:   # From age 6 to 16 (different matrix)
    sex = input("Are you male or female (f/m)? ")
    if sex == "m":
        if bmi < boys[age-6][1]:
            print('Too light!')
        elif boys[age - 6][1] <= bmi < boys[age - 6][2]:
            print('Normal BMI!')
        elif boys[age - 6][2] <= bmi < boys[age - 6][3]:
            print('Too heavy!')
        elif bmi >= boys[age-6][3]:
            print('Obese!')
        else:
            print('Normal weight.')
    else:       # sex == "f"
        if bmi < girls[age-6][1]:
            print('Too light!')
        elif girls[age - 6][1] <= bmi < girls[age - 6][2]:
            print('Normal BMI!')
        elif girls[age - 6][2] <= bmi < girls[age - 6][3]:
            print('Too heavy!')
        elif bmi >= girls[age-6][3]:
            print('Obese!')
        else:
            print('Normal weight.')

