# pip3 install tk
from tkinter import *
import re

bin_value = ''
dec_value = ''
is_converting = False

def convert_bin_to_dec(val:StringVar=None):
    global bin_value, dec_var, is_converting
    val_str = val.get()
    if val_str == '' or is_converting: return
    is_converting = True
    if re.match('^[0-1]+$', val_str):
        bin_value = str(val_str)
        dec_var.set(int(bin_value, 2))
    else: val.set(bin_value)
    is_converting = False

def convert_dec_to_bin(val:StringVar=None):
    global dec_value, bin_var, is_converting
    val_str = val.get()
    if val_str == '' or is_converting: return
    is_converting = True
    if re.match('^[0-9]+$', val_str):
        dec_value = str(val_str)
        bin_var.set(bin(int(dec_value))[2:])
    else: val.set(dec_value)
    is_converting = False

# Setup TKinter
root = Tk()
root.title("Bin2Dec")
root.geometry("400x200")
root.resizable(0, 0)

# Grid
[root.rowconfigure(idx, weight=1) for idx in range(2)]
[root.columnconfigure(idx, weight=1+idx) for idx in range(2)]

# Binary
Label(root, text='Binary').grid(row=0, column=0, sticky='E')

bin_var = StringVar(value='0')
bin_var.trace('w', lambda n, i, m, bin_var=bin_var: convert_bin_to_dec(bin_var))

bin_entry = Entry(root, textvariable=bin_var)
bin_entry.grid(row=0, column=1)

# Decimals
Label(root, text='Decimal').grid(row=1, column=0, sticky='E')

dec_var = StringVar(value='0')
dec_var.trace('w', lambda n, i, m, dec_var=dec_var: convert_dec_to_bin(dec_var))

dec_entry = Entry(root, textvariable=dec_var)
dec_entry.grid(row=1, column=1)

root.mainloop()
