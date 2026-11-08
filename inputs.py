import tkinter as tk, os, csv
from tkinter import messagebox

root = tk.Tk()
root.title("Input GUI app")
root.geometry("400x500")
root.config(bg = "lightblue")
root.iconbitmap("python_18894.ico")

def submit():
    #print("Submitted the data!")
    folder = "DATA"
    full_path = folder + os.sep + "info.csv"
    header = ["status", "age", "name", "address", "employed"]
    if not os.path.exists(folder):
        os.mkdir(folder)
        with open(full_path, "w") as w:
            write = csv.writer(w)
            write.writerow(header)

    status = married_var.get()
    age = age_var.get()
    address = address_text.get("1.0", "end-1c")
    name = name_entry.get()
    employed = employed_var.get()
    data = {"status": status, "age": age, "address": address, "name": name, "employed": employed}
    #print(data)
    msg = messagebox.askquestion("Is this the correct info?", str(data))

    if msg == "yes":
        messagebox.showinfo("Thank you!", "Your data has been submitted successfully!")
        print(data)
        with open(full_path, "a") as w:
            write = csv.writer(w)
            write.writerow(data.values())
## LABELS
## NAME
name_label = tk.Label(root, text = "Full Name: ")
name_label.place(x = 20, y = 50)
name_entry = tk.Entry(root)
name_entry.place(x = 120, y=50)

## ADDRESS
address_label = tk.Label(root, text = "Full Address: " )
address_label.place(x = 20, y = 80)
address_text = tk.Text(root, width = 23, height = 3)
address_text.place(x = 120, y = 80)

## AGE
age_label = tk.Label(root, text = "Age: ")
age_label.place(x = 20, y = 150)
age_var = tk.IntVar()
age_var.set(18)
age_option = tk.OptionMenu (root, age_var, *list(range(18, 61)))
age_option.place(x = 120, y = 150)

## EMPLOYEE STATUS
employed_label = tk.Label(root, text = "Employed status: ")
employed_label.place(x = 20, y = 180)
employed_var = tk.BooleanVar()
employed_check = tk.Checkbutton(root, variable = employed_var)
employed_check.place(x = 120, y = 180)
                            
## MARITAL STATUS
marital_label = tk.Label(root, text = "Marital status: ")
marital_label.place(x = 20, y = 200)
married_var = tk.StringVar()
married_var.set("Single")
marital_radio1 = tk.Radiobutton(root, text="Single", variable = married_var, value = "Single")
marital_radio2 = tk.Radiobutton(root, text="Married", variable = married_var, value = "Married")
marital_radio1.place(x = 120, y = 200)
marital_radio2.place(x = 180, y = 200)

## SUBMIT BUTTON
submit_button = tk.Button(root, text="Submit", command = submit)
submit_button.place(x = 150, y = 250)

root.mainloop()
