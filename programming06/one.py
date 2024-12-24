''' Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!'''
def change(num):
    binary=""
    while num > 0:
        rem=num%2
        binary=binary+str(rem)
        num=num//2
    binary_="".join(reversed(binary))
    return binary_
num= int(input ("enter a number to change into binary"))
print(f"{num} binary is {change(num)}")
    


