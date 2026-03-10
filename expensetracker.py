expenses = []
try:
    with open("expenses.txt", "r") as f:
        for line in f:
            item, amount = line.strip().split(" - ")
            expenses.append((item, float(amount)))
except FileNotFoundError:
    pass

while True:
    print("\n**** Daily Expenses Tracker ****")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculating Expenses")
    print("4. Delete Expense")
    print("5. Saving and Exiting.....")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter the amount of expense: "))
        expenses.append((item, amount))
        print("Expense added!")
    elif choice =="2":
        print("\n Your Expenses")
        for item, amount in expenses:
            print(f"{item} - {amount}")
    elif choice =="3":
        total = sum(amount for item, amount in expenses)
        print(f"Calculating Expenses: {total}")
    elif choice == "4":
        if len(expenses)==0:
            print("There is no expenses available to be deleted")
        else:
            print("\nExpenses List:")
            i = 0
            for expense in expenses:
                print(i+1, "-", expense[0], "-", expense[1])
                i = i + 1

            num = int(input("Enter expense number to delete: "))

            if num >= 1 and num <= len(expenses):
                expenses.pop(num-1)
                print("Expense deleted!")
            else:
                print("Invalid number")
    elif choice == "5":
        with open("expenses.txt", "w") as f:
          for item, amount in expenses:
            f.write(item + " - " + str(amount) + "\n")
        f.close()

        print("Saved & Exiting program...")
        break
        
    
    else:
        print("Invalid choice!Please Try again.") 