import sys
import os

path = os.getcwd()
sys.path.insert(0, "/Users/ritvarun/Development/Python/pystl/pystl_v2")

from structures.trees.avlt import AVLTree

ll = AVLTree([10,5,22,6,3,18,91,18,12,4,2,1])

for item in ll:
    print(item)

# ll.push(-100)
# ll.push(87)
# ll.push(100)
# ll.pop(0)
# ll.pop(-100)
# print("-"*100)
# for item in ll:
#     print(item)

print("Len : ", len(ll))
