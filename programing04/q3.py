lower_count = 0
upper_count = 0

def inp(value):
    global lower_count, upper_count  # Use global to modify the variables
    for val in value:
        value[0].upper()
        value[0:]
    
        if val.islower():
            lower_count += 1
        elif val.isupper():
            upper_count += 1
        return value
    

value = input("Enter a string: ")
inp(value)
print(f"There are {lower_count} lowercase and {upper_count} uppercase letters in the string '{value}'.")
print(inp(value))

