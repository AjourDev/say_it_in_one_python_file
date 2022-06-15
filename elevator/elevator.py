import time
from tkinter import *
import threading
from functools import partial

floors_selected = list()
def go_to_floor(t=None):
    global floor_buttons, floors_selected, current_floor
    if len(floors_selected) == 0:
        if t not in floors_selected and int(t) != current_floor:
            if int(t) == 0:
                gf_button.config(foreground='#AA5')
            else:
                floor_buttons[int(t)-1].config(foreground='#AA5')
        
            floors_selected.append(int(t))
            floors_selected.sort()
            print(floors_selected)

def visual_chevron(is_going_up):
    if is_going_up:
        up_label.config(image=up_image_sample)
        down_label.config(image='')
    else:
        down_label.config(image=down_image_sample)
        up_label.config(image='')


app_is_running = True
time_closing = 0
time_opening = 0
floor_time = 4
current_floor_time = 0
next_floor = 0

def move_elevator(time=0):
    global current_floor, floors_selected, is_going_up, elevator_doors_open
    global time_closing, is_moving, current_floor_time, next_floor, time_opening

    if not is_moving:
        if len(floors_selected) != 0 and elevator_doors_open and not is_moving:
            next_floor = floors_selected[0]
            elevator_doors_open = False
            time_closing = int(time)
            visual_chevron(floors_selected[0] > current_floor)
            print('Closing doors')
        elif len(floors_selected) != 0 and not elevator_doors_open and time - time_closing == 4 and not is_moving:
            time_closing = 0
            current_floor_time = 0
            is_moving = True
            if current_floor == 0: gf_button.config(foreground='black')
            else: floor_buttons[current_floor-1].config(foreground='black')
            print(f'Doors closed, going to floor {floors_selected[0]}')
    elif is_moving:
        current_floor_time += 1
        if current_floor_time == 4 and current_floor != next_floor:
            current_floor_time = 0
            if floors_selected[0] > current_floor: current_floor += 1
            else: current_floor -= 1
            if current_floor == 0: current_floor_stringvar.set(f'Ground floor')
            else: current_floor_stringvar.set(f'Floor: {current_floor}')
        elif current_floor == next_floor and not elevator_doors_open:
            elevator_doors_open = True
            time_opening = int(time)
            print('Opening doors')
        elif time - time_opening == 4 and is_moving:
            floors_selected.remove(current_floor)
            if current_floor == 0: gf_button.config(foreground='green')
            else: floor_buttons[current_floor-1].config(foreground='green')
            is_moving = False
            down_label.config(image='')
            up_label.config(image='')
            print('Doors open')
        
def app_timer():
    global floors_selected, is_going_up
    app_time = 0
    while(app_is_running):
        app_time += 1
        time.sleep(0.5)
        move_elevator(app_time)

def init_elevator_timer():
    global thread1
    thread1 = threading.Thread(target=app_timer)
    thread1.start()

MEDIA_DIR = 'media'
thread1 = None
typefont = ('Arial', 25)

# Setup TKinter
root = Tk()
root.geometry('700x500')
root.title('Elevator')
root.resizable(0, 0)

root.rowconfigure(0, weight=1)

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)

floor_amount = 32 # Excluding Ground floor
is_moving = False
is_going_up = True
elevator_doors_open = True
current_floor = 0
current_floor_stringvar = StringVar(value=f'Ground floor')

left_container = Frame(root, bg='black')
left_container.grid(row=0, column=0, sticky='NEWS')

rows = 8
columns = 4

[left_container.rowconfigure(idx, weight=1) for idx in range(rows+1)]
[left_container.columnconfigure(idx, weight=1) for idx in range(columns)]

right_container = Frame(root, bg='lightblue')
right_container.grid(row=0, column=1, sticky='NEWS')

[right_container.rowconfigure(idx, weight=1) for idx in range(3)]
right_container.columnconfigure(0, weight=1)

# Load images
up_image = PhotoImage(file = f'{MEDIA_DIR}/caret-up.png')
up_image_sample = up_image.subsample(5, 5)

down_image = PhotoImage(file = f'{MEDIA_DIR}/caret-down.png')
down_image_sample = down_image.subsample(5, 5)

up_label = Label(right_container, bg='lightblue')
up_label.grid(row=0, column=0, sticky='S')

current_floor_label = Label(right_container, textvariable=current_floor_stringvar, font=typefont , bg='lightblue', foreground='black')
current_floor_label.grid(row=1, column=0)


down_label = Label(right_container, bg='lightblue')
down_label.grid(row=2, column=0, sticky='N')

floor_buttons = [Button(left_container, command=partial(go_to_floor, idx+1), text=f'{idx+1}', font=typefont) for idx in range(floor_amount)]
gf_button = Button(left_container, command=partial(go_to_floor, 0), font=typefont, text=f'Ground floor', foreground='green')
gf_button.grid(row=rows, column=0, columnspan=columns, sticky='NEWS')

row_k = -1
for idx, floor_button in enumerate(floor_buttons):
    if idx % columns == 0: row_k +=1
    if idx < columns * rows:
        floor_button.grid(row=row_k, column=idx % columns, sticky='NEWS', pady=2, padx=2)

init_elevator_timer()
root.mainloop()

if thread1 != None:
    app_is_running = False
    thread1.join()
