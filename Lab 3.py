# Programmers: Anthony, Aidan, Nicol
# Course: CS151 Dr. Rajeev
# Date: 9/30/21
# Lab Number: 3
# Inputs: Weight of the package and distance needed to travel
# Outputs: How much they will be charged

# Variables
weight = float(input("Input Weight of Package: "))
distance = float(input("Input Distance Package Will Travel: "))
# Invalid Weight and Distance Messages
if weight <= 0:
    print("Invalid Weight (Please input a weight that is 10 kg or above)")
if weight > 20:
    print("Invalid Weight (Maximum weight is 20 kg)")
if distance < 10:
    print("Invalid Distance (Minimum Distance is 10 miles)")
if distance > 3000:
    print("Invalid Distance (Maximum Distance is 3,000 miles)")
# Calculating Amount Charged
if weight <= 2:
    amountCharged = (distance/500) * 1.10
elif 2 < weight <= 6:
    amountCharged = (distance/500) * 2.20
elif 6 < weight <= 10:
    amountCharged = (distance/500) * 3.70
elif 10 < weight <= 20:
    amountCharged = (distance/500) * 4.80
print("Amount to be Charged: $" + str(amountCharged))
