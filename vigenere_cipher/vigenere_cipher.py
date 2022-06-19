########
# Ajourdev © Nick
########

from tkinter import *
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def enc_vigenere_cipher(text_input:str='', cipher_input:str='') -> str:
    if text_input == '' or cipher_input == '' or not re.match('^[a-zA-Z]+$', text_input) or not re.match('^[a-zA-Z]+$', cipher_input): return None
    text_input = text_input.lower()
    cipher_input = cipher_input.lower()

    if len(text_input) > len(cipher_input):
        while len(text_input) > len(cipher_input):
            cipher_input += cipher_input
    
    cipher_input = cipher_input[:len(text_input)]

    enc = ''.join([alphabet[(alphabet.index(text_input[idx]) + alphabet.index(cipher_input[idx])) % 26] for idx, _ in enumerate(text_input)])
    return enc

def dec_vigenere_cipher(enc_input:str='', cipher_input:str='') -> str:
    if enc_input == '' or cipher_input == '' or not re.match('^[a-zA-Z]+$', enc_input) or not re.match('^[a-zA-Z]+$', cipher_input): return None
    enc_input = enc_input.lower()
    cipher_input = cipher_input.lower()

    if len(enc_input) > len(cipher_input):
        while len(enc_input) > len(cipher_input):
            cipher_input += cipher_input
    
    cipher_input = cipher_input[:len(enc_input)]

    dec = ''
    for idx, _ in enumerate(enc_input):
        tt = alphabet.index(enc_input[idx]) - alphabet.index(cipher_input[idx])
        dec += alphabet[tt + 26 if tt < 0 else tt]
    return dec

typing = False

def enc_vigener_cipher_command(val:StringVar):
    global enc_var, key_var, dec_var, typing
    if typing: return
    typing = True
    dec_var.set(enc_vigenere_cipher(enc_var.get(), key_var.get()))
    typing = False

def dec_vigener_cipher_command(val:StringVar):
    global enc_var, key_var, dec_var, typing
    if typing: return
    typing = True
    enc_var.set(dec_vigenere_cipher(dec_var.get(), key_var.get()))
    typing = False

# Setup TKinter
root = Tk()
root.title("Vigenere Cipher")
root.geometry("400x200")
root.resizable(0, 0)

# Grid
[root.rowconfigure(idx, weight=1) for idx in range(3)]
[root.columnconfigure(idx, weight=1+(idx*2)) for idx in range(2)]

# Text
Label(root, text='Text').grid(row=0, column=0, sticky='E')

enc_var = StringVar()
enc_var.trace('w', lambda n, i, m, enc_var=enc_var: enc_vigener_cipher_command(enc_var))

bin_entry = Entry(root, textvariable=enc_var)
bin_entry.grid(row=0, column=1)

# Key
Label(root, text='Key').grid(row=1, column=0, sticky='E')

key_var = StringVar()
# key_var.trace('w', lambda n, i, m, key_var=enc_var: enc_vigener_cipher_command(enc_var))

bin_entry = Entry(root, textvariable=key_var)
bin_entry.grid(row=1, column=1)

# Ciphertext
Label(root, text='Ciphertext').grid(row=2, column=0, sticky='E')

dec_var = StringVar()
dec_var.trace('w', lambda n, i, m, dec_var=dec_var: dec_vigener_cipher_command(dec_var))

bin_entry = Entry(root, textvariable=dec_var)
bin_entry.grid(row=2, column=1)

root.mainloop()
