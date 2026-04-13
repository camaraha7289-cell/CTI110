# Anthony Camara- hernandez 
# 4/12/2026
# P2LAB2
#
# Create dictionary with key-value pairs (vehicle : mpg)
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}
# Print the keys
print("Available vehicles:")
print(vehicles.keys())

# Ask user to choose a vehicle
vehicle_choice = input("\nEnter a vehicle to see it's MPG: ")

# Check if the vehicle exists in the dictionary
if vehicle_choice in vehicles:
    mpg = vehicles[vehicle_choice]
    
    # Display mpg
    print(f"The MPG for {vehicle_choice} is {mpg}.")
    
    # Ask for miles to drive
    miles = float(input("Enter the number of miles you will drive: "))
    
    # Calculate gallons needed
    gallons_needed = miles / mpg
    
 # Display result with added wording
    print(f"You will need {gallons_needed:.2f} gallons of gas needed to drive the vehicle {miles:.2f} miles.")
