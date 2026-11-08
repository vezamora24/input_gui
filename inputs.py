import tkinter as tk, os, csv
root = tk.Tk()
root.title("Input GUI app")
root.geometry("400x500")
root.config(bg = "lightblue")
root.iconbitmap("python_18894.ico")

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

root.mainloop()
