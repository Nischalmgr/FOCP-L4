def celcius_fer(celsius):
     fahrenheit = (9/5) * celsius + 32
     return fahrenheit
list=[]
for x in range (1,7):
     input_=input("enter celcus with 'c'")
     if input_[-1].upper()!='C':
        print("enter c also")
     else:
       value=float(input_[:-1])
       list.append(value)

       fer=celcius_fer(value)
       print(f"{value} C is equal to {fer} F")

if list:
    print(f"maximum: {max(list)} , minimum: {min(list)}, mean: {sum(list)/len(list)}")
else:
    print("no data added")
    
