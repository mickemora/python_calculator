print("Hi")
#from replit import clear
import art

def execute_operation(operation, first_number, second_nummber):
  if operation == "+":
    return first_number + second_number
  elif operation == "-":
    return first_number - second_number
  elif operation == "*":
    return first_number * second_number
  elif operation == "/":
    return first_number / second_number

new_session            = True

while new_session == True:
  print(art.logo)
  first_round          = True
  continue_calculating = True
  result               = 0
  cummulative          = 0
  
  while continue_calculating:
    if first_round:
      first_number  = float(input("What's the first number? : " ))
      print("+")
      print("-")
      print("*")
      print("/")
      operation     = input("Pick an operation: ")
      second_number = float(input("What's the next number? : " ))
      result        = execute_operation(operation, first_number, second_number)
      cummulative   = result
      print(f"{first_number} {operation} {second_number} = {result}")
    else:
      operation     = input("Pick an operation: ")
      second_number = float(input("What's the next number? : " ))
      result        = execute_operation(operation, cummulative, second_number)
      print(f"{cummulative} {operation} {second_number} = {result}")
      cummulative   = result
    if input(f"Type Y to continue calculating with {result}, or type N to start a new calculation: ").lower() == "y":
      continue_calculating = True
      first_round          = False
    else:
      continue_calculating = False
      #clear()