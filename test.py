import pandas as pd
from guis.principal_root import My_GUI
from tkinter import simpledialog
import sys

df = pd.read_csv("dados.csv")


with open("LICENSE", "r") as text:
    cont = text.read()

print(cont)