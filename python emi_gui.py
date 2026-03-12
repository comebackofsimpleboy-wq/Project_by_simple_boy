import tkinter as tk
from tkinter import messagebox

def calculate_emi():
    try:
        loan_amount = float(entry_loan.get())
        annual_interest_rate = float(entry_interest.get())
        tenure_years = float(entry_tenure.get())

        monthly_interest_rate = annual_interest_rate / (12 * 100)
        months = tenure_years * 12

        emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / \
              ((1 + monthly_interest_rate) ** months - 1)

        total_payment = emi * months
        total_interest = total_payment - loan_amount

        result_label.config(
            text=f"Monthly EMI: ₹{round(emi,2)}\n"
                 f"Total Payment: ₹{round(total_payment,2)}\n"
                 f"Total Interest: ₹{round(total_interest,2)}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create window
root = tk.Tk()
root.title("EMI Calculator")
root.geometry("400x350")

# Labels & Entries
tk.Label(root, text="Loan Amount (₹)").pack(pady=5)
entry_loan = tk.Entry(root)
entry_loan.pack()

tk.Label(root, text="Annual Interest Rate (%)").pack(pady=5)
entry_interest = tk.Entry(root)
entry_interest.pack()

tk.Label(root, text="Loan Tenure (Years)").pack(pady=5)
entry_tenure = tk.Entry(root)
entry_tenure.pack()

# Button
tk.Button(root, text="Calculate EMI", command=calculate_emi, bg="green", fg="white").pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()