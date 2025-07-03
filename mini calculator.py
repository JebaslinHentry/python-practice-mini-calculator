#Mini calculator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
user_choice = input("Choose an operation (add, subtract, multiply, divide): ")
if user_choice == "add":
    print("The sum is:", a + b)
elif user_choice == "subtract":
    print("The difference is:", a - b)
elif user_choice == "multiply":
    print("The product is:", a * b)
elif user_choice == "divide":
    print("The quotient is:", a / b)
else:
    print("Invalid operation")
