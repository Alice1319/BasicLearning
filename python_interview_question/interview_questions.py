# 1.1行代碼實現1-100之和
#print(sum(range(101)))

# 2.如何在函數內部修改全局變量
a = 100
def foo1():
    print("foo1" + "-"*50)
    global a 
    a = 200
    print(a)

def foo2():
    print("foo2" + "-"*50)
    print(a)

foo1()
foo2()
print("Done.")
