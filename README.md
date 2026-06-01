# Python Calculator

This repository contains a simple command-line calculator built in Python.

The program allows a user to perform basic arithmetic operations, continue calculating with the previous result, or start a new calculation session.

## Project Overview

This project is a beginner-friendly Python exercise focused on basic program structure, functions, user input, arithmetic operations, and loop-based control flow.

The calculator supports the following operations:

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`

The application also displays a calculator-themed ASCII art logo when a new calculation session begins.

## Main Objective

The objective of this project is to practice foundational Python programming concepts by creating an interactive command-line calculator.

The project demonstrates how to:

- Define and call functions
- Use conditional statements
- Capture user input
- Convert input to numeric values
- Perform arithmetic operations
- Use nested loops
- Continue calculations using a previous result
- Organize display assets in a separate file

## Repository Structure

```text
.
├── main.py
├── art.py
└── README.md
```

## Technologies Used

- Python

No external libraries are required.

## File Descriptions

### `main.py`

This is the main application file.

It imports the ASCII logo from `art.py`:

```python
import art
```

It defines the main calculation function:

```python
def execute_operation(operation, first_number, second_nummber):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
```

The application then runs through an interactive loop that:

1. Prints the calculator logo
2. Prompts for the first number
3. Displays available operations
4. Prompts for an operation
5. Prompts for the second number
6. Calculates the result
7. Asks whether the user wants to continue calculating with the previous result

### `art.py`

This file stores the calculator ASCII art logo in a variable named `logo`.

The logo is printed at the beginning of a new calculation session.

## How the Program Works

The calculator starts a new session and displays the logo.

The user is asked to enter the first number:

```text
What's the first number? :
```

The program then displays the supported operators:

```text
+
-
*
/
```

The user selects an operation and enters the next number.

The calculator performs the selected operation and displays the result:

```text
5.0 + 3.0 = 8.0
```

The user is then asked whether they want to continue calculating with the current result:

```text
Type Y to continue calculating with 8.0, or type N to start a new calculation:
```

If the user enters `Y`, the calculator uses the previous result as the first number for the next operation.

If the user enters `N`, the current calculation session ends.

## Program Flow

```text
Start calculator
    ↓
Display logo
    ↓
Ask for first number
    ↓
Display available operations
    ↓
Ask for operation
    ↓
Ask for next number
    ↓
Execute selected operation
    ↓
Display result
    ↓
Continue with current result?
    → Yes: use result as next starting number
    → No: end current calculation session
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/mickemora/python_calculator.git
```

2. Navigate into the project directory:

```bash
cd python_calculator
```

3. Run the application:

```bash
python main.py
```

Depending on your environment, you may need to use:

```bash
python3 main.py
```

## Example Interaction

```text
What's the first number? : 10
+
-
*
/
Pick an operation: *
What's the next number? : 5
10.0 * 5.0 = 50.0
Type Y to continue calculating with 50.0, or type N to start a new calculation: y
Pick an operation: -
What's the next number? : 20
50.0 - 20.0 = 30.0
```

## Key Programming Concepts Demonstrated

This project demonstrates several core Python concepts:

- Functions
- Function parameters
- Return values
- Conditional logic
- User input
- Type conversion with `float()`
- Arithmetic operations
- Boolean variables
- While loops
- Nested loops
- State management using previous results
- Importing from another Python file
- Multi-line strings for ASCII art

## Known Issues / Improvement Opportunities

The current code is a learning exercise and contains a few areas that could be improved:

- The function parameter is named `second_nummber`, but the function body uses `second_number`.
- Invalid operators are not currently handled.
- Division by zero is not currently handled.
- Non-numeric input is not currently validated.
- The calculator does not fully restart a new session after choosing `N` because the outer session loop remains active without resetting through a clear user path.
- The commented `clear()` function suggests the project may have originally been designed for Replit.

## Potential Enhancements

Future improvements could include:

- Fix the `second_nummber` typo
- Add input validation for numbers and operators
- Add division-by-zero handling
- Refactor operation logic into a dictionary of functions
- Add a clear screen function
- Add automated tests
- Add support for exponentiation
- Add support for square root or percentage calculations
- Add a history of calculations
- Package the calculator as a reusable module

## Summary

This project is a simple Python command-line calculator. It is useful for practicing functions, control flow, arithmetic operations, user input, loops, and basic state management through continued calculations using the previous result.
