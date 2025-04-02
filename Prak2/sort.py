from my_list import MyList
from list_node import ListNode
import random

listik = MyList()
for i in range(10):
    listik.append(random.randint(1, 100))
print(listik)
listik.sort()
print(listik)
print(len(listik))
