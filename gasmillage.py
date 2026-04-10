name = input('Please enter your name: ')
total_distance = int(input('Please enter your total distance for today'))
total_fuel_cost = int(input('Please enter your total fuel cost for today'))
total_gallons_purchased = int(input('Please enter your total gallons purchased for today'))
total_gallons_of_fuel_used = int(input('Please enter your total gallons of fuel used for the week'))
parking_fee_per_day = int(input('Please enter your parking fee per day'))
toll_per_day = int(input('Please enter your toll per day'))


total_miles_per_day = total_distance/2
cost_per_gallon  = total_fuel_cost/total_gallons_purchased
average_miles_per_gallon = total_miles_per_day/total_gallons_of_fuel_used
total_cost_of_driving_to_work_per_day = (total_miles_per_day/average_miles_per_gallon*total_fuel_cost)*parking_fee_per_day*toll_per_day


print('Hi'+name+'Your Total miles driven per day is', total_miles_per_day)
print('Your Total cost of driving to work everyday is', total_cost_of_driving_to_work_per_day)
print('Consider car pooling if this cost is too much for you to bear')

# BMI VALUES
# Underweight: less than 18.5
# Normal: between 18.5 and 24.9
# Overweight: between 25 and 29.9
# Obese: 30 or greater

print('BMI VALUES FOR YOUR OWN USE')
print('Underweight: less than 18.5')
print('Overweight: between 25 and 29.9')
print('Obese: 30 or greater')




weight_in_pounds = float(input('Please enter your weight in pounds'))
height = int(input('Please enter your height'))
Bmi = weight_in_pounds*703/(height**2)


print(weight_in_pounds)
print('Your BMI is', Bmi)


think = 'helllo'

print(think)
if Bmi < 18.5:
    print(' You are Underweight')
elif Bmi >= 25 and Bmi <= 29.9:
     print(' You are Overweight')
elif Bmi >= 30:
    print(' You are Obese')




