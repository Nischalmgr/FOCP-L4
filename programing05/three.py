import sys
argvar=sys.argv[1:]
print(argvar)
print(sorted(argvar))
sortvar=sorted(argvar,key=len)
print(sortvar)

