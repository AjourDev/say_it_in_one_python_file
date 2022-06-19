########
# Ajourdev © Nick
########

from tkinter import *
from random import randint
import re

lorem_ipsum_list = ['donec', 'dictumst', 'parturient', 'commodo', 'habitasse', 'sem', 'aliquam', 'tellus', 'amet', 'turpis', 'senectus', 'diam', 'integer', 'lectus', 'molestie', 'egestas', 'sollicitudin', 'at', 'laoreet', 'risus', 'odio', 'velit', 'pretium', 'fames', 'quam', 'libero', 'vitae', 'sed', 'fermentum', 'mus', 'dis', 'nibh', 'curabitur', 'sit', 'ultrices', 'vestibulum', 'urna', 'leo', 'habitant', 'condimentum', 'potenti', 'placerat', 'arcu', 'sodales', 'scelerisque', 'natoque', 'suspendisse', 'in', 'adipiscing', 'vehicula', 'eiusmod', 'quisque', 'ultricies', 'consequat', 'mollis', 'rutrum', 'nunc', 'luctus', 'aliqua', 'sapien', 'lobortis', 'mauris', 'ullamcorper', 'phasellus', 'tempus', 'id', 'a', 'ornare', 'gravida', 'ridiculus', 'eros', 'dictum', 'convallis', 'tristique', 'varius', 'penatibus', 'nullam', 'vulputate', 'elementum', 'tempor', 'praesent', 'bibendum', 'lacinia', 'eleifend', 'sociis', 'erat', 'elit', 'vel', 'metus', 'nam', 'mi', 'tortor', 'volutpat', 'suscipit', 'pharetra', 'facilisi', 'nulla', 'euismod', 'nascetur', 'sagittis', 'incididunt', 'auctor', 'nisl', 'lacus', 'felis', 'ante', 'dapibus', 'tincidunt', 'etiam', 'dignissim', 'augue', 'nec', 'enim', 'eu', 'hac', 'viverra', 'fringilla', 'cras', 'cursus', 'rhoncus', 'non', 'proin', 'eget', 'porttitor', 'est', 'porta', 'maecenas', 'mattis', 'facilisis', 'nisi', 'faucibus', 'semper', 'magnis', 'magna', 'netus', 'consectetur', 'ac', 'posuere', 'labore', 'malesuada', 'interdum', 'platea', 'morbi', 'justo', 'dolore', 'montes', 'feugiat', 'duis', 'orci', 'ligula', 'imperdiet', 'dui', 'hendrerit', 'neque', 'pulvinar', 'vivamus', 'ut', 'congue', 'venenatis', 'blandit', 'quis', 'do', 'iaculis', 'massa', 'fusce', 'ipsum', 'dolor', 'pellentesque', 'aliquet', 'aenean', 'lorem', 'et', 'accumsan', 'purus']
lorem_ipsum_list_len = len(lorem_ipsum_list)

def make_words(amount:int) -> str:
    return ' '.join([lorem_ipsum_list[randint(0, lorem_ipsum_list_len-1)] for _ in range(amount)])

def make_sentences(amount:int) -> str:
    min_words_in_sentence = 8
    max_in_sentence_cap = 25
    sl = [randint(min_words_in_sentence, max_in_sentence_cap) for _ in range(amount)]
    acl = []
    for amount in sl:
        for idx in range(amount):
            sent = lorem_ipsum_list[randint(0, lorem_ipsum_list_len-1)]
            acl.append(sent.capitalize() if idx == 0 else sent)
        acl.append('.')
    return ' '.join(acl).replace(' .', '.')

def make_paragraph(amount:int) -> str:
    paragraph_min = 3
    paragraph_max = 5
    pl = [randint(paragraph_min, paragraph_max) for _ in range(amount)]
    pcl = []
    for paragraph_amount in pl:
        pcl.append(make_sentences(paragraph_amount))
    return '\n\n'.join(pcl)

def generate(event=None):
    global gen_selection, amount_var, selection
    if gen_selection.get() == '' or amount_var == '' or not re.match('^[0-9]+$', amount_var.get()): return
    if gen_selection.get() == selection[0]:
        tb1.delete(1.0, "end-1c")
        tb1.insert(INSERT, make_words(int(amount_var.get())))
    if gen_selection.get() == selection[1]:
        tb1.delete(1.0, "end-1c")
        tb1.insert(INSERT, make_sentences(int(amount_var.get())))
    if gen_selection.get() == selection[2]:
        tb1.delete(1.0, "end-1c")
        tb1.insert(INSERT, make_paragraph(int(amount_var.get())))

# Setup TKinter
root = Tk()
root.title("Lorem Ipsum Generator")
root.geometry("800x500")
root.resizable(0, 0)
root.rowconfigure(0, weight=6)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
[root.columnconfigure(idx, weight=1) for idx in range(3)]

# Textfield
text_container = Frame(root, bg='gray')
text_container.grid(column=0, columnspan=3, row=0, sticky='NEWS')
text_container.grid_rowconfigure(0, weight=1)
text_container.grid_columnconfigure(0, weight=1)

tb1 = Text(text_container, wrap='word')
tb1.grid(column=0, row=0, sticky='NEWS')

text_sb = Scrollbar(text_container, orient="vertical", command=tb1.yview)
text_sb.grid(column=1, row=0, sticky='NS')
tb1['yscrollcommand'] = text_sb.set

selection = ['Words', 'Sentences', 'Paragraphs']
gen_selection = StringVar(value='Sentences')
OptionMenu(root, gen_selection, *selection).grid(row=1, column=0)

amount_var = StringVar(value='0')
Entry(root, textvariable=amount_var).grid(row=1, column=1)

Button(root, text='Generate!', command=generate).grid(row=1, column=2)

root.mainloop()
