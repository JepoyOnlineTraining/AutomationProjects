# # Example1
#
# class A:
#
#     def m1(self):
#         print("this is m1 from class A")
#
#
# class B(A):
#     def m2(self):
#         print("this is m2 from class B")
#
#
# b = B()
# b.m1() # method from class A
# b.m2()
# a = A()
# a.m1()


# # Example2: single inheritance
#
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# b = B()
# b.m1()
# b.m2()

# # Example3: Multiple inheritance
#
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# c = C()
# c.m1()
# c.m2()
# c.m3()

# # Example4: Hierarchy inheritance
#
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
# bobj = B()
# bobj.m2()
# bobj.m1()
#
# cobj = C()
# cobj.m1()
# cobj.m3()

# # Example5:
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B:
#     a, b = 300, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A, B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# cobj= C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# # Example6:Overriding
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 from class B")
#         super().m1()
#
# bobj = B()
# bobj.m1()

# # Example7
#
# class A:
#
#     a, b = 10, 20
#
# class B(A):
#
#     i, j = 100, 200
#     def m(self, x, y):
#         print(x + y)
#         print(self.i + self.j)
#         print(self.a + self.b)
#
#
# bobj = B()
# bobj.m(1, 2)


# # Example8: overriding variables
#
# class Parent:
#     name = "Scott"
#
#
# class Child(Parent):
#     name = "John"
#
#
# cobj = Child()
# print(cobj.name)


# # Example9: Overriding methods
#
# class Bank:
#     def rateOfIntereset(self):
#         return 0
#
#
# class XBank(Bank):
#     def rateOfIntereset(self):
#         return 10
#
#
# class YBank(Bank):
#     def rateOfIntereset(self):
#         return 12
#
#
# bank = YBank()
# print(bank.rateOfIntereset())

# Example10: Polymorphism can be implemented overloading concept

 
