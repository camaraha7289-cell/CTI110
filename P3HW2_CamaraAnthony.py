#Anthony Camara-Hernandez
#4/10/2026
#Salary Calculator
#request emplyee into

# request emplyee information
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime
if hours > 40:
    # Calcualte overtime pay
    overtime_hours = hours - 40 
    # Calucalte over pay 
    overtime_pay = overtime_hours * (rate * 1.5)
    # Calualte salary for regular hours
    regular_pay = 40 * rate
    #calculate Gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate 
    gross_pay = regular_pay 

# Display results 
print("-----------------------")
print("Emplyee Name:", name)
print(f'{"Hours worked:":15}{"Pay Rate:":12}{"OverTime Pay":<15}{"Regulary Pay":<15}{"Gross Pay":<12}')
print("--------------------------------------")
print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')





