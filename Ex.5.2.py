# Simple Monthly Expense Program
food = 0
travel = 0
shopping = 0

while True:
    category = input("Enter category (Food/Travel/Shopping or 'done'): ")
    
    if category == "done":
        break
    
    amount = int(input("Enter expense amount: "))
    
    if category == "Food":
        food = food + amount
    elif category == "Travel":
        travel = travel + amount
    elif category == "Shopping":
        shopping = shopping + amount
    else:
        print("Invalid category!")

print("\n--- Monthly Expense Summary ---")
print("Food     =", food)
print("Travel   =", travel)
print("Shopping =", shopping)
print("Total    =", food + travel + shopping)
