from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox 
import string
import random

window = Tk()
window.geometry("700x500")
window.title("Random Password Generator")
window.config(background="light blue")
window.resizable(False, False)

def password_generate():
    len_password = val.get()
    num_special = special_var.get()
    num_digits = digits_var.get()

    len_special_digits=num_special+num_digits

    if len_password == 0 or num_special > len_password or num_digits > len_password or len_special_digits > len_password:
        messagebox.showerror("Invalid Input", "Please enter valid values.")
        return
    
    special_characters = ''.join(random.choice(string.punctuation) for _ in range(num_special))
    digit_characters = ''.join(random.choice(string.digits) for _ in range(num_digits))

    all_char=string.ascii_uppercase+string.ascii_lowercase

    remaining_len = len_password - num_special - num_digits
    if remaining_len < 0:
        remaining_len = 0

    password_str = ''.join(random.choice(all_char) for _ in range(remaining_len))
    
    shuffled_password = special_characters + digit_characters + password_str
    shuffled_password_list = list(shuffled_password)
    random.shuffle(shuffled_password_list)
    shuffled_password = ''.join(shuffled_password_list)

    password.set(shuffled_password)


title_label = Label(window, text="Random Password Generator", background="light blue", foreground="black", font=("Arial", 18, "bold"))
title_label.pack(anchor="center", pady=20)

length_label = Label(window, text="Enter the length of your password:", background="light blue", foreground="darkgreen", font=("Arial", 14, "bold"))
length_label.place(x=20, y=90)

val = IntVar()
selector = Combobox(window, textvariable=val, state="readonly")
selector['values'] = [str(i) for i in range(1, 16)]
selector.place(x=420, y=90)

special_label = Label(window, text="Enter the number of special characters:", background="light blue", foreground="darkgreen", font=("Arial", 14, "bold"))
special_label.place(x=20, y=120)

special_var = IntVar()
special_entry = Entry(window, textvariable=special_var, font=("Arial", 14))
special_entry.place(x=420, y=120)

digits_label = Label(window, text="Enter the number of digits:", background="light blue", foreground="darkgreen", font=("Arial", 14, "bold"))
digits_label.place(x=20, y=150)

digits_var = IntVar()
digits_entry = Entry(window, textvariable=digits_var, font=("Arial", 14))
digits_entry.place(x=420, y=150)

generate_button = Button(window, text="Generate Password", background="orange", foreground="black", font=("Arial", 14), cursor="hand2", command=password_generate)
generate_button.pack(anchor="center", pady=180)

res_label = Label(window, text="Generated Password is:", background="light blue", foreground="darkgreen", font=("Arial", 14, "bold"))
res_label.place(x=20, y=360)

password = StringVar()
password_final = Entry(window, textvariable=password, state="readonly", foreground="blue", font=("Arial", 14))
password_final.place(x=300, y=360)

window.mainloop()
