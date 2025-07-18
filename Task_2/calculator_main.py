from calculator import Calculator

while True:

    def calc():     
        print("Welcome to the calculator!")
        print("Choose an operation:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")

        choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                return
            
            calculate = Calculator(num1,num2)

            if choice == '1':
                print(f"{num1} + {num2} = {calculate.add()}")
            elif choice == '2':
                print(f"{num1} - {num2} = {calculate.subtract()}")
            elif choice == '3':
                print(f"{num1} * {num2} = {calculate.multiply()}")
            elif choice == '4':
                result = calculate.divide()
                if isinstance(result, str):
                    print(result)  # Prints error message
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4).")

    # Usage
    if __name__ == "__main__":
        calc()

