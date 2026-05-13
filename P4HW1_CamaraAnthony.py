# Anthony Camara hernandez
# 4/30/2026
# Anthony Camara hernandez
# 4/29/2026
# P4HW1
# Use while loop and for loop together

# Ask user how many scores they want to enter
num_scores = int(input("How many scores would you like to enter? "))

scores = []

# Loop to collect scores
for i in range(num_scores):

    while True:
        score = float(input(f"Enter score #{i + 1}: "))

        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("Invalid score. Please enter a score between 0 and 100.")

# Save original list before removing lowest
original_scores = scores.copy()

# Find and remove lowest score
lowest_score = min(scores) # removes lowest score
scores.remove(lowest_score) 

# Calculate average
average = sum(scores) / len(scores)

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print("Lowest Score:", lowest_score)
print("Modified List:", scores)
print("Average Score:", round(average, 2))
print("Letter Grade:", letter_grade)
print("--------------------------------")
