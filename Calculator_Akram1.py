# BUILDING A SIMPLE CALCULATOR IN PYTHON BY MR. AKRAM | ICE | BHT | MATRICULATION: 945097

# Selecting operation by a user

print("Select an operation to perform: ")   # Select which an operation want to get by calculator

print("1. ADD")                             # To adding numbers
print("2. SUBTRACT")                        # To Subtracting numbers
print("3. MULTIPLY")                        # To Multiplying numbers
print("4. DIVIDE")                          # To Diving numbers

operation = input()                         # To get user input

if operation == "1":                                                    # To add numbers
    Number1 = input("Insert the first number: ")                        # To get first input from user
    Number2 = input("Insert the second number: ")                       # To get second input from user
    print("The result (ADD) is: " + str(int(Number1) + int(Number2)))   # Perform operation and convert inputs to int

elif operation == "2":                                                  # To subtract numbers
    Number1 = input("Insert the first number: ")                        # To get first input from user
    Number2 = input("Insert the second number: ")                       # To get second input from user
    print("The result (SUB) is: " + str(int(Number1) - int(Number2)))   # Perform operation and convert inputs to int

elif operation == "3":                                                  # To subtract numbers
    Number1 = input("Insert the first number: ")                        # To get first input from user
    Number2 = input("Insert the second number: ")                       # To get second input from user
    print("The result (MUL) is: " + str(int(Number1) * int(Number2)))   # Perform operation and convert inputs to int

elif operation == "4":                                                  # To subtract numbers
    Number1 = input("Insert the first number: ")                        # To get first input from user
    Number2 = input("Insert the second number: ")                       # To get second input from user
    print("The result (DIV) is: " + str(int(Number1) / int(Number2)))   # Perform operation and convert inputs to int

else:
    print ("Sorry, invalid input!")




