from tkinter import messagebox
from tkinter import Entry, filedialog
import guis.principal_root as GUP
from tkinter import *
from sympy import sympify
import tkinter as tk
from variables import(
     _version_,
     __all__,
     big_number
)


inst = GUP.My_GUI()
entry = inst.self.entry
scrol = inst.self.scrolled_text
# Function to view shortcut commands
def all_shortcuts():

    text = """                   Ctrl-c: Copy text from the entry\n
                Ctrl-v: Paste text from the entry anywhere\n
                Ctrl-x: Cut the text and paste it anywhere\n
                Ctrl-e: Clear the text field\n
                Ctrl-l: Clear the result field\n
                Ctrl-o: Clean All (Clear everything)\n
                Ctrl-q: Quit (Exit)\n"""
    messagebox.showinfo("Shortcut", text)



# See the version Of MATK 
def version():
    messagebox.showinfo("Version", f"Version: {_version_}\n01/02/2024")


# This function is for when the number becomes too large, it will return ("It's too large")
def Numero_Grande(res):
    res = float(res)
    if res >=big_number:
        return "Its so big"
    else:
        return "909"
#================================And of LN(Large Number)================================#



