# day care center calculator
# user shouldn't input letters and special character

print("=== Day Care Calculator ===")
num1 = input("Enter a number: ")
ope = str(input("Enter the mathematical operation: "))
num2 = input("Enter a number: ")
'''plus = num1 + num2
minus = num1 - num2
divide = num1 / num2
multiply = num1 * num2'''

if num1.isdigit() and num2.isdigit():
    num1 = float(num1) 
    num2 = float(num2)    
         
    if ope == "+":
        plus = num1 + num2
        print(f"{num1} + {num2} = {plus:.2f}")
    elif ope == "-":
        minus = num1 - num2
        print(f"{num1} - {num2} = {minus:.2f}")
    elif ope == "/":
        divide = num1 / num2
        print(f"{num1} / {num2} = {divide:.2f}")
    elif ope == "*":
        multiply = num1 * num2
        print(f"{num1} * {num2} = {multiply:.2f}")
else:
    print("No input")
else:
    print("Invalid input:: Please input a number")

             