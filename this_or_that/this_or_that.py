from tkinter import *
import os
from random import randint
from PIL import Image, ImageTk
from collections import Counter

# Setup TKinter
root = Tk()
root.geometry('800x600')
root.title('This or That')
root.resizable(0, 0)

# Rows
root.rowconfigure(0, weight=4)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Constants/Variables
MEDIA_DIR = 'media'
if not os.path.exists(MEDIA_DIR): os.mkdir(MEDIA_DIR)
media = [f'{MEDIA_DIR}/{img}' for img in os.listdir(MEDIA_DIR) if '.jpg' in img.lower() or '.png' in img.lower()]
score = {}.fromkeys(media, 0)
if len(media) == 0 or len(media) == 1: exit()

# Methods
def select_images() -> set:
    img_set = set()
    if len(media) == 0 or len(media) == 1: return
    while len(img_set) != 2:
        img_set.add(media[randint(0, len(media)-1)])
    return img_set

img1_dir = ''
img2_dir = ''
def new_img():
    global this_img_canvas, that_img_canvas, img1_dir, img2_dir
    img1_dir, img2_dir = select_images()
    this_size = [this_img_canvas.winfo_height(), this_img_canvas.winfo_width()]
    that_size = [that_img_canvas.winfo_height(), that_img_canvas.winfo_width()]

    img1 = Image.open(img1_dir)
    img2 = Image.open(img2_dir)
    img1.thumbnail((this_size[0]-20, this_size[1]-20))
    img2.thumbnail((that_size[0]-20, that_size[1]-20))

    img_1 = ImageTk.PhotoImage(img1)
    img_2 = ImageTk.PhotoImage(img2)

    this_img_canvas.create_image(this_size[1] // 2, this_size[0] // 2, image=img_1)
    this_img_canvas.image = img_1

    that_img_canvas.create_image(that_size[1] // 2, that_size[0] // 2, image=img_2)
    that_img_canvas.image = img_2

def select_this():
    score[img1_dir] += 1
    score_var.set(get_top())
    new_img()

def select_that():
    score[img2_dir] += 1
    score_var.set(get_top())
    new_img()

def get_top() -> str:
    if len(media) > 2: return '\n'.join([f'{val[0]}: {val[1]}' for val in Counter(score).most_common(3)])
    elif len(media) == 2: return '\n'.join([f'{val[0]}: {val[1]}' for val in Counter(score).most_common(2)])
    else: return 'N/A'

# UI setup
this_img_canvas = Canvas(root, relief=RIDGE, bd=2)
this_img_canvas.grid(row=0, column=0, sticky='NEWS', padx=5, pady=5)

that_img_canvas = Canvas(root, relief=RIDGE, bd=2)
that_img_canvas.grid(row=0, column=1, sticky='NEWS', padx=5, pady=5)

this_btn = Button(root, text='This', command=select_this).grid(row=1, column=0)
that_btn = Button(root, text='That', command=select_that).grid(row=1, column=1)

score_var = StringVar(value=get_top())
Label(root, textvariable=score_var).grid(row=2, column=0, columnspan=2, sticky='NEWS')

root.after(80, new_img)
root.mainloop()
