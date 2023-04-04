# # Example 1
# class MyClass:
#
#     def myfunc(self):
#         pass
#
#     def display(self, name):
#         print(name)
#
#
# mc1 = MyClass()
# mc1.myfunc()
# mc1.display("Jann Geo")

# # Example 2 - Static Method
#
# class MyClass:
#
#     def m1(self):
#         print()
#
#     @staticmethod
#     def m2(self, num):
#         print(self, num)
#
#
# MyClass.m2(1, 3)

# # Example 3
#
# class MyClass:
#     a, b = 10, 20
#
#     def add(self):
#         print(self.a, self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
#
# mc = MyClass()
# mc.add()
# mc.mul()

# # Example 4
# i, j = 12, 25
# class MyClass:
#     a, b = 10, 20
#
#     def add(self, x, y):
#         print(x + y)
#         print(self.a + self.b)
#         print(i + j)

# # Example 5
#
# a, b = 15, 25
#
# class MyClass:
#     a, b = 10, 20
#     def add(self, a, b):
#         print(a + b)
#         print(self.a + self.b)
#         print(globals()['a'] + globals()['b'])
#
#
# mc = MyClass()
# mc.add(1, 3)


# # Example 6 : One class can have multiple objects
#
# class MyClass:
#
#     def display(self, name):
#         print("This is display method")
#         print("Hi", name)
#
#
# obj1 = MyClass()
# obj1.display("Jack")
# obj2 = MyClass()
# obj2.display("Clearance")
#
# # Example 7
# class MyClass:
#
#     def __init__(self):
#         print("this is constructor")
#
#     def m1(self):
#         print("Hello...")
#
#
# mc = MyClass()


# # Example 8
#
# class MyClass:
#     name = "john"
#
#     def __init__(self, name):
#         print(name)
#         print(self.name)
#
# mc = MyClass("Jann")

# Example 9

class Emp:

    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def print_eid(self):
        print(self.eid)

    def print_ename(self):
        print(self.ename)

    def print_sal(self):
        print(self.sal)


emp1 = Emp(123, "jann", "20")
emp2 = Emp(132, "geo", "10")

emp1.print_sal()
emp1.print_ename()
emp1.print_sal()


