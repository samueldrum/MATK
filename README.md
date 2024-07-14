# MATK

**MATK** is a Mathematics statistic and finance (pre) application developed in Python with a graphical interface using Tkinter. It offers functionalities based on the SymPy library for symbolic calculations. For detailed information on using SymPy's features, please refer to

[![SymPy Version](https://img.shields.io/badge/SymPy-1.12-green)](https://www.sympy.org/)
[![NumPy Version](https://img.shields.io/badge/NumPy-1.26-blue)](https://numpy.org/doc/stable/)
[![Pandas Version](https://img.shields.io/badge/Pandas-2.2.0-yellow)](https://pandas.pydata.org/docs/)



## Features

### 1. Calculation of a Factorial of a Number
To calculate the factorial of a number `n`, enter the command `fat n` in the input and get the result.

Example:
```python
fat 5
```

### 2. Square Root
Calculate the square root of a number, whether complex or real, using the `sqrt` command.

Example:
```python
sqrt 16
```
Complex number
```python
sqrt -1
```
https://github.com/BidjorySamuel/MATK/assets/158420011/5874cd69-15c9-44af-ad47-46ab89e787af

Cube root
```python
cbrt 27
```

### 3. Trigonometric Functions
Perform trigonometric calculations, such as natural logarithm, logarithm base 2, logarithm base 10, cosine, sine, and tangent, using the commands `ln`, `log2`, `log10`, `cos`, `sin`, and `tan`, and more.

Example:
```python
ln 10
```

### 4. Equation Solving and Factoring
Solve equations and simplify expressions by factoring. Use the `sol` command to solve polynomial equations with `set` for solveset, and `fator` to factor followed by the equation or expression.

Example:
```python
sol x**2 - 4 = 0
```
```python
set x**2 - 4 = 0
```
Example:
```python
fator x**2 - 4
```

### 5. Exponentiation
Perform exponentiation operations using the `^` character.

Example:
```python
2^3
```

### 5.1 Calculations
Solve calculations in MATK, including derivative, differential, integral functions.

Example of a derivative of x^2:
```python
deriv x**2 
```

Example: Differential of x^2
```python
diff x**2
```

Example: Integral of x^2
```python
integ x**2
```
Exemple: Percentil os [1,2,3,4,100]
```python
percentile[1,2,3,4,100]
```

It will return
```bash
>>> percentile 25%: 2.0
percentile 50%: 3.0
percentile 75%: 4.0
percentile 100%: 100.0
```
![See the statitics descriptive video](https://youtu.be/KeDp8Z6tpVo)


Exemple: pecentper (percentile personalized)
The only difference with this pecentper compared to
percentile is that the percentile already returns the quartils,
but pecentper will return based on the last number in the list.

```python
pecentper[1,2,3,4,5,100]
```
The outpul will be:
```bash
100%: 5.0
```

## STATS MENU
Describe Function: This function provides a summary of the dataset, including statistical measures such as mean, median, minimum, maximum, and quartiles. It offers a comprehensive overview of the data's distribution and characteristics.

Info Function: The Info function provides essential information about the dataset, including the data types of each column, memory usage, and non-null counts. It helps users understand the structure and composition of the dataset.

Group By Function: The Group By function automatically detects grouping columns in the dataset upon import. It allows users to aggregate data based on specific columns, providing insights into grouped data analysis.

Sample Function: The Sample function allows users to take a glimpse of the dataset by displaying a sample of rows. It includes sub-functions such as Head and Tail, which show the first or last few rows of the dataset, respectively.

### 6. GUI (Graphical User Interface)
The application has an intuitive graphical interface where you can enter commands and visualize results conveniently.
![Check the video who show about Stats Menu](https://youtu.be/OYjSN5FJio0)

## Requirements

- Tkinter (Graphical interface)
- Sympy (for symbolic calculations)

## Troubleshooting and Solutions

The encountered issue arises when encountering an error indicating 'No module named 'tkinter' on Linux systems. To resolve this, it is recommended to execute the command 
```bash
sudo apt install python3-tk
```
in the terminal. Furthermore, if encountering a different error message stating
```bash
No module named 'the_module
```
It is advised to navigate to the directory containing the setup.py file and execute either
```bash
pip install .
```
or
```bash
python3 -m pip install .
```
to address the missing module dependency.

Make sure to report any issues or bugs you encounter during testing.

## Notes
Ensure you install the required libraries before running the application. You can install them using the command:
```bash
pip install -r requirements.txt
```

### NOTE:
There is one thing, each time you open the program, it will ask where to save the history of the calculations you are doing in MATK.

*This project was developed by Samuel Bidjory.*
