"""MATK is a MATematiKa application."""



"""The necessary libraries for it are tkinter (for now) to generate the GUI (graphical user interface),
   and sympy. Check the sympy documentation at https://docs.sympy.org/latest/index.html
   And also numpy at https://numpy.org/doc/stable/"""





import statistics, numpy, os
from statistics import *
import numpy as np
from tkinter import (Label,
                    Button,
                    Entry,
                    Scrollbar,
                    VERTICAL,
                    font,
                    messagebox,
                    filedialog,
                    simpledialog,
                    scrolledtext
)

from functions.variables import big_number, _version_, __all__
import tkinter as tk
import sympy as sp
from sympy import (
    sympify,
    solve,
    Symbol,
    factor,
    solveset,
    Derivative
)
"""The main GUI class, with all its elements."""

class My_GUI():
    def __init__(self, janela) -> None:
        self.janela = janela
        self.barra_menu = tk.Menu(janela)
        self.janela.geometry("700x500")

        self.diretorio_salvamento = None
        self.janela.resizable(False, False)

        self.entry = Entry(self.janela, font=12 ,width=65, highlightthickness=0.50, highlightbackground="white", bg="#1f1d1c", fg="white")
        self.entry.pack(pady=15)

        label = Label(self.janela, text=">$>", bg="#1f1d1c", fg="green", font=5).place(x=12, y=14)

        self.scrolled_text = scrolledtext.ScrolledText(self.janela, width=200, height=30, fg="white", bg="#1f1d1c", state="disabled")
        self.scrolled_text.pack(padx=10, pady=10)
        self.barra_menu = tk.Menu(janela)
        

        # Create a menu 
        self.main = tk.Menu(self.barra_menu, tearoff=0)
        self.main.add_command(label="functions", command=self.all_func)


        #create a submenu (Clean) for menu
        self.submenu_clean = tk.Menu(self.main, tearoff=0)
        self.main.add_cascade(label="Clean", menu=self.submenu_clean)

        
        



        #Create a statistics menu
        self.statistics = tk.Menu(self.barra_menu, tearoff=0)
        self.statistics.add_command(label="Describe", command=self.describe)
        self.statistics.add_command(label="Info", command=self.infos)

        #Submeno of View amostrate
        self.submenu_amos = tk.Menu(self.statistics, tearoff=0)
        self.statistics.add_cascade(label="Sample", menu=self.submenu_amos)
        self.submenu_amos.add_command(label="Head", command=self.head)
        self.submenu_amos.add_command(label="Tail", command=self.tail)
        #create a submenu (Descritive) for menu
        self.submenu_descrit = tk.Menu(self.statistics, tearoff=0)
        self.statistics.add_cascade(label="Descri Stats", menu=self.submenu_descrit)
        self.submenu_descrit.add_command(label="Mean", command=self.mean_)
        self.submenu_descrit.add_command(label="Median", command=self.median_)
        self.submenu_descrit.add_command(label="Mode", command=self.mode_)
        self.submenu_descrit.add_command(label="Variance", command=self.variance_)
        self.submenu_descrit.add_command(label="Standard Deviation", command=self.stdv_)
        self.submenu_descrit.add_command(label="Outliers", command=self.outliers)


        

        # Add commands to the "Clean" submenu
        self.submenu_clean.add_command(label="Clear Result", command=self.clear_scrolled_text)
        self.submenu_clean.add_command(label="Clear Entry", command=self.clear_entry)
        self.submenu_clean.add_command(label="Clear All", command=self.clear)

        #-------------------------------------------------------------------------------#
        self.main.add_command(label="Save", command=self.caminho)
        self.main.add_command(label="version", command=version)
        self.main.add_command(label="About", command=self.about)
        #self.menu_exemplo.add_command(label="Ver atalhos", command=all_shortcuts)
        self.main.add_command(label="Quit", command=quit)

        # Add the menu to the main menu
        self.barra_menu.add_cascade(label="Main", menu=self.main)
        self.barra_menu.add_cascade(label="Stats", menu=self.statistics)
        

        # Add the main menu to the window
        self.janela.config(menu=self.barra_menu)

        scrollbar = Scrollbar(janela, orient=VERTICAL)
        scrollbar.pack(side="right", fill="y")

        self.entry.bind("<Control-c>", self.copiar_texto)
        self.entry.bind("<Control-v>", self.colar_texto)
        self.entry.bind("<Control-x>", self.cortar_texto)
        self.entry.bind("<Control-e>", lambda event: self.clear_entry())
        self.entry.bind("<Control-l>", lambda event: self.clear_label())
        self.entry.bind("<Control-o>", lambda event: self.clear())
        self.entry.bind("<Control-q>", lambda event: quit())
        self.entry.bind("<Control-s>", lambda event: self.caminho())
        self.entry.bind("<Return>", lambda event: self.pesquisar())


  

    
    def pesquisar(self):
        self.scrolled_text.configure(state="normal")
        try:
            import math
            self.entry_txt = self.entry.get().lower()

            #---------------Factorial------------------------#
            """If the command starts with the word 'fat' followed by a number, the 'fat' command will
            Calculate the factorial of the number n."""
            if self.entry_txt.startswith("fat"):
                """Transforming the two elements into a list to extract only the number."""

                entry = self.entry_txt.split()
                """-------------------0-----1--"""
                # Extracting only the number ["fat", "n"]
                ent = entry[1]
                
                """Using the math module to calculate the factorial of the number."""
                res = math.factorial(int(ent))
                self.salvar_calculos(res)
                self.scrolled_text.insert(tk.END, f">>> {res}\n")
            #-------------End of factorial-----------------------#
    
            #Square root --------------------------------#
            elif self.entry_txt.startswith("sqrt"):
                self.raiz_quadrada()
            #--------------End of sqrt----------------------#
                
            #Cube root------------------------------------#
            elif self.entry_txt.startswith("cbrt"):
                self.cube_root()
                

            #------Trigonometry section--------#
                """The syntax of trigonomety functions is: function <number>
                   Exemple:
                   >>> ln 34
                   >>> log10 45
                   >>> acosh 2"""
            """Create a dictionary to store trigonometric functions."""
            trigono_func = {
                "ln":math.log,
                "log2":math.log2,
                "log10":math.log10,
                "cos":math.cos,
                "sin":math.sin,
                "tan":math.tan,
                "acos":math.acos,
                "atan":math.atan,
                "asin":math.asin,
                "cosh":math.cosh,
                "acosh":math.acosh,
                "asinh":math.asinh,
                "atanh":math.atanh
                #You can continue, adding more functions
                
            }
            
            """trig cmd = (ln, log2, log10, cos, sin, tan, etc...) and trig_func
               are the corresponding functions for the names"""

            for trig_cmd, trig_func in trigono_func.items():
                if self.entry_txt.startswith(trig_cmd):
                    entry = self.entry_txt.split()
                    pegar_num = entry[1]
                    
                    try:
                        num = float(pegar_num)
                        if trig_cmd == 'acosh' and num < 1:
                            raise ValueError("O argumento para acosh deve ser maior ou igual a 1.")
                        
                        result = trig_func(num)
                        self.scrolled_text.insert(tk.END, f">>> {result}\n")
                        self.salvar_calculos(result)
                        break
                    except ValueError as e:
                        self.scrolled_text.insert(tk.END,f"Erro: {e}\n")

            #-------------End of trig------------------#
                
        #===================================================#

            #-------------Pow------------------#
            if "^" in self.entry_txt:
                entry = self.entry_txt.replace("^", "**")
            #------------End of pow---------------------#
                
            #==============================================#
                
            #------------Solve Equation------------#
                
              #The syntax of sol - integ gonna be the: function <the_equation>
                """Exemple:
                >>> sol 2*x - 4
                >>> integ 3*x + 1
                >>> deriv 3*x**2 """
            elif self.entry_txt.startswith("sol"):  #If the input starts with 'sol'(solve).
                try:
                    from random import choice
                    entry = self.entry_txt.replace("sol","")           # replace sol with ""
                    x = Symbol('x')
                    entry_sym = sympify(entry)                         # Create the variable 'x'
                    resol = solve(entry_sym, x)                        # And solve it
                    self.scrolled_text.insert(tk.END, f">>> {resol}\n")
                    self.salvar_calculos(resol)
            

                except Exception as e:
                    with open("main_pck\exemple.txt", 'r') as exemplo:
                        exemple = [equacao.strip() for equacao in exemplo.readlines()]
                        rand = choice(exemple)
                    self.scrolled_text.insert(tk.END, f">>> {rand}\n")

            elif self.entry_txt.startswith("set"):  # If the input starts with set (solveset).
                try:
                    from random import choice
                    entry = self.entry_txt.replace("set","")           # Replace "set" with ""

                    x = Symbol('x')
                    entry_sym = sympify(entry)                         # Create the variable 'x'
                    resol = solveset(entry_sym, x) 
                    self.scrolled_text.insert(tk.END, f">>> {resol}\n")                    # And solve it
                    self.salvar_calculos(resol)
           
                except Exception as e:
                    with open("main_pck\exemple.txt", 'r') as exemplo:
                        exemple = [equacao.strip() for equacao in exemplo.readlines()]
                        rand = choice(exemple)
                    self.scrolled_text.insert(tk.END, f">>> {rand}\n")

             #======================FIM====================#
            
            elif self.entry_txt.startswith("deriv"):  # If the input starts with deriv (derivative).
                try:
                    from random import choice
                    entry = self.entry_txt.replace("deriv","")               # Replace "deriv" with ""
                    x = Symbol('x')                                          # Create the variable 'x'
                    entry_sym = Derivative(entry, x)                         
                    resol = entry_sym.doit()                                 # And solve it
                    self.scrolled_text.insert(tk.END, f">>> {resol}\n")
                    self.salvar_calculos(resol)

                except Exception as e:
                    with open("main_pck\exemple.txt", 'r') as exemplo:
                        exemple = [equacao.strip() for equacao in exemplo.readlines()]
                        rand = choice(exemple)
                    self.scrolled_text.insert(tk.END, f">>> {res}\n")
            
            elif self.entry_txt.startswith("integ"):                     # If the input starts with integ (integral)
                try:
                    
                    from random import choice
                    entry = self.entry_txt.replace("integ","")           # Replace "deriv" with ""
                    entry_sym = sympify(entry)                  
                    resol = sp.integrate(entry_sym)                      # And solve it
                    self.scrolled_text.insert(tk.END, f">>> {resol}\n")
                    self.salvar_calculos(resol)

                except Exception as e:
                    with open("main_pck\exemple.txt", 'r') as exemplo:
                        exemple = [equacao.strip() for equacao in exemplo.readlines()]
                        rand = choice(exemple)
                    self.scrolled_text.insert(tk.END, f">>> {rand}\n")

            elif self.entry_txt.startswith("mean"):
                self.mean()
            elif self.entry_txt.startswith("med"):
                self.median()
            elif self.entry_txt.startswith("mode"):
                self.mode()
            elif self.entry_txt.startswith("stdv"):
                self.stdv()
            elif self.entry_txt.startswith("var"):
                self.variance()
            elif self.entry_txt.startswith("outliers"):
                self.detect_outliers()
            elif self.entry_txt.startswith("percentile"):
                self.percentile()
            elif self.entry_txt.startswith("pecentper"):
                self.percentile_per()
            elif self.entry_txt.startswith("mad"):
                self.mad()
            elif self.entry_txt.startswith("regression"):
                self.regressao_linear()
            elif self.entry_txt.startswith("comb"):
                self.comb()
            elif self.entry_txt.startswith("perm"):
                self.permutation()
            
            elif self.entry_txt.startswith("diff"):  # If the input starts with diff (differential).
                try:
                    from random import choice
                    entry = self.entry_txt.replace("diff","")           # substitui o "diff" por nada
                    x = Symbol('x')                                     # cria o incógnito 'x'
                    entry_sym = sympify(entry)                         
                    resol = sp.diff(entry_sym, x)        # e o resolve
                    self.scrolled_text.insert(tk.END, f">>> {resol}\n")
                    self.salvar_calculos(resol)

                except Exception as e:
                    with open("main_pck\exemple.txt", 'r') as exemplo:
                        exemple = [equacao.strip() for equacao in exemplo.readlines()]
                        rand = choice(exemple)
                    self.scrolled_text.insert(tk.END, f">>> {rand}\n")
            elif "version" in self.entry_txt:
                self.version()



            #------------Fatoração Polinomial----------#
            elif self.entry_txt.startswith("factor"):
                try:
                    entry = self.entry_txt.replace("factor","")
                    resol = factor(entry)
                    self.scrolled_text.insert(tk.END, f">>> {resol}\n")
                    self.salvar_calculos(resol)
                except Exception as e:
                    with open("main_pck\exemple.txt", 'r') as exemplo:
                        exemple = [equacao.strip() for equacao in exemplo.readlines()]
                        rand = choice(exemple)
                    self.scrolled_text.insert(tk.END, f">>> {rand}\n")
                    

            elif self.entry_txt.startswith("complex"): 
                self.complex_number()                                                           

            self.calculo_simples()   
        except Exception as e:
            print(f"Erro: {e}")

        self.scrolled_text.configure(state="disabled")



    

    # Function to calculate the square root of a complex and non-complex number
    def raiz_quadrada(self):
        self.scrolled_text.configure(state="normal")
        try:
            """The syntax of this function is sqrt <the_value>
               >>> sqrt 25
               >>> sqrt -1
               >>> sqrt -4/4
               >>> sqrt 3.9"""
            from fractions import Fraction
            import cmath, math
            if self.entry_txt.startswith("sqrt"):
                entry = self.entry_txt.replace("sqrt", "")

                # Verificar se a entrada é um número complexo
                if 'j' in entry:
                    result = cmath.sqrt(complex(entry.replace('j', '')))
                    self.scrolled_text.insert(tk.END, str(result).replace('j', 'i'))
                    self.salvar_calculos(result)
                else:
                    # Tentar converter a entrada para um número
                    num = Fraction(entry)
                    
                    # Verificar se o número é negativo
                    if num < 0:
                        result = f"i*sqrt({abs(num)})"  # Número complexo
                    elif num == -1:
                        result = "i"
                    else:
                        # Verificar se o número é uma fração
                        fraction_representation = Fraction(num)
                        if fraction_representation.denominator != 1:
                            result = fraction_representation
                        else:
                            result = math.sqrt(num)
                    
                    self.scrolled_text.insert(tk.END, f">>> {result}\n")
                    self.salvar_calculos(result)
                    
        except ValueError:
            self.scrolled_text.insert(tk.END, "#Error: Invalid input\n")
        except IndexError:
            self.scrolled_text.insert(tk.END, "#Error: Invalid input format\n")
        self.scrolled_text.configure(state="disabled")


    def cube_root(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("cbrt"):
                entry = self.entry_txt.replace("cbrt", "")
                in_number = int(entry)
                result = in_number**(1/3)
                self.scrolled_text.insert(tk.END,f">>> {result}\n")
                self.salvar_calculos(result)
        except ValueError:
            self.scrolled_text.insert(tk.END,"#Error: Invalid Input format\n" )
        self.scrolled_text.configure(state="disabled")
        
            
# This is the function for when there is no command in front of the numbers, and it will perform a simple calculation
    def calculo_simples(self):
        self.scrolled_text.configure(state="normal")
        try:
            resultado = sympify(self.entry_txt)

            self.scrolled_text.insert(tk.END, f">>> {resultado}\n")
            self.salvar_calculos(resultado)
        except Exception as e:
            print(e)
        self.scrolled_text.configure(state="disabled")
            
    
    # Handle complex numbers
    def complex_number(self):
        self.scrolled_text.configure(state="normal")
        """The syntax of this function is 
           >>> complex 2 + 3i
           >>> complex 3i + 4 * 4
           >>> complex (1i + 3) * (3 + 9i)"""
        try:
            if self.entry_txt.startswith("complex"):
                entry = self.entry_txt.replace("complex","")
                if "i" in entry:
                    entry = entry.replace("i", "j")
                    result = eval(entry)
                    resultstr = str(result).replace("j", "i")

                    self.scrolled_text.insert(tk.END, text=resultstr)
                    self.salvar_calculos(resultstr)
        except:
            pass
        self.scrolled_text.configure(state="disabled")

               


    #==========Functions for copying and pasting characters in the Entry or textbox of the window==========#
    def copiar_texto(self):
        try:
            texto = self.entry.get()
            self.entry.clipboard_clear()
            self.entry.clipboard_append(texto)
            
        except:
            pass # I didn't return anything because it's working correctly, but it's giving me an 'error' in the terminal


    def colar_texto(self):
        try:
            texto = self.entry.clipboard_get()
            self.entry.insert(tk.END, texto)
        except:
            pass #The same thing for this too


    def cortar_texto(self):
        try:
            texto = self.entry.get()
            self.entry.clipboard_clear()
            self.entry.clipboard_append(texto)
            self.entry.insert(0, tk.END)
        except:
            pass
    #===================================End Ctrl-C Ctrl-V Ctrl-X================================#
        

    #Clear the text field, the result field, and clear everything, respectively.
    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def clear_scrolled_text(self):
        self.scrolled_text.configure(state="normal")
        self.scrolled_text.delete(1.0, tk.END)
        self.scrolled_text.configure(state="disabled")

    def clear(self):
        self.scrolled_text.configure(state="normal")
        self.clear_entry()
        self.clear_scrolled_text()
        self.scrolled_text.configure(state="disabled")

    #-------------End clear--------------#

    #Show all functions of the application
  

   



    "Save the calculations to MATK_calculations.txt file on your computer"
    def salvar_calculos(self, resultado):
        self.scrolled_text.configure(state="normal")

        try:
            if self.diretorio_salvamento is None:
                # Se o diretório de salvamento não foi escolhido, peça ao usuário para escolher um
                self.diretorio_salvamento = self.caminho()

                if not self.diretorio_salvamento:
                    # Se o usuário cancelou a escolha do diretório, retorne sem salvar
                    return

            import os
            from datetime import datetime
            data = datetime.now()
            formato_data_hora = data.strftime("%d/%m/%Y %H:%M:%S")

            caminho_arquivo = os.path.join(self.diretorio_salvamento, "MATK_calculations.txt")

            if not os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, "w") as arquivo:
                    arquivo.write("MATK History\n\n\n")

            with open(caminho_arquivo, "a") as arquivo:
                arquivo.write(f"°: {self.entry_txt} = {str(resultado)} ---- Date:: ---- {formato_data_hora}\n")
        except Exception as e:
            print(f"Error when saving calculations: {e}")
        
        self.scrolled_text.configure(state="disabled")



    from tkinter import filedialog
    
    #Open the file explorer window to select the path
    def caminho(self):
        if not self.diretorio_salvamento:
            # If the directory has not been chosen yet, prompt the user to choose it
            self.diretorio_salvamento = filedialog.askdirectory(title="Where do you want to save it?")
        return self.diretorio_salvamento

    def all_func(self):
        self.scrolled_text.configure(state="normal")
        from time import sleep
        lista = [i for i in __all__]
        self.scrolled_text.insert(tk.END, f"{lista}\n\n{len(lista)} functions\n")
        self.entry.clipboard_append(lista)
        messagebox.showinfo("Information", "This list was automatically copied, you can paste it wherever you want")
        sleep(2)
        self.scrolled_text.configure(state="disabled")

    

    #The sintaxe of the functions above gonna be: function [and a list of number]
    """Exemple:
       Calculate the mean of a list of values
       >>> mean[1,2,3,4] or mean 1,2,3,4
       Calculate the regression of a list values
       >>> regression[2,3,4]
       Calculate the standard derivation of a list values
       >>> stdv[10,445,33]"""
       
       

    def mean(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("mean"):
                entry = self.entry_txt[len("mean"):].strip()  # Remove  "mean" e spaces
                numbers = [float(num) for num in entry.strip('[]').split(',')]  # convert the numbers in float
                resultado = sum(numbers) / len(numbers)
                self.scrolled_text.insert(tk.END,f">>> {resultado}\n")
                self.salvar_calculos(resultado)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")


    def median(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("med"):
                entry = self.entry_txt[len("med"):].strip()
                numbers = [float(num) for num in entry.strip('[]').split(',')]
                resultado = statistics.median(numbers)
                self.scrolled_text.insert(tk.END,f">>> {resultado}\n")
                self.salvar_calculos(resultado)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")


    def mode(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("mode"):
                entry = self.entry_txt[len("mode"):].strip()
                numbers = [float(num) for num in entry.strip('[]').split(',')]
                resultado = statistics.mode(numbers)
                self.scrolled_text.insert(tk.END,f">>> {resultado}\n")
                self.salvar_calculos(resultado)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")
    
    def stdv(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("stdv"):
                entry = self.entry_txt[len("stdv"):].strip()
                numbers = [float(num) for num in entry.strip('[]').split(',')]
                resultado = statistics.stdev(numbers)
                self.scrolled_text.insert(tk.END,f">>> {resultado}\n")
                self.salvar_calculos(resultado)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")

    def variance(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("var"):
                entry = self.entry_txt[len("var"):].strip()
                numbers = [float(num) for num in entry.strip('[]').split(',')]
                resultado = statistics.variance(numbers)
                self.scrolled_text.insert(tk.END,f">>> {resultado}\n")
                self.salvar_calculos(resultado)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")


    # Detect outliers function
    def detect_outliers(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("outliers"):
                entry = self.entry_txt[len("outliers"):].strip()
                # Convertendo a entrada para uma lista de números
                numbers = [float(num) for num in entry.strip('[]').split(',')]
                q1 = numpy.percentile(numbers, 25)
                q3 = numpy.percentile(numbers, 75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                outliers = [num for num in numbers if num < lower_bound or num > upper_bound]

                if not outliers:
                    self.scrolled_text.insert(tk.END, ">>> Não existe outliers\n")

                else:
                    self.scrolled_text.insert(tk.END,f">>> {outliers}\n")
                    self.salvar_calculos(outliers)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")

    @staticmethod
    def detect_outlier(df, coluna):
        import numpy as np
        """
        Detecta outliers em uma coluna específica de um DataFrame usando a regra do IQR.

        Args:
            df (DataFrame): O DataFrame contendo os dados.
            coluna (str): O nome da coluna na qual os outliers devem ser detectados.

        Returns:
            DataFrame: Um DataFrame contendo os outliers detectados na coluna especificada.
        """
        coluna_data = df[coluna].tolist()
        Q1 = np.percentile(coluna_data, 0.25)
        Q3 = np.percentile(coluna_data, 0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = [num for num in coluna_data if num < lower_bound or num > upper_bound]

        if not outliers:
            return "Não existe ouliers\n\n"
        else:
            return "Existe ouliers\n\n"



    def percentile(self):
        self.scrolled_text.configure(state="normal")
        try:
            """
            >>> percentile[1,2,3,4,5] #OUTPUT |
            >>> percentile 25% 2.0          <<|
                percentile 50% 3.0          <<|
                percentile 75% 4.0          <<|
                percentile 100% 5.0         <<|"""

            if self.entry_txt.startswith("percentile"):
                entry = self.entry_txt[len("percentile"):].strip()
                # Obtém o valor do percentil a partir do entry
                # Corrigir a conversão para números
                numbers = [float(num) for num in entry.strip('[]').split(',')]
                
                percentile_25 = numpy.percentile(numbers, 25)
                percentile_50 = numpy.percentile(numbers, 50)
                percentile_75 = numpy.percentile(numbers, 75)
                percentile_100 = numpy.percentile(numbers, 100)
                resultado = f">>> percentile 25%: {percentile_25}\npercentile 50%: {percentile_50}\npercentile 75%: {percentile_75}\npercentile 100%: {percentile_100}\n"
                self.scrolled_text.insert(tk.END,resultado)
                self.salvar_calculos(resultado)
               
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")

        
    def percentile_per(self):
        self.scrolled_text.configure(state="normal")
        try:
            """
            pecenper(percentile personalized)
            "The only difference with this pecentper compared to
            percentile is that the percentile already returns
            the quartiles, but this one will return based on the
            last number in the list." 
            >>> pecentper[1,2,3,4,5,100] #OUTPUT: 100% = 5.0
            >>> pecentper[1,2,3,4,5,75] #OUTPUT: 75% = 4.0"""
            if self.entry_txt.startswith("pecentper"):
                entry = self.entry_txt[len("pecentper"):].strip()
                # Obtém o valor do percentil a partir do entry
                # Corrigir a conversão para números
                numbers = [float(num) for num in entry.strip('[]').split(',')]

                numbers_discart = numbers[:-1]
                
                percentile = numpy.percentile(numbers_discart, numbers[-1])
                resultado = f">>> percentile {numbers[-1]}% : {percentile}\n"
                self.scrolled_text.insert(tk.END,resultado)
                self.salvar_calculos(resultado)
            
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")




    def mad(self):
        self.scrolled_text.configure(state="normal")
        try:
            if self.entry_txt.startswith("mad"):
                entry = self.entry_txt[len("mad"):].strip()
                numbers = [float(num) for num in entry.strip('[]').split(',')]
                mean_value = sum(numbers) / len(numbers)
                mad_resultado = sum(abs(num - mean_value) for num in numbers) / len(numbers)
                self.scrolled_text.insert(tk.END,f">>> {mad_resultado}\n")
                self.salvar_calculos(mad_resultado)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")





    def regressao_linear(self):
        self.scrolled_text.configure(state="normal")
        try:
            entry = self.entry_txt[len("regression"):].strip()
            data = [float(num) for num in entry.strip('[]').split(',')]

            # Crie um array numpy a partir dos dados
            x = np.arange(len(data))
            y = np.array(data)

            # Realize a regressão linear
            coeficientes = np.polyfit(x, y, 1)
            text=f"{coeficientes[0]:.1f}x {'+' if coeficientes[1] >= 0 else '-'} {abs(coeficientes[1]):.1f}"

            # Exiba os coeficientes da regressão linear na label
            self.scrolled_text.insert(tk.END,f">>> {text}\n")
            self.salvar_calculos(text)

        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira uma lista válida de números\n")
        self.scrolled_text.configure(state="disabled")

    
    def comb(self):
        self.scrolled_text.configure(state="normal")
        """Combination of n, k"""
        try:
            import math
            if self.entry_txt.startswith("comb"):
                entry = self.entry_txt[len("comb"):].strip()
                
                # Corrigir a conversão para inteiros
                numbers = [int(num) for num in entry.strip('[]').split(',')]
                
                result = math.comb(numbers[0], numbers[1])

                self.scrolled_text.insert(tk.END,f">>> {result}\n")
                self.salvar_calculos(result)
        except ValueError:
            self.scrolled_text.insert(tk.END,">>> Erro: Insira dois números inteiros para combinação\n")
        self.scrolled_text.configure(state="disabled")

    
    def permutation(self):
        self.scrolled_text.configure(state="normal")
        """Permutation of n, k"""
        try:
            import math
            if self.entry_txt.startswith("perm"):
                entry = self.entry_txt[len("perm"):].strip()

                numbers = [int(num) for num in entry.strip('[]').split(',')]

                result = math.perm(numbers[0], numbers[1])

                self.scrolled_text.insert(tk.END,f">>> {result}\n")
                self.salvar_calculos(result)
        except ValueError:
            self.scrolled_text.insert(tk.END, ">>> Erro: Put 2 integers values for permute\n")
        self.scrolled_text.configure(state="disabled")

    
    def describe(self):
        self.scrolled_text.configure(state="normal")
        import pandas as pd
        from tkinter import filedialog
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            try:
                if filename.endswith(".csv"):
                    df = pd.read_csv(filename)

                elif filename.endswith(".xlsx"):
                    df = pd.read_excel(filename)

                self.scrolled_text.insert(tk.END, f"DESCRIBE\n\n{round(df.describe(), 2)}\n\n")
            except Exception as e:
                self.scrolled_text.insert(tk.END, e)
        else:
            self.scrolled_text.insert(tk.END, "This file did not exist\n")
        self.scrolled_text.configure(state="disabled")

    def infos(self):
        self.scrolled_text.configure(state="normal")
        import pandas as pd
        from tkinter import filedialog
        from io import StringIO
        import sys
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if filename:
            try:
                if filename.endswith(".csv"):
                    df = pd.read_csv(filename)
                elif filename.endswith(".xlsx"):
                    df = pd.read_excel(filename)
                    
                # Converte as informações do DataFrame em uma string
                buffer = StringIO()
                sys.stdout = buffer
                df.info()
                sys.stdout = sys.__stdout__
                
                # Obtém a saída do buffer como uma string
                info_string = buffer.getvalue()
                
                # Insere a saída no widget ScrolledText
                self.scrolled_text.insert(tk.END, f"INFO\n\n{info_string}\n\n\n")
            except Exception as e:
                # Se ocorrer um erro, insira a mensagem de erro no widget
                self.scrolled_text.insert(tk.END, str(e))
        else:
            self.scrolled_text.insert(tk.END, "This file did not exist")
        self.scrolled_text.configure(state="disabled")
    

    def head(self):
        self.scrolled_text.configure(state="normal")
        import pandas as pd
        from tkinter import filedialog
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            try:
                if filename.endswith(".csv"):
                    df = pd.read_csv(filename)

                elif filename.endswith(".xlsx"):
                    df = pd.read_excel(filename)

                self.scrolled_text.insert(tk.END, f"HEAD\n\n{df.head()}\n\n")
            except Exception as e:
                self.scrolled_text.insert(tk.END, e)
        else:
            self.scrolled_text.insert(tk.END, "This file did not exist\n")
        self.scrolled_text.configure(state="disabled")

    def tail(self):
        self.scrolled_text.configure(state="normal")
        import pandas as pd
        from tkinter import filedialog
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            try:
                if filename.endswith(".csv"):
                    df = pd.read_csv(filename)

                elif filename.endswith(".xlsx"):
                    df = pd.read_excel(filename)

                self.scrolled_text.insert(tk.END, f"TAIL\n\n{df.tail()}\n\n")
            except Exception as e:
                self.scrolled_text.insert(tk.END, e)
        else:
            self.scrolled_text.insert(tk.END, "This file did not exist\n")
        self.scrolled_text.configure(state="disabled")

    
    def outliers(self):
        self.scrolled_text.configure(state="normal")
        import pandas as pd
        from tkinter import filedialog, simpledialog
        dado = simpledialog.askstring("Inserir dado", "Digita nome da coluna:")
        coluna = dado
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
       

        if filename:
            if filename.endswith(".csv"):
                try:
                    df = pd.read_csv(filename)
                    if coluna in df.columns:
                        self.scrolled_text.insert(tk.END, f"OUTLIERS\n\n{self.detect_outlier(df, dado)}")
                    else:
                        self.scrolled_text.insert(tk.END, "Você deve colocar a coluna para voce calcular o outlier\n\n")
                except:
                    self.scrolled_text.insert(tk.END, "Esse arquivo não é tipo csv\n\n")
        self.scrolled_text.configure(state="disabled")



    

    #==--------------------------Descriptive statistics---------------------------------==#
                    
    def mean_(self):
        import pandas as pd
        #Calculate the mean of a number column of a dataframe
        self.scrolled_text.configure(state="normal")
        dado = simpledialog.askstring("Nome da coluna", "Insira o nome da coluna:")

        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            if filename.endswith(".csv"):
                df = pd.read_csv(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"MEAN\n\n>>> {mean(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, ">>> Não existe essa coluna\n\n")
            
            elif filename.endswith(".xlsx"):

                df = pd.read_excel(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"MEAN\n\n>>> {mean(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, ">>> Não existe essa coluna\n\n")
        else:
            messagebox.showerror("Erro", "Arquivo deve ser .csv ou .xlsx")
        self.scrolled_text.configure(state="disabled")


    
    def median_(self):
        #Calculate the median of a number column of a dataframe
        self.scrolled_text.configure(state="normal")
        import pandas as pd
        dado = simpledialog.askstring("Nome da coluna", "Insira o nome da coluna:")

        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            if filename.endswith(".csv"):
                df = pd.read_csv(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"MEDIAN\n\n>>> {median(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, ">>> Não existe essa coluna\n\n")
            
            elif filename.endswith(".xlsx"):

                df = pd.read_excel(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"MEDIAN\n\n{median(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, ">>> Não existe essa coluna\n\n")
        else:
            messagebox.showerror("Erro", "Arquivo deve ser .csv ou .xlsx")
        self.scrolled_text.configure(state="disabled")

    def mode_(self):
        #Calculate the mode of a number column of a dataframe
        self.scrolled_text.configure(state="normal")
        import pandas as pd
        dado = simpledialog.askstring("Nome da coluna", "Insira o nome da coluna:")

        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            if filename.endswith(".csv"):
                df = pd.read_csv(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"MODE\n\n>>> {mode(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, ">>> Não existe essa coluna\n\n")
            
            elif filename.endswith(".xlsx"):

                df = pd.read_excel(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"MEAN\n\n>>> {mean(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, ">>> Não existe essa coluna\n\n")
        else:
            messagebox.showerror("Erro", "Arquivo deve ser .csv ou .xlsx")
        self.scrolled_text.configure(state="disabled")

    def variance_(self):
        self.scrolled_text.configure(state="normal")
        #Calculate the variance of a number column of a dataframe
        import pandas as pd
        dado = simpledialog.askstring("Nome da coluna", "Insira o nome da coluna:")

        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            if filename.endswith(".csv"):
                df = pd.read_csv(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"VARIANCE\n\n>>> {variance(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, "Não existe essa coluna\n\n")
            
            elif filename.endswith(".xlsx"):

                df = pd.read_excel(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"VARIANCE\n\n>>> {variance(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, "Não existe essa coluna\n\n")
        else:
            messagebox.showerror("Erro", "Arquivo deve ser .csv ou .xlsx")
        self.scrolled_text.configure(state="disabled")

    def stdv_(self):
        self.scrolled_text.configure(state="normal")
        #Calculate the stdv of a number column of a dataframe
        import pandas as pd
        dado = simpledialog.askstring("Nome da coluna", "Insira o nome da coluna:")

        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

        if filename:
            if filename.endswith(".csv"):
                df = pd.read_csv(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"STANDARD DEVIATION\n\n>>> {stdev(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, "Não existe essa coluna\n\n")
            
            elif filename.endswith(".xlsx"):

                df = pd.read_excel(filename)
                coluna = df[dado].tolist()

                if coluna:
                    self.scrolled_text.insert(tk.END, f"STANDARD DEVIATION\n\n>>> {stdev(coluna)}\n\n")
                else:
                    self.scrolled_text.insert(tk.END, "Não existe essa coluna\n\n")
        else:
            messagebox.showerror("Erro", "Arquivo deve ser .csv ou .xlsx")
        
        self.scrolled_text.configure(state="disabled")


    # A function for the "about Menu button 
    def about(self):

        self.clear_scrolled_text()
        self.scrolled_text.configure(state="normal")
        import sys, os
        from io import StringIO

        relative_path = os.path.relpath("/home/sam/Documentos/pYTHON/Trabalho/Matk/LICENSE")
        rel_path = os.path.relpath("LICENSE")
        with open(rel_path, "r") as text:
            buffer = StringIO()
            sys.stdout = buffer
            content = text.read()
            sys.stdout = sys.__stdout__


        self.scrolled_text.insert(tk.END, f"{content}\n\n")

        self.scrolled_text.configure(state="disabled")



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

