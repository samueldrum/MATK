# main.py

from tkinter import Tk
from principal_root import My_GUI  #Adjust the import here.

class Run(My_GUI):
    def main():
        jan = Tk()
        app = My_GUI(jan)
        jan.title("MATK")
        jan.configure(bg="#1f1d1c")
        jan.mainloop()

if __name__ == "__main__":
    Run.main()

