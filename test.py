def func5(a):
    print("in func5 a = ", a)
    b = 100 + a
    d = 2 * a
    print("in func5 b = ", b)
    print("in func5 d = ", d)
    print("in func5 c = ", c)
    return b + 10
          
a = 10
b = 15
c = 25
c = func5(b) 
# 
print("a = ", a)
print("b = ", b) 
print("c = ", c) 
# a = 10
# b = 110
# d = 20 

#print("d = ", d) # d is not defined