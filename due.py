def calculate_due_amount(amount_paid, total_bill):
    due = amount_paid - total_bill
    return due

# Example values based on your story
total_bill = 2.50
amount_paid = 4.00

due_amount = calculate_due_amount(amount_paid, total_bill)
print(f"The shopkeeper should return ${due_amount:.2f} to Vishal.")
