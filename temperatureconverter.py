class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def convert_to_fahrenheit(self):
        # Convert Celsius to Fahrenheit using the formula: (Celsius * 9/5) + 32
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit

# Taking input from the user
celsius_temp = float(input("Enter the temperature in Celsius: "))

# Creating an object of the TemperatureConverter class
converter = TemperatureConverter(celsius_temp)

# Calling the convert_to_fahrenheit method to convert the temperature
fahrenheit_temp = converter.convert_to_fahrenheit()

# Displaying the result
print(f"The temperature {celsius_temp} Celsius is equal to {fahrenheit_temp} Fahrenheit.")
