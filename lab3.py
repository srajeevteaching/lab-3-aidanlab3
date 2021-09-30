# Programmers: Aidan S, Nicol, Anthony
# Course: CS151, Dr. Rajeev
# Date: 9/30/21
# Lab Number: 3
# Program Inputs: Weight of package and distance
# Program Outputs: How much it costs to ship

# Submission One submission per team including all member names.

# Weight of package Rate per 500 miles (or fraction) 2 kg or less $1.10 Over 2 kg but not more than 6 kg $2.20 Over
# 6 kg but not more than 10 kg $3.70 Over 10 kg but not more than 20 kg $4.80 Write a program that asks for the weight
# of the package and the distance it is to be shipped, and then displays the charges.

# Inputs/variables
weight = float(input("Input the weight of the package in kg "))
distance = float(input("Input the distance for the package in miles "))
price = 0

# Input Validation: Do not accept values of 0 or less for the weight of the package. Do not accept weights of more than
# 20 kg (this is the maximum weight the company will ship). Do not accept distances of less than 10 miles or more than
# 3,000 miles. These are the company’s minimum and maximum shipping distances.

# calculation
if weight <= 0:
    print("Package is too light")
elif weight <= 2:
    price = 1.10
elif weight <= 6:
    price = 2.20
elif weight <= 10:
    price = 3.70
elif weight <= 20:
    price = 4.80
elif weight > 20:
    print("Package is too heavy")

if distance < 10:
    print("Distance is too short")
elif distance <= 500:
    print("The price is", price * 1)
elif distance <= 1000:
    print("The price is", price * 2)
elif distance <= 1500:
    print("The price is", price * 3)
elif distance <= 2000:
    print("The price is", price * 4)
elif distance <= 2500:
    print("The price is", price * 5)
elif distance <= 3000:
    print("The price is", price * 6)
elif distance > 3000:
    print("Distance is too far")

