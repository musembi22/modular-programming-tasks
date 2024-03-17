# x = int(input("Enter a number:"))

#if x%2 == 0:
 #print ( x, "is an even number.")

#else :
 #print ( x, "is an odd number.")
class NumberChecker:
    def __init__(self, number):
        self.number = number

    def check_even_odd(self):
        if self.number % 2 == 0:
            return "even"
        else:
            return "odd"

# Taking input from the user
num = int(input("Enter a number: "))

# Creating an object of the NumberChecker class
checker = NumberChecker(num)

# Calling the check_even_odd method to determine if the number is even or odd
result = checker.check_even_odd()

# Displaying the result
print(f"The number {num} is {result}.")
