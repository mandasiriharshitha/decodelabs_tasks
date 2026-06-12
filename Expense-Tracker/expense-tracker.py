print("------------------------------")
print("      EXPENSE TRACKER")
print("------------------------------")

total_spent = 0

num_expenses = int(input("\nEnter the number of expenses: "))

for i in range(1, num_expenses + 1):
    expense = float(input(f"Enter expense {i}: "))
    total_spent += expense

print("\n------------------------------")
print("      EXPENSE SUMMARY")
print("------------------------------")

print(f"\nTotal Spent: ₹{total_spent}")

print("\nThank you for using Expense Tracker!")
