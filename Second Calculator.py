# My second calculator

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

def division(a,b):
    if b!=0:
        return a/b
    else:
        return "cannot divide by zero"

def multiplication(a,b):
    return a * b 

print("1.Addition")
print("2.Subtract")
print("3.Division")
print("4.Multiplication")

choice=input("Choose operation:")

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if choice == "1":
    print(add(num1,num2))
elif choice == "2":
    print(subtract(num1,num2))
elif choice == "3":
    print(division(num1,num2))
elif choice == "4":
    print(multiplication(num1,num2))
else:
    print("Invalid choice")