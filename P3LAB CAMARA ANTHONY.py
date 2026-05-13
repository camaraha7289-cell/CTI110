# Anthony Camara
# 4/26/2026
# P3LAB
# Calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money
# Get Value from User


change = float(input("Enter an amount of money float: $"))
#Converting the value to an integer
if change == 0.00:
    print("No Change")
change = round(change * 100)

#Determine how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quaters = change // 25 
change = change - (num_quaters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change



if num_dollars > 0 :
    if num_dollars == 1:
        print(f"{num_dollars} Dollars")
    else:
        print(f"{num_dollars} Dollar")

if num_quaters > 0 :
    if num_quaters == 1:
        print(f"{num_quaters} Quarter")
    else:
        print(f"{num_quaters} Quaters")

if num_dimes > 0 :
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickels > 0 :
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")

if num_pennies > 0 :
    if num_pennies == 1:
        print(f"{num_pennies} Pennie")
    else:
        print(f"{num_pennies} Pennies")
























