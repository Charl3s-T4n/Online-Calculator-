from replit import clear     # so that i can clear the output in console 
from art import logo

def add(n1, n2):                            # CREATING FUNCTIONS for calculator 
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def multi(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2 
  
operations = {'+' : add, '-' : sub, '*' : multi, '/' : div}          # Key-value pair for operations of calculator 

def calculator():            # Create calculator function ( so i can use RECURSION )
  print(logo)
  first_number = float(input("What is your first number?: "))   # Needs to be float so that won't have error if user pass in a value with decimal 

  flag_variable_first = False      # Create first flag variable

  while not flag_variable_first:      # while True:
    for operation_symbol in operations:            # Loop through the keys of the dict
      print(operation_symbol)                # Print the symbol for user to choose
    operation_symbol_chosen = input("Pick an operation from the line above: ")
    second_number = float(input("What is your next number?: "))  # Needs to be float so that won't have error if user pass in a value with decimal 
    operation_function = operations[operation_symbol_chosen]                          # operation_functoin will be add/sub/multi/div
    answer = operation_function(n1=first_number, n2=second_number)
    print(f"{first_number} {operation_symbol_chosen} {second_number} = {answer}")
    continue_calculating = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start new calculation.: ")
    if continue_calculating == 'y':
      first_number = answer              # first number will be the answer from the previous equation, while second number will be the next number user will input 
      flag_variable_first = False      # While loop continue 
    elif continue_calculating == 'n':      
      flag_variable_first = True       # Stop while loop
      clear()                     # Clear output in console 
      calculator()           # Call back the function which restarts the calculator  ( RECURSION ) 
    
calculator()         # calling the calculator function which starts it 
 

