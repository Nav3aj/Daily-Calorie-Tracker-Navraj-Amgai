"""
Project: Daily Calorie Tracker
Author: Navraj Amgai
Date: 2025-11-13
Description:
A minimal, easy-to-explain program that asks for meals and calories,
calculates total and average, checks a daily limit, and optionally saves the report.


"""

def get_number(prompt):
    # Keep asking until the user types a valid non-negative number.
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter 0 or a positive number.")
            else:
                return value
        except ValueError:
            print("That's not a number. Try again.")

def main():
    print("=== DAILY CALORIE TRACKER ===")

    # 1) Ask how many meals.
    while True:
        try:
            count = int(input("How many meals did you have today? "))
            if count <= 0:
                print("Enter 1 or more.")
            else:
                break
        except ValueError:
            print("Please enter a whole number like 1, 2, 3.")

    meals = []      # list of meal names
    calories = []   # list of numbers (calories for each meal)

    # 2) Read each meal name and its calories
    for i in range(1, count + 1):
        name = input(f"Meal {i} name: ").strip()   # simple text
        cal = get_number(f"Calories for {name}: ")
        meals.append(name)
        calories.append(cal)

    # 3) Compute total and average
    total = sum(calories)
    average = total / len(calories)

    # 4) Get daily limit and show summary
    limit = get_number("\nEnter your daily calorie limit: ")

    print("\n----- SUMMARY -----")
    for name, cal in zip(meals, calories):
        print(f"{name:15} {cal:6.1f} cal")
    print("--------------------")
    print(f"Total Calories : {total:.1f}")
    print(f"Average Calories : {average:.1f}")

    if total <= limit:
        print("You are within your limit ✅")
    else:
        print("You exceeded your limit ⚠️")

    # 5) Save option.
    save = input("\nSave report to file? (y/n): ").lower()
    if save == 'y':
        signature = "By Navraj Amgai"
        with open("calorie_report.txt", "a") as f:
            f.write("----- Daily Report -----\n")
            for name, cal in zip(meals, calories):
                f.write(f"{name:15} {cal:6.1f} cal\n")
            f.write(f"Total: {total:.1f} | Avg: {average:.1f} | Limit: {limit:.1f}\n")
            f.write(signature + "\n")
            f.write("------------------------\n\n")
        print("Saved as calorie_report.txt")
        print(signature)  
    else:
        print("Report not saved.")

    print("\nThank you — program finished.")
    print("By Navraj Amgai")

if __name__ == "__main__":

    main()
