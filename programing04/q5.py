def celsius_to_fahrenheit(celsius):
  
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
   
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

 
celsius_value = float(input("Enter temperature in Celsius: "))
fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
 
converted_fahrenheit = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value}°C is equal to {converted_fahrenheit}°F.")

 
converted_celsius = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value}°F is equal to {converted_celsius}°C.")
