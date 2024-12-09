def valid(number, answer=True):
    if number>=0 and number<=100:
        return answer
    else:
        return not answer
number=int(input("enter number"))
result=valid(number)
print(result)
    


