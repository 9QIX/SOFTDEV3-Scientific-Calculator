import sympy as sp


def scientific_calculator():
    print(" ______________________________________________________________________")
    print("|  _______   _______   _______   _______   _______   _______   _______  |")
    print("| |       | |       | |       | |       | |       | |       | |       | |")
    print("| |   7   | |   8   | |   9   | |  (+)  | |  (-)  | |  (*)  | |  (/)  | |")
    print("| |_______| |_______| |_______| |_______| |_______| |_______| |_______| |")
    print("| |       | |       | |       | |       | |       | |       | |       | |")
    print("| |   4   | |   5   | |   6   | | (sin) | | (cos) | | (tan) | | (log) | |")
    print("| |_______| |_______| |_______| |_______| |_______| |_______| |_______| |")
    print("| |       | |       | |       | |       | |       | |       | |       | |")
    print("| |   1   | |   2   | |   3   | | (asin)| | (acos)| | (atan)| | (exp) | |")
    print("| |_______| |_______| |_______| |_______| |_______| |_______| |_______| |")
    print("| |       | |       | |       | |       | |       | |       | |       | |")
    print("| |   0   | |   .   | |   =   | | (sqrt)| |  (^)  | |  (ln) | |(log10)| |")
    print("| |_______| |_______| |_______| |_______| |_______| |_______| |_______| |")
    print("|_______________________________________________________________________|")

    while True:
        print("-" * 76)
        print("Enter a mathematical expression or 'quit' to exit.")
        print("-" * 76)

        expression = input(">>> ")

        if expression.lower() == 'quit':
            print("Exiting calculator.")
            break

        try:
            result = sp.sympify(expression)
            if isinstance(result, sp.Basic):
                # If the result is a symbolic expression, evaluate it numerically
                result = float(result)

            if isinstance(result, complex):
                # If the result is a complex number, display it as a string
                print("-" * 76)
                print("Result:", str(result))
            else:
                print("-" * 76)
                print("Result:", result)
        except (ValueError, sp.SympifyError):
            print("-" * 76)
            print("Invalid input. Please enter a valid expression.")
        except ZeroDivisionError:
            print("-" * 76)
            print("Division by zero is not allowed.")
        except Exception as e:
            print("-" * 76)
            print("Syntax Error")
        # except Exception as e:
        #     print("-" * 76)
        #     print("An error occurred:", str(e))


if __name__ == "__main__":
    scientific_calculator()
