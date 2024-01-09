print("Welcome to the Tip calculator!")

# Inputs

bill_amount = float(input("Enter the bill amount: $"))
tip_percentage = float(input("Enter tip percentage (e.g., 12, 15 or 20%): "))
people = int(input("How many people to split the bill: "))

# Calculate tip and total

tip_amount = bill_amount * (tip_percentage / 100)
total_amount_each = (bill_amount + tip_amount) / people

# Output

print(f"Tip: ${tip_amount:.2f}")
print(f"Each person should pay: ${total_amount_each:.2f}")