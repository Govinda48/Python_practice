class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

class E(D):
    pass

obj = E()
print(E.mro())