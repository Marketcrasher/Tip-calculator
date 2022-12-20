# Program to calculate the tip for a restaurant bill

# Prompt the user to enter the total bill amount
bill_amount = float(input("Enter the total bill amount: "))

# Prompt the user to enter the desired tip percentage
tip_percentage = float(input("Enter the desired tip percentage: "))

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount due
total_amount = bill_amount + tip_amount

# Display the tip amount and total amount due
print("Tip amount: $" + str(tip_amount))
print("Total amount due: $" + str(total_amount))
