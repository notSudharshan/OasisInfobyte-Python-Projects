import tkinter as tk
def bmicalcy():
        hieght = float(height_entry.get())
        weight = float(weight_entry.get())
        if hieght <= 0 or weight <= 0:
            messagebox.showerror("ZERO error", "Height and weight should be above zero.")
            return
        bmi = weight / (hieght ** 2)
        bmi = round(bmi, 1)
        result_label.config(text=f"BMI: {bmi}")
        if bmi < 18.5:
            status = "You are underweight."
        elif bmi < 25:
            status = "You are normal."
        elif bmi < 30:
            status = "A bit overweight."
        else:
            status = "Obese range."
        status_label.config(text=status)
window = tk.Tk()
window.title("Basic BMI Calculator")
tk.Label(window, text="Height (m):").grid(row=0, column=0, pady=6, sticky="w")
tk.Label(window, text="Weight (kg):").grid(row=1, column=0, pady=6, sticky="w")
height_entry = tk.Entry(window)
height_entry.grid(row=0, column=1, pady=6)
weight_entry = tk.Entry(window)
weight_entry.grid(row=1, column=1, pady=6)
tk.Button(window, text="Check BMI", command=bmicalcy).grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)
status_label = tk.Label(window, text="")
status_label.grid(row=4, column=0, columnspan=2)
window.mainloop()
