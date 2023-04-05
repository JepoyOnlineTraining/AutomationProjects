import sys
sys.path.append("C:/Training/SeleniumPython/Day 9/packageA")
sys.path.append("C:/Training/SeleniumPython/Day 9/packageB")

# Approach 1

# import emp
# import stu
#
# empobj= emp.Employee(eid=123, ename="Geo", sal=100)
# empobj.displayemp()
#
# stuobj = stu.Student(sid=123, sname="Jann", grade=1)
# stuobj.displaystu()


# Approach 2

from emp import Employee
from stu import Student

empobj = Employee(eid=123, ename="Geo", sal=100)
empobj.displayemp()

stuobj = Student(sid=123, sname="Jann", grade=1)
stuobj.displaystu()