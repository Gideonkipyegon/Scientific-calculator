import math

def scientific_calculator():
    print("Welcome to Scientific Calculator!")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Trigonometric Functions")
    print("8. Exit")

    while True:
        choice = int(input("Enter operation number: "))

        if choice == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 + num2)
        elif choice == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 - num2)
        elif choice == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", num1 * num2)
        elif choice == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero!")
        elif choice == 5:
            num = float(input("Enter number: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", math.pow(num, exponent))
        elif choice == 6:
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))
        elif choice == 7:
            angle = float(input("Enter angle in degrees: "))
            print("Sin:", math.sin(math.radians(angle)))
            print("Cos:", math.cos(math.radians(angle)))
            print("Tan:", math.tan(math.radians(angle)))
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid operation number.")

scientific_calculator()
