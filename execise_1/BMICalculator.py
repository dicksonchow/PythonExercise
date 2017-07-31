# -*- coding: utf-8 -*-
import sys

# lbs to kg
lbs_in_kg = 0.45359237

try:
    # User input
    height = float(raw_input('Please enter your height: '))
    weight_unit =  raw_input('Please enter the unit for the weight value (lbs/kg): ')
    weight = float(raw_input('Please enter your weight: '))
    print '\n'

    # Check the height and the weight
    if height < 0:
        print 'Height cannot be less than zero'
        sys.exit(1)

    if weight < 0:
        print 'Weight cannot be less than zero'
        sys.exit(1)

    # Check whether the user has entered a valid weight unit
    if weight_unit not in ['lbs', 'kg']:
        print 'Invalid weight unit'
        sys.exit(1)

    # Transform the height to m if the user enters the value in cm
    height = height if height < 2.5 else height / 100

    if weight_unit == 'lbs':
        weight *= lbs_in_kg

    # Calculate the BMI value
    bmi = weight / (height * height)
    print 'Your BMI value is: ' + str(bmi) + '\n'

    if bmi < 18.5:
        print 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        print 'Normal or Healthy Weight'
    elif 25.0 <= bmi <= 29.9:
        print 'Overweight'
    else:
        print 'Obese'

except ValueError as e:
    print 'Error - Invalid input: ' + str(e)
    sys.exit(1)

except ZeroDivisionError as e:
    print 'Error - Height cannot be zero'
    sys.exit(1)
