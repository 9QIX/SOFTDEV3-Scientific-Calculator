# Scientific Calculator Documentation

Welcome to the documentation for the Scientific Calculator CLI. This documentation will guide you on how to use the calculator and provide a comprehensive explanation of the code, line by line and function by function.

## Table of Contents

- [Scientific Calculator Documentation](#scientific-calculator-documentation)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [Example Usage](#example-usage)
  - [Code Explanation](#code-explanation)
    - [Imports](#imports)
    - [math_functions Dictionary](#math_functions-dictionary)
    - [is_valid_expression Function](#is_valid_expression-function)
    - [evaluate_expression Function](#evaluate_expression-function)
    - [degrees_to_radians Function](#degrees_to_radians-function)
    - [main Function](#main-function)

## Usage

To use the Scientific Calculator, follow these steps:

1. Clone the GitHub repository to your local machine:

   ```bash
   git clone https://github.com/9QIX/SOFTDEV3ScientificCalculator
   ```

2. Navigate to the project directory:

   ```bash
   cd SOFTDEV3ScientificCalculator
   ```

3. Run the calculator:

   ```bash
   python main.py
   ```

4. You will be prompted to enter a mathematical expression. Type your expression and press Enter to see the result. Enter 'q' to quit the calculator.

### Example Usage

```bash
Welcome to Scientific Calculator CLI
Enter a mathematical expression (q to quit): sin(pi/2)
Result: 1.0
```

## Code Explanation

Let's go through the code, explaining each part, line by line, and function by function.

### Imports

```python
import math
```

- This line imports the Python `math` module, which provides mathematical functions like sine, cosine, and more.

### math_functions Dictionary

```python
math_functions = {
    'sin': lambda x: math.sin(degrees_to_radians(x)),
    'cos': lambda x: math.cos(degrees_to_radians(x)),
    'tan': lambda x: math.tan(degrees_to_radians(x)),
    'log': math.log,
    'sqrt': math.sqrt,
    'pi': math.pi,
    'exp': math.exp,
    'factorial': math.factorial
}
```

- Here, we create a dictionary called `math_functions` that maps mathematical function names to their corresponding functions from the `math` module. This allows us to evaluate expressions that use these functions.

### is_valid_expression Function

```python
def is_valid_expression(expression):
    valid_chars = "0123456789+-*/()., "
    return all(char in valid_chars for char in expression)
```

- The `is_valid_expression` function checks if a given expression contains only valid characters. It returns `True` if all characters are valid and `False` otherwise.

### evaluate_expression Function

```python
def evaluate_expression(expression):
    try:
        return eval(expression, {'__builtins__': None}, math_functions)
    except (SyntaxError, NameError, ZeroDivisionError, ValueError):
        return None
```

- The `evaluate_expression` function takes an expression as input and attempts to evaluate it using Python's `eval` function. It restricts access to built-in functions by passing `{'__builtins__': None}` and provides access to the `math_functions` dictionary. It catches and handles potential errors such as syntax errors, name errors, zero division, and value errors.

### degrees_to_radians Function

```python
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)
```

- The `degrees_to_radians` function converts degrees to radians. It's used to allow trigonometric functions to accept angle values in degrees.

### main Function

```python
def main():
    print("Welcome to Scientific Calculator CLI")
    while True:
        expression = input("Enter a mathematical expression (q to quit): ")
        if expression.lower() == 'q':
            break

        if is_valid_expression(expression):
            result = evaluate_expression(expression)
            if result is not None:
                print("Result:", result)
            else:
                print("Invalid calculation error. Please try again.")
        else:
            print("Invalid input. Please enter a valid mathematical expression.")
```

- The `main` function is the entry point of the program. It displays a welcome message and enters a loop to repeatedly prompt the user for mathematical expressions. It also handles the 'q' option to quit the calculator.
