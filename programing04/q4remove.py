def test(value):
    if len(value) > 1 :
        value= value[:-1]
        return value
    else :
        return value
value=input ("enter a value :")
print(test(value))