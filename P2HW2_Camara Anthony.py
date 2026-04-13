# Anthony Camara
# 4/12/2026
# P2HW2
# Grade Book pseudocode algorithm 
#
"""
Pseudocode (Algorithm) :
1. Create an empty list called module_grades
2. Ask the user to enter grade for Module 1
3. Ask the user to enter grade for Module 2
4. Ask the user to enter grade for Module 3
5. Ask the user to enter grade for Module 4
6. Ask the user to enter grade for Module 5
7. Ask the user to enter grade for Module 6
8. Convert all inputs to float values
9. Store all grades into the list module_grades
10. Find the lowest grade using min()
11. Find the highest grade using max()
12. Find the sum of grades using sum()
13. Calculate average by dividing sum by number of grades
14. Display results with proper formatting (2 decimal places for average)
"""
#
# Collect grades
module1 = float(input("Enter grade for Module 1 : "))
module2 = float(input("Enter grade for Module 2 : "))
module3 = float(input("Enter grade for Module 3 : "))
module4 = float(input("Enter grade for Module 4 : "))
module5 = float(input("Enter grade for Module 5 : "))
module6 = float(input("Enter grade for Module 6 : "))

# Store grades in a list

module_grades = [module1, module2, module3, module4, module5, module6]

# Calculations

lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Display results

print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest}")
print(f"{'Highest Grade:':<20}{highest}")
print(f"{'Sum of Grades:':<20}{total}")
print(f"{'Average:':<20}{average:.2f}")
print("--------------------------------")





