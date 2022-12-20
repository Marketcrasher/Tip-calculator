def tip_calculator(total, tip_percentage):
    # Calculate the tip amount
    tip = total * tip_percentage

    # Calculate the total cost including the tip
    total_with_tip = total + tip

    # Return the tip amount and the total cost including the tip
    return tip, total_with_tip

# Enter in tip percentage and total price below:
total = 300
tip_percentage = 0.15
tip, total_with_tip = tip_calculator(total, tip_percentage)
print(f"Tip amount: ${tip:.2f}")
print(f"Total including tip: ${total_with_tip:.2f}")