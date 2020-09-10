# 作用域

if(1 >0):
    a = 10
    print("if a:", a)
    print("if a id:", id(a))

print("a:", a)
print("a id:", id(a))


def f1():
    b = 20
    print("f1 b:", b)
    print("f1 b id:", id(b))
f1()
# print("b:", b) 报错访问不到b

c = 30
print("c:", c)
print("c id:", id(c))
def f2():
    c = 33  #局部变量
    print('f2 c:', c)
    print("f2 c id:", id(c))

f2()
