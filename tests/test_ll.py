import sys
import os

path = os.getcwd()
sys.path.insert(0, "/Users/ritvarun/Development/Python/pystl/pystl_v2")

from structures.lists.ll import LinkedList

ll = LinkedList([1,2,3,4,5,6,7,8,9,10])

for item in ll:
    print(item)

ll.pop()
ll.pop(0)

for item in ll:
    print(item)
