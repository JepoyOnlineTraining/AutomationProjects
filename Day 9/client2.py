# from package1.module1 import *
# from package1.package2.module2 import *
#
# display()
# show()

# Approach1
import sys
sys.path.append("C:/Training/SeleniumPython/Day 9/package1")
sys.path.append("C:/Training/SeleniumPython/Day 9/package1/package2")
# import module1
# import module2
#
# module1.display()
# module2.show()


# Approach2
from module1 import *
from module2 import *

display()
show()
