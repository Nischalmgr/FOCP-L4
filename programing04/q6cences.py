def celcius_fer(celsius):
     fahrenheit = (9/5) * celsius + 32
     return fahrenheit
input_=input("enter celcus with 'c'")
if input_[-1].upper()!='C':
     print("enter c also")
else:
     value=float(input_[:-1])
     fer=celcius_fer(value)
     print(f"{value} C is equal to {fer} F")
