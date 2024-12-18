#immutable
# bracket not req
info="test", 2,3
print(type(info))
name,count,data=info
print(count)
print(name)
def myfun(name,a,b):
    print(b)
mod=1,2,3
myfun(*mod)
a=(1)
b=(1,)
print(f"a{type(a)}, b{type(b)}")