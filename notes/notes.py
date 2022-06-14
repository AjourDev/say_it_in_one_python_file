from tkinter import *
from functools import partial
import os

notes_list = []
selected_note = 0

NOTE_DIR = 'notes.bin'

if os.path.exists(NOTE_DIR):
    with open(NOTE_DIR, 'rb') as file:
        file_data = file.read()
        if file_data != b'': 
            file_data_arr = file_data.split(b'.--.')
            notes_list = [datapoint.decode('utf-16') for datapoint in file_data.split(b'.--.')]

# Methods
def save_notelist():
    global notes_list
    saving_list = [bin_enc.encode('utf-16') for bin_enc in notes_list]
    saving_list = b'.--.'.join(saving_list)
    with open(NOTE_DIR, 'wb') as file:
        file.write(saving_list)

def init_notes():
    global notes_list
    if len(notes_list) == 0: return
    note_title = ''
    for note in notes_list:
        if note.split('\n')[0] == '': note_title = '-'
        else: note_title = note.split('\n')[0]
        lb1.insert(0, note_title)

def select_note(event=None):
    global selected_note, lb1
    if lb1.size() == 0 or lb1.curselection() == (): return
    selected_note = lb1.curselection()[0]
    tb1.delete(1.0, "end-1c")
    tb1.insert(INSERT, notes_list[selected_note])

def new_note(event=None):
    new_note_val = 'New note'
    notes_list.insert(0, new_note_val)
    lb1.insert(0, new_note_val)
    selected_note = 0
    lb1.selection_set(selected_note)
    save_notelist()
    select_note()

def delete_note(event=None):
    global selected_note, lb1
    if lb1.size() == 0: return
    lb1.delete(selected_note)
    notes_list.pop(selected_note)
    save_notelist()
    if selected_note > 0:
        selected_note = 0
        lb1.selection_set(0)
        select_note()

def save_note(event=None):
    global selected_note, lb1
    if lb1.size() == 0: return
    tb_val = tb1.get(1.0, "end-1c")
    if tb_val == '': return
    lb1.delete(selected_note)
    note_title = tb1.get(1.0, END).splitlines()[0]
    if note_title == '': note_title = '-'
    lb1.insert(selected_note, note_title)
    notes_list[selected_note] = tb1.get(1.0, "end-1c")
    save_notelist()

# Setup TKinter
root = Tk()
root.title("Notes")
root.geometry("800x500")
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

root.rowconfigure(0, weight=1)

notes_container = Frame(root, bg='gray')
notes_container.grid(column=0, row=0, sticky='NEWS')
notes_container.grid_rowconfigure(0, weight=1)
notes_container.grid_columnconfigure(0, weight=1)

lb1 = Listbox(notes_container)
lb1.grid(column=0, row=0, sticky='NEWS')

vsb = Scrollbar(notes_container, orient="vertical", command=lb1.yview)
vsb.grid(column=1, row=0, sticky='NS')
lb1['yscrollcommand'] = vsb.set
lb1.bind('<<ListboxSelect>>', select_note)

text_container = Frame(root, bg='gray')
text_container.grid(column=1, row=0, rowspan=2, sticky='NEWS')
text_container.grid_rowconfigure(0, weight=1)
text_container.grid_columnconfigure(0, weight=1)

tb1 = Text(text_container)
tb1.grid(column=0, row=0, sticky='NEWS')

text_sb = Scrollbar(text_container, orient="vertical", command=tb1.yview)
text_sb.grid(column=1, row=0, sticky='NS')
tb1['yscrollcommand'] = text_sb.set

btn_container = Frame(root)
btn_container.grid(column=0, row=1, sticky='NEWS')
[btn_container.grid_columnconfigure(idx, weight=1) for idx in range(3)]

Button(btn_container, text='Delete', command=delete_note).grid(column=0, row=0, sticky='NEWS', padx=5, pady=5)
Button(btn_container, text='Create', command=new_note).grid(column=1, row=0, sticky='NEWS', padx=5, pady=5)
Button(btn_container, text='Save', command=save_note).grid(column=2, row=0, sticky='NEWS', padx=5, pady=5)

init_notes()
root.mainloop()
