# 🎂 Age Calculator
# 📅 Day 26 of 90 Days Python Series by Momina Raheel

from datetime import datetime

print("✨ Welcome to the Age Calculator ✨")

while True:
    # 🧑 Ask user for their birthdate
    birth_date_input = input("\nEnter your birthdate (YYYY-MM-DD): ")

    try:
        # ✅ Convert input string to a datetime object
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

        # 📅 Get current date
        today = datetime.today()

        # 🧮 Calculate age in years
        age_years = today.year - birth_date.year

        # Adjust if birthday hasn't happened yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1

        # 🧮 Calculate months and days difference
        age_months = (today.month - birth_date.month) % 12
        if today.day < birth_date.day:
            age_months = (age_months - 1) % 12

        # Print the result
        print(f"\n🎉 You are {age_years} years and {age_months} months old!")

    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

    # Ask if user wants to calculate again
    again = input("\nDo you want to calculate another age? (yes/no): ").lower()
    if again != "yes":
        print("\nThanks for using the Age Calculator! 🧡")
        break
