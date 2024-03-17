#num1= int(input("Enter your fisrt number"))
#num2=int(input("Enter your second number"))
#sum = num1 + num2
#print("the sum of the your two numbers is", sum)
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Creating an object of the Calculator class
calculator = Calculator(num1, num2)

# Calling the add method to perform addition
result = calculator.add()

# Displaying the result
print("The sum of", num1, "and", num2, "is:", result)
