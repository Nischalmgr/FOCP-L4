#key value 
#key is not mutable but value is mutable
# key  must be diff but value may be same
#is ordered
# dict1={"name": "hari", "age":17}
# print(dict1)
# dict2=dict({"name": "hari", "age":17})
# print(type(dict2))
# print(dict2)

# stoct=dict([("apple",10,),("bana",12)])
# print (stoct)
# dictcomperehension={x: x**3 for x   in range (2,8)}
# print(dictcomperehension)
# print(dict1["name"])
# for i in dict1.values():
#     print(i)
# for i in dict1.values():
#     print(i)
# for key , values in dict2.items():
#     print(key,values)
# print(dict2.items())
# print(dict2.values())
# print(dict2.keys())
# for i, (key,values) in enumerate(dict2.items()):
#     print(i, key, values)
def age(name,age):
    print(name,age)
detail={"name":"hello", "age":13}
age(**detail)
def rev(**detail):
    print(detail)
rev(**detail)
#touple string, int , any thing can be keys
lang_gen = { "Java":3, "Assembly":2, "Machine Code":1 }
print(("Assembly" in lang_gen))