from tkinter import *
from datetime import datetime, date

# Setup TKinter
root = Tk()
root.geometry('700x400')
root.title('Calendar')
root.resizable(0, 0)

max_rows = 7
max_columns = 7

[root.rowconfigure(idx, weight=1) for idx in range(max_rows+1)]
[root.columnconfigure(idx, weight=1) for idx in range(max_columns)]

date_time_keeper = datetime.today()
first_of_month = datetime(date_time_keeper.date().year, date_time_keeper.date().month, 1)

showing_month = date_time_keeper.date().month
showing_year = date_time_keeper.date().year

MONTHS = [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
DAYS = [None, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
CURRENT_MONTH = MONTHS[date_time_keeper.date().month]

def get_days_in_month(year, month):
    if month == 12: return (date(year+1, 1, 1) - date(year, month, 1)).days
    else: return (date(year, month+1, 1) - date(year, month, 1)).days

def get_prev_month(event=None):
    global showing_month, showing_year, grid_holder
    if showing_month == 1: showing_month = 12; showing_year -= 1
    else: showing_month -= 1
    dim = get_days_in_month(showing_year, showing_month)
    if grid_holder == None: return
    t_am = 1 - DAYS.index(datetime(showing_year, showing_month, 1).strftime("%A"))
    for label in grid_holder:
        t_am += 1
        if t_am > 0 and t_am <= dim: label.config(text=f'{t_am}')
        else: label.config(text='')
    current_month_var.set(f'Today: {date_time_keeper.strftime("%A")}, {CURRENT_MONTH} {date_time_keeper.day} {date_time_keeper.year}\nShowing: {MONTHS[showing_month]} {showing_year}')

def get_next_month(event=None):
    global showing_month, showing_year, grid_holder
    if showing_month == 12: showing_month = 1; showing_year += 1
    else: showing_month += 1
    dim = get_days_in_month(showing_year, showing_month)
    if grid_holder == None: return
    t_am = 1 - DAYS.index(datetime(showing_year, showing_month, 1).strftime("%A"))
    for label in grid_holder:
        t_am += 1
        if t_am > 0  and t_am <= dim:
            label.config(text=f'{t_am}')
        else: label.config(text='')
    current_month_var.set(f'Today: {date_time_keeper.strftime("%A")}, {CURRENT_MONTH} {date_time_keeper.day} {date_time_keeper.year}\nShowing: {MONTHS[showing_month]} {showing_year}')

def get_current_month():
    global first_of_month, grid_holder, showing_month, showing_year
    if grid_holder == None: return
    t_am = 1 - DAYS.index(first_of_month.strftime("%A"))
    dim = get_days_in_month(showing_year, showing_month)
    for label in grid_holder:
        t_am += 1
        if t_am > 0  and t_am <= dim:
            label.config(text=f'{t_am}')
        else: label.config(text='')
    current_month_var.set(f'Today: {date_time_keeper.strftime("%A")}, {CURRENT_MONTH} {date_time_keeper.day} {date_time_keeper.year}\nShowing: {MONTHS[showing_month]} {showing_year}')

def init_month_holder() -> list:
    t_holder = list()
    for row_idx in range(max_rows-1):
        for col_idx in range(max_columns):
            lb = Label(root, bg='black', text='')
            lb.grid(row=row_idx+2, column=col_idx, sticky='NEWS', padx=1, pady=1)
            t_holder.append(lb)
    return t_holder

current_month_var = StringVar()

Button(root, text='<', command=get_prev_month).grid(row=0, column=0, sticky='NEWS', padx=1, pady=1)
Button(root, text='>', command=get_next_month).grid(row=0, column=max_columns-1, sticky='NEWS', padx=1, pady=1)

cur_month_label = Label(root, textvariable=current_month_var, bg='black', foreground='White')
cur_month_label.grid(row=0, column=1, columnspan=max_columns-2, sticky='NEWS', padx=1, pady=1)

[Label(root, bg='black', text=f'{day}').grid(row=1, column=idx, sticky='NEWS', padx=1, pady=1) for idx, day in enumerate(DAYS, -1) if day != None]

grid_holder = init_month_holder()
get_current_month()

root.mainloop()
