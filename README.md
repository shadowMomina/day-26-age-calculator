

# 🎂 Age Calculator – Day 26 of 90 Days Python Series

Ever wondered exactly how old you are — not just in years but also in months? 😎
This beginner-friendly Python **Age Calculator** makes it easy! Just enter your birthdate, and it instantly tells your age in years and months.

A fun and practical way to learn how to work with Python’s **`datetime`** module. 🐍✨

---

## 🧠 Features

✅ Calculate exact age in years and months
✅ Uses the built-in `datetime` module
✅ Validates input format (YYYY-MM-DD)
✅ Runs until the user decides to exit
✅ Beginner-friendly — perfect for Python learners

---

## ⚙️ How It Works

1. The program asks for your birthdate in `YYYY-MM-DD` format.
2. It uses `datetime` to calculate your current age.
3. It displays your age in years and months.
4. You can calculate multiple ages without restarting the program.

### 🧾 Example:

```
✨ Welcome to the Age Calculator ✨

Enter your birthdate (YYYY-MM-DD): 2002-09-15

🎉 You are 23 years and 0 months old!

Do you want to calculate another age? (yes/no): no

Thanks for using the Age Calculator! 🧡
```

---

## 💻 Concepts Used

* `datetime` module
* `while` loops
* `try` and `except` for input validation
* Conditional logic
* User input/output formatting

---

## 🧩 Code Overview

```python
from datetime import datetime

print("✨ Welcome to the Age Calculator ✨")

while True:
    birth_date_input = input("\nEnter your birthdate (YYYY-MM-DD): ")

    try:
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
        today = datetime.today()

        age_years = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1

        age_months = (today.month - birth_date.month) % 12
        if today.day < birth_date.day:
            age_months = (age_months - 1) % 12

        print(f"\n🎉 You are {age_years} years and {age_months} months old!")

    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

    again = input("\nDo you want to calculate another age? (yes/no): ").lower()
    if again != "yes":
        print("\nThanks for using the Age Calculator! 🧡")
        break
```

---

## 🚀 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/shadowMomina/python-age-calculator.git
   ```
2. **Navigate to the folder**

   ```bash
   cd python-age-calculator
   ```
3. **Run the script**

   ```bash
   python age_calculator.py
   ```

---

## 🌸 About This Project

This project is part of my **90 Days Python Series**, where I build simple, useful, and fun Python projects every day to strengthen my programming skills.

Day 26 focuses on **date handling and calculations** with real-world applications. 🚀

---

## 📂 Repository

🔗 [GitHub Repo: python-age-calculator](https://github.com/shadowMomina/python-age-calculator)

---

## 📜 License

**Self-Independent License (Free for Learning & Use)**

You are free to:

* ✅ Use this code for personal or educational purposes
* ✅ Modify, enhance, or build on top of it
* ✅ Share it with proper credit

**Conditions:**

* Do not sell or redistribute under your own name without attribution.
* Keep author credit visible: **Created by Momina Raheel (shadowMomina)**.

---

## 💬 Author

👩‍💻 **Momina Raheel**
📅 *90 Days Python Series* — Building something new every day!

Follow along for more daily coding projects and beginner-friendly tools. 🌟

