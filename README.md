# Daily Expenses Tracker (Python)

A simple **command-line Python application** that helps users track their daily expenses.
The program allows you to **add, view, calculate, delete, and save expenses** using a text file for persistent storage.

---

## 📌 Features

* ➕ **Add Expense** – Add a new expense with name and amount
* 📋 **View Expenses** – Display all recorded expenses
* 🧮 **Calculate Total Expenses** – Show the total amount spent
* ❌ **Delete Expense** – Remove an expense from the list
* 💾 **Save Data** – Automatically saves expenses to a text file (`expenses.txt`) before exiting
* 📂 **File Persistence** – Loads saved expenses when the program starts

---

## 🛠️ Technologies Used

* **Python 3**
* **File Handling**
* **Loops & Conditional Statements**
* **Lists & Tuples**

---

## 📂 Project Structure

```
Daily-Expenses-Tracker
│
├── expenses.py        # Main Python program
├── expenses.txt       # File where expenses are stored
└── README.md          # Project documentation
```

---

## ▶️ How to Run the Program

1. **Clone the repository**

```
git clone https://github.com/your-username/daily-expenses-tracker.git
```

2. **Navigate to the project folder**

```
cd daily-expenses-tracker
```

3. **Run the Python program**

```
python expenses.py
```

---

## 📷 Example Menu

```
**** Daily Expenses Tracker ****
1. Add Expense
2. View Expenses
3. Calculating Expenses
4. Delete Expense
5. Saving and Exiting.....
```

---

## 🧠 How It Works

* The program first attempts to **load existing expenses** from `expenses.txt`.
* All expenses are stored as **(item, amount)** tuples in a list.
* Users interact with the program using a **menu-based system**.
* When exiting, the program **writes all expenses back to the file** so they are saved for the next run.

---

## 🚀 Possible Future Improvements

* Add **date tracking for expenses**
* Export data to **CSV or Excel**
* Create a **GUI version using Tkinter**
* Add **expense categories (Food, Travel, Bills, etc.)**
* Show **monthly statistics**

---


If you like this project, feel free to ⭐ the repository!

---
