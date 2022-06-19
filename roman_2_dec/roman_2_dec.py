########
# Ajourdev © Nick
########

from tkinter import *
import re

decimals = { 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M' }
num_list, spec_num_list, tens = [1000, 500, 100, 50, 10, 5, 1], [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], [100, 10, 1]

def get_non_regular_numerals(num) -> str:
    tt = max(filter(lambda i: i < num, tens))
    return f'{decimals[tt]}{decimals[num+tt]}'

def convert_roman_to_dec(val_str:StringVar=None):
    num_str = ''
    val = val_str.get()
    if not re.match('^[0-9]+$', val) or val == None: return
    val = int(val)
    while val != 0:
        for num in spec_num_list:
            if val >= num:
                num_str += decimals[num] if num in num_list else get_non_regular_numerals(num)
                val -= num
                break
    dec_var.set(num_str)
    return num_str

# Setup TKinter
root = Tk()
root.title("Roman2Dec")
root.geometry("400x200")
root.resizable(0, 0)

# Grid
[root.rowconfigure(idx, weight=1) for idx in range(2)]
[root.columnconfigure(idx, weight=1+idx) for idx in range(2)]

# Decimal
Label(root, text='Decimal').grid(row=0, column=0, sticky='E')

roman_var = StringVar(value='0')
roman_var.trace('w', lambda n, i, m, roman_var=roman_var: convert_roman_to_dec(roman_var))

bin_entry = Entry(root, textvariable=roman_var)
bin_entry.grid(row=0, column=1)

# Decimals
Label(root, text='Roman numerals').grid(row=1, column=0, sticky='E')

dec_var = StringVar(value='0')

dec_entry = Label(root, textvariable=dec_var)
dec_entry.grid(row=1, column=1)

root.mainloop()
