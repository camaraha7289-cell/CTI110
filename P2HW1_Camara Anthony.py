# Anthony Camara
# 4/10/2026
# P2HW1
# Basic Travel Budget Calculator (Formatted Version)


print('This program calculates and displays Travel expenses')


# 1. Ask user to enter their budget
budget = float(input("Enter your total travel budget: $"))


# 2. Ask user to enter travel destination
destination = input("Enter your travel destination: ")


# 3. Ask user for amount they will spend on gas
gas = float(input("Enter amount you will spend on gas: $"))


# 4. Ask user for amount they will spend on accommodation
accommodation = float(input("Approcimately how much will you need for accomodation: $"))


# 5. Ask user for amount they will spend on food
food = float(input("Last, enter amount you will spend on food: $"))


# 6. Add expenses
total_expenses = gas + accommodation + food


# 7. Subtract expenses from budget
remaining_balance = budget - total_expenses


# 8. Display results (formatted)
print("\n------------ Travel Budget Summary ------------")

# Formatting width
label_width = 20
value_width = 15

print(f"{'Destination:':<{label_width}}{destination:>{value_width}}")
print(f"{'Total Budget:':<{label_width}}{'$' + format(budget, '.2f'):>{value_width}}")
print(f"{'Gas:':<{label_width}}{'$' + format(gas, '.2f'):>{value_width}}")
print(f"{'Accommodation:':<{label_width}}{'$' + format(accommodation, '.2f'):>{value_width}}")
print(f"{'Food:':<{label_width}}{'$' + format(food, '.2f'):>{value_width}}")
print(f"{'Total Expenses:':<{label_width}}{'$' + format(total_expenses, '.2f'):>{value_width}}")
print(f"{'Remaining Balance:':<{label_width}}{'$' + format(remaining_balance, '.2f'):>{value_width}}")
print("\n------------------------------------------------")
print(f"{'Remaining Balance:':<{label_width}}${remaining_balance:>{value_width - 1}.2f}")

