# Anthony Camara
# 4/5/2026
# P1HW1
# Travel Budget Calculater


print('This program calculates and displays travel expenses')


budget = float(input("Enter budget: $"))
destination = input("Enter your travel destination: ")
fuel = float(input("Enter amount you will spend on fuel: $"))
accommodation = float(input("Enter amount you will spend on accommodation: $"))
food = float(input("Enter amount you will spend on food: $"))
total_expenses = fuel + accommodation + food
remaining_balance = budget - total_expenses
print("\n--- Travel Expenses ---")
print("Destination:", destination)
print("Initial Budget: $", budget)
print("Fuel: $", fuel)
print("Accommodation: $", accommodation)
print("Food: $", food)
print("Total Expenses: $", total_expenses)
print("Remaining Balance: $", remaining_balance)

