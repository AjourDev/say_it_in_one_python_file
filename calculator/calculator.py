from tkinter import *
from functools import partial
import re

# Setup TKinter
root = Tk()
root.title("Bin2Dec")
root.geometry("400x500")
root.resizable(0, 0)

calculations = []
calc_value = 0

def is_last_calc(lapp) -> bool:
    if lapp == '/' or lapp == 'X' or lapp == '-' or lapp == '+': return True
    else: return False

def calculation(val1, calc_t, val2) -> float:
    val1, val2 = float(val1), float(val2)
    if calc_t == '/': return 0 if val1 == 0 and val2 == 0 else val1 / val2
    elif calc_t == '*': return val1 * val2
    elif calc_t == '+': return val1 + val2
    else: return val1 - val2

def calc_list(l_p) -> float:
    for idx, calc in enumerate(l_p):
        if is_last_calc(calc): l_p[idx+1] = calculation(l_p[idx-1], calc, l_p[idx+1])
        elif calc == '=': return l_p[idx-1]

def calc_input(event:str=''):
    global number_var, calc_value, calculations, calc_var
    cur_val = number_var.get()
    if event == 'AC':
        cur_val = 0
        number_var.set(f'{cur_val}')
        calculations.clear()
        calc_var.set('0')
        return

    if re.match('^[0-9]+$', event):
        new_val = int(cur_val + event)
        number_var.set(new_val)
    
    if event == '/' or event == 'X' or event == '-' or event == '+':
        # if not is_last_calc(calculations[-1]):
        calculations.append(cur_val)
        calculations.append(event)
        number_var.set('0')
        calc_var.set(' '.join(calculations))

    if event == '=' and len(calculations) > 1:
        calculations.append(cur_val)
        calculations.append('=')
        result_val = '%0.2f' % calc_list(list(calculations))
        calculations.append(str(result_val))
        calc_var.set(' '.join(calculations))
        number_var.set('0')
        calculations.clear()

    if event == '+/-':
        cur_val = int(cur_val) * -1
        number_var.set(f'{cur_val}')

# Grid
[root.rowconfigure(idx, weight=1) for idx in range(7)]
[root.columnconfigure(idx, weight=1) for idx in range(4)]

button_names = [
    'AC', '+/-', '', '/',
    '7', '8', '9', 'X',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '', '', '='
    ]

row = 1
for idx, button_name in enumerate(button_names):
    temp_colspan = 1
    col = idx % 4
    if col == 0: row += 1
    if row == 6 and col == 0: temp_colspan = 3
    if row == 2 and col == 1: temp_colspan = 2
    
    if button_name != '':
        Button(root, text=button_name, command=partial(calc_input, button_name)).grid(row=row, columnspan=temp_colspan, column=col, sticky='NEWS', padx=5, pady=5)

calc_var = StringVar(value='0')
calc_label = Label(root, bg='black', textvariable=calc_var, foreground='white', font=('Arial', 17))
calc_label.grid(row=0, rowspan=1, column=0, columnspan=4, sticky='NEWS', padx=5, pady=5)

number_var = StringVar(value='0')
number_label = Label(root, bg='black', textvariable=number_var, foreground='white', font=('Arial', 25))
number_label.grid(row=1, rowspan=1, column=0, columnspan=4, sticky='NEWS', padx=5, pady=5)

root.mainloop()
