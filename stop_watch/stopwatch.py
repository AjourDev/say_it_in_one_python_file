########
# Ajourdev © Nick
########

import threading
import time
from tkinter import *
from tkinter import ttk

# App constants
timer_started = False
timer_value = 0

# Manage background thread
TIMER_SPEED = 0.1
app_is_running = True
def app_timer():
    global TIMER_SPEED, app_is_running, timer_started, timer_value, timer_var
    while(app_is_running):
        time.sleep(TIMER_SPEED)
        if timer_started:
            timer_value += TIMER_SPEED
            timer_var.set(timer_format(timer_value))

APP_THREAD = threading.Thread(target=app_timer)
def init_app_timer():
    global APP_THREAD
    APP_THREAD.start()

# App methods
def timer_format(seconds:int=0) -> str:
    return f'{int(seconds // 60 // 60)} Hours\n{int(seconds // 60) % 60} Minutes\n{(seconds % 60):.1f} Seconds'

def start_stop_timer(event=None):
    global timer_started
    timer_started = not timer_started
    start_stop_string.set('Stop' if timer_started else 'Start')

def reset_timer(event=None):
    global timer_started, timer_value
    if timer_started: return
    timer_var.set(timer_format())
    timer_value = 0

# Setup TKinter
root = Tk()
root.geometry('400x200')
root.title('Stopwatch')
root.resizable(0, 0)

ROOT_ROWS = 4
ROOT_COLUMNS = 2

[root.rowconfigure(idx, weight=1) for idx in range(ROOT_ROWS)]
[root.columnconfigure(idx, weight=1) for idx in range(ROOT_COLUMNS)]

timer_var = StringVar(value=timer_format())

Label(root, textvariable=timer_var, bg='black', font=('Arial', 20)).grid(row=0, rowspan=ROOT_ROWS-1, column=0, columnspan=2, sticky='NEWS', pady=5, padx=5)

start_stop_btn = Button(root, text='Reset', command=reset_timer)
start_stop_btn.grid(row=ROOT_ROWS-1, column=0, sticky='NEWS', pady=5, padx=5)

start_stop_string = StringVar(value='Start')
reset_btn = Button(root, textvariable=start_stop_string, command=start_stop_timer)
reset_btn.grid(row=ROOT_ROWS-1, column=1, sticky='NEWS', pady=5, padx=5)

init_app_timer()
root.mainloop()

app_is_running = False
APP_THREAD.join()
