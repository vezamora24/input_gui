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
## EMPLOYEE STATUS
## MARITAL STATUS
## SUBMIT BUTTON

root.mainloop()
