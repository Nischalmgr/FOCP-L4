'''Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''
def is_prime(num):
    if num <= 1:   
        return False
    for i in range(2, int(num)):  
        if num % i == 0:   
            return False
    return True

 
num = int(input("Enter a number to check if it's prime: "))

 
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
