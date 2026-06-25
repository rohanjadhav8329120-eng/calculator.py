print("This is my first calculator")
num1 = int(input("Enter you'r First Number: "))
num2 = int(input("Enter you'r Second Number: "))

operations = input("Select you'r operations: '+', '-', '*', '/'  ")
if operations == '+':
    print(num1 + num2)
elif operations == '-':
    print(num1 - num2)
elif operations == '*':
    print(num1 * num2)
elif operations == '/':
    print(num1 / num2)
else: 
    print("Please Select Valid Operations")