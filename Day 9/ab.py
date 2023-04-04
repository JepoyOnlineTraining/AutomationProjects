# # Approach1
# import a
# import b
#
# obj1 = a.Animal()
# obj1.display()
#
# obj2 = b.Bird()
# obj2.display()

# Approach2

from a import Animal
from b import Bird

obj1 = Animal()
obj2 = Bird()

obj1.display()
obj2.display()

Animal().display()
Bird().display()
