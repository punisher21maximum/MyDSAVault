"""
1. Counters

input - iterator
output - dict, keys as eles, values as frequency of eles
         sorted, dec frequency

Counter - is a class, we pass iterator, it returns the dict
          as object.
        - has functions like, 
            - most_common()
                input - for how many eles
                output - list of tuples [('e', 4), ('a', 3)]
"""
from collections import Counter

str1 = "aaabbbccdeeee"
list1 = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4]
# print(Counter(str1))
# print(Counter(str1).most_common(2))
# print(Counter(str1).most_common(2)[0][0])  # most common ele
# print(Counter(list1))


"""
2. namedtuple

Similar to struct
"""
from collections import namedtuple

Point = namedtuple("Point2", "x, y")
pt1 = Point(1, -4)
# print(pt1, pt1.x, pt1.y)

"""
3. OrderedDict

Since Py 3.7 dict is ordered by default
"""

from collections import OrderedDict

"""
4. deque
"""
from collections import deque

dq = deque()

dq.append(1)
dq.appendleft(2)
# print(dq)

dq.pop()
dq.popleft()

dq.extend([4, 5, 6])
dq.extendleft([3, 2, 1])

# print(dq)

# Rotate

print(dq)
# dq.rotate(2)
dq.rotate(-1)
print(dq)
