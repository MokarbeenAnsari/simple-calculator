class SimpleCalculator:
    def add(self, x, y):
        """Add two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtract two numbers."""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y

    def divide(self, x, y):
        """Divide two numbers."""
        if y == 0:
            print("Cannot divide by zero.")
            return None
        return x / y

    def display_menu(self):
        """Display the calculator operation menu."""
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

    def main(self):
        """Main calculator loop."""
        self.display_menu()

        choice = input("Enter the number of your choice (1, 2, 3, or 4): ")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print(f"The result of adding {num1} and {num2} is: {self.add(num1, num2)}")
        elif choice == "2":
            print(f"The result of subtracting {num1} and {num2} is: {self.subtract(num1, num2)}")
        elif choice == "3":
            print(f"The result of multiplying {num1} and {num2} is: {self.multiply(num1, num2)}")
        elif choice == "4":
            result = self.divide(num1, num2)
            if result is not None:
                print(f"The result of dividing {num1} and {num2} is: {result}")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    calculator = SimpleCalculator()
    calculator.main()
