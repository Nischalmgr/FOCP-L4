data=[1, 3, 3, 4]
print(data.reverse())
#mutator ko none value return
data.pop()
cop=data.copy()
print(data.count(2))
del cop
print(cop)

print((i*j for i in range (10) for j in range (10)))
