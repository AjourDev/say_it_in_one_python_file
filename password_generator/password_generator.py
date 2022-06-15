from tkinter import *
from tkinter import ttk
from secrets import randbits
import random

# 0=No signs, 1=Signs
comb_chars = [
    'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789',
    'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789 !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    ]

sl_steps = [(idx+1) for idx in range(40)]

def generate_password(event=None):
    global pass_length, pwd_var
    random.seed(randbits(256))
    comb_index = choices.index(pwd_sel.get())
    new_pass = ''.join([comb_chars[comb_index][random.randint(0, len(comb_chars[comb_index])-1)] for _ in range(pass_length.get())])
    pwd_var.set(new_pass)

def set_slider(val):
    global pass_length
    pass_length.set(min(sl_steps, key=lambda x:abs(x-float(val))))
    pass_label_string.set(f'Length: {pass_length.get()}')

# Setup TKinter
root = Tk()
root.title("Password generator")
root.geometry("500x200")
root.resizable(0, 0)

[root.rowconfigure(idx, weight=1) for idx in range(4)]
[root.columnconfigure(idx, weight=1+idx*3) for idx in range(2)]

pwd_var = StringVar()
Label(root, text='Password: ').grid(row=0, column=0, sticky='E')
Entry(root, textvariable=pwd_var).grid(row=0, column=1, sticky='WE', padx=5, pady=5)

pass_length = IntVar(value=10)
pass_label_string = StringVar(value='Length: 10')
Label(root, textvariable=pass_label_string).grid(row=1, column=0)
pass_scale = ttk.Scale(root, variable=pass_length, value=10, from_=0, to=40, command=set_slider,)
pass_scale.grid(row=1, column=1, sticky='WE', padx=5, pady=5)

choices = ['No special signs', 'Include special signs']
pwd_sel = StringVar(value='No special signs')
OptionMenu(root, pwd_sel, *choices).grid(row=2, column=0, columnspan=2)

Button(root, text='Generate', command=generate_password).grid(row=3, column=0, columnspan=2)

generate_password()
root.mainloop()
