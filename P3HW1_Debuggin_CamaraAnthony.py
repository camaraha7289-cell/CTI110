# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.


# Enter grades for six modules
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
# determine letter grade for average


print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest}")
print(f"{'Highest Grade:':<20}{highest}")
print(f"{'Sum of Grades:':<20}{total}")
print(f"{'Average:':<20}{average:.2f}")
print("--------------------------------")
if average >= 90:
    print("Your Grade is: A")
elif average >= 80:
    print("Your Grade is: B")
elif average >= 70:
    print("Your Grade is: C")
elif average >= 60:
    print("Your Grade is: D")
else:
    print("Your Grade is: F")





