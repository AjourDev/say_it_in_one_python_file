import re
from tkinter import *

username_re = '^[A-Za-z]\w{3,19}$'
mail_re = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
password_re = '^\S{8,20}'

def validate_input(event=None):
    global username_var, email_var, password_var, val_var
    if not re.match(username_re, username_var.get()):
        val_var.set('Invalid username')
    elif not re.match(mail_re, email_var.get()):
        val_var.set('Invalid mail')
    elif not re.match(password_re, password_var.get()):
        val_var.set('Invalid password!')
    else:
        val_var.set('It is valid!')

def reset_input(event=None):
    global username_var, email_var, password_var
    username_var.set('')
    email_var.set('')
    password_var.set('')
    pass

# Setup TKinter
root = Tk()
root.title("Input validation")
root.geometry("400x200")
root.resizable(0, 0)

[root.rowconfigure(idx, weight=1) for idx in range(5)]
[root.columnconfigure(idx, weight=1) for idx in range(2)]

username_var = StringVar()
email_var = StringVar()
password_var = StringVar()

username_var.trace('w', lambda n, i, m, username_var=username_var: validate_input())
email_var.trace('w', lambda n, i, m, username_var=username_var: validate_input())
password_var.trace('w', lambda n, i, m, username_var=username_var: validate_input())

val_var = StringVar(value='Invalid username')

Label(root, text='Username:').grid(row=0, column=0, sticky='E')
Label(root, text='Email:').grid(row=1, column=0, sticky='E')
Label(root, text='Password:').grid(row=2, column=0, sticky='E')

Entry(root, textvariable=username_var).grid(row=0, column=1, sticky='W')
Entry(root, textvariable=email_var).grid(row=1, column=1, sticky='W')
Entry(root, textvariable=password_var).grid(row=2, column=1, sticky='W')

Label(root, textvariable=val_var).grid(row=3, column=0, columnspan=2, sticky='NEWS')

Button(root, text='Reset', command=reset_input).grid(row=4, column=0, columnspan=2)

root.mainloop()
