from tkinter import *
import random
import time

# Root Window Setup
root = Tk()
root.geometry("1200x700")
root.title("Kenyan Restaurant Management System")

# Top Frame for Title and Time
top_frame = Frame(root, width=1200, relief=SUNKEN)
top_frame.pack(side=TOP, fill=X)

# Main Frame for Inputs and Outputs
main_frame = Frame(root, relief=SUNKEN)
main_frame.pack(side=LEFT, fill=BOTH, expand=True)

# Styling Variables
title_font = ('helvetica', 30, 'bold')
label_font = ('arial', 16, 'bold')
entry_bg_color = "#e6f7ff"
button_bg_color = "#008cba"

# Time Display
localtime = time.asctime(time.localtime(time.time()))

# Title and Time Display
Label(top_frame, font=title_font, text="Welcome to Nyama Haven Restaurant", fg="black", anchor='w').pack(pady=10)
Label(top_frame, font=('arial', 20, 'bold'), text=localtime, fg="green", anchor='w').pack()

# Variables
rand = StringVar()
fries = StringVar()
ugali = StringVar()
soup = StringVar()
chapati = StringVar()
mbuzi = StringVar()
drinks = StringVar()
subtotal = StringVar()
tax = StringVar()
total = StringVar()
service_charge = StringVar()

# Utility Functions

def validate_numeric(value):
    try:
        return float(value)
    except ValueError:
        return 0

def calculate():
    rand.set(random.randint(10000, 99999))
    
    # Retrieve Values
    cost_fries = validate_numeric(fries.get()) * 150  # Ksh
    cost_ugali = validate_numeric(ugali.get()) * 100
    cost_soup = validate_numeric(soup.get()) * 180
    cost_chapati = validate_numeric(chapati.get()) * 50
    cost_mbuzi = validate_numeric(mbuzi.get()) * 500
    cost_drinks = validate_numeric(drinks.get()) * 120

    # Calculate Costs
    meal_cost = cost_fries + cost_ugali + cost_soup + cost_chapati + cost_mbuzi + cost_drinks
    tax_cost = meal_cost * 0.16
    service_cost = meal_cost * 0.1
    total_cost = meal_cost + tax_cost + service_cost

    # Update Outputs
    subtotal.set(f"Ksh {meal_cost:.2f}")
    tax.set(f"Ksh {tax_cost:.2f}")
    service_charge.set(f"Ksh {service_cost:.2f}")
    total.set(f"Ksh {total_cost:.2f}")

def reset():
    variables = [rand, fries, ugali, soup, chapati, mbuzi, drinks, subtotal, tax, service_charge, total]
    for var in variables:
        var.set("")

def exit_app():
    root.destroy()

# Menu and Inputs
menu_items = [
    ("Fries", fries),
    ("Ugali", ugali),
    ("Soup", soup),
    ("Chapati", chapati),
    ("Mbuzi Choma", mbuzi),
    ("Drinks", drinks)
]

for i, (item, var) in enumerate(menu_items):
    Label(main_frame, text=item, font=label_font, anchor="w").grid(row=i, column=0, padx=10, pady=5)
    Entry(main_frame, font=label_font, textvariable=var, bd=5, bg=entry_bg_color, justify="right").grid(row=i, column=1, padx=10, pady=5)

# Outputs
output_items = [
    ("Sub Total", subtotal),
    ("Tax (16%)", tax),
    ("Service Charge (10%)", service_charge),
    ("Total", total)
]

for i, (item, var) in enumerate(output_items):
    Label(main_frame, text=item, font=label_font, anchor="w").grid(row=i, column=2, padx=10, pady=5)
    Entry(main_frame, font=label_font, textvariable=var, bd=5, bg=entry_bg_color, justify="right", state="readonly").grid(row=i, column=3, padx=10, pady=5)

# Buttons
Button(main_frame, text="Calculate", font=label_font, bg=button_bg_color, fg="white", command=calculate).grid(row=6, column=0, padx=10, pady=20)
Button(main_frame, text="Reset", font=label_font, bg=button_bg_color, fg="white", command=reset).grid(row=6, column=1, padx=10, pady=20)
Button(main_frame, text="Exit", font=label_font, bg=button_bg_color, fg="white", command=exit_app).grid(row=6, column=2, padx=10, pady=20)

# Start GUI
root.mainloop()
