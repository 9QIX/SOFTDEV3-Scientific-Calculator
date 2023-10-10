import sympy as sp


def calculator():
    print("Python Calculator")

    while True:
        print("-" * 50)
        print("Enter a mathematical expression or 'quit' to exit.")
        print("-" * 50)

        expression = input(">>> ")

        if expression.lower() == 'quit':
            print("Exiting calculator.")
            break

        try:
            result = sp.sympify(expression)
            if isinstance(result, sp.Basic):
                # If the result is a symbolic expression, evaluate it numerically
                result = float(result)

            print("-" * 50)
            print("Result:", result)
        except (ValueError, sp.SympifyError):
            print("-" * 50)
            print("Invalid input. Please enter a valid expression.")


if __name__ == "__main__":
    calculator()
