''' Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

def test(num):
    factor=[]
    for x in range(1,num+1):
        if num%x==0:
            factor.append(x)
    return factor
num= int(input ("enter a number to find its factors"))
print(f"the factors of {num} are {test(num)}")


