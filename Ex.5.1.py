# Simple Expense Program
total = 0        # total money spent
count = 0        # number of expenses
while True:
   expense = input("Enter expense (or 'done'): ")
     if expense == "done":
        break
     expense = int(expense)   # change text to number
    total = total + expense  # add to total
    count = count + 1        # increase count
print("Total monthly expenditure =", total)
print("Number of expenses recorded =", count)
