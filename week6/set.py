# set1={}
# set1={1,2,3,4,5,6,7,8,9,True,1}
# print(set1)
# print(11 in set1)
# set2={1,2}
# set3={2,3,4}
# print(set1)
# print(set1 | set3)
# print(set1 & set3)
# print( set1-set3)
# for i in set2:
    # print(i)
# set5=set("aeiou")
# print(type(set5))
# set7={}
# print(type(set7))
# print({set({chr(x) for x in range(ord("a"), ord("z")+1)})})
# freeset={"a", "b"}

# new=frozenset(freeset)
# print(type(new))
#  subset < > 
word={1,2,3,4,5,6}
word2={9,20}
word3={11,12}
print(word.update(word2))
word |= word3
print(word)
#.add()/.pop()
#discard no exceptipon remove exception