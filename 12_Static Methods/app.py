# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    

celsius = 24
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"celsius {celsius}°C is equal to fahrenheit {fahrenheit}°F")