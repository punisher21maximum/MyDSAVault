"""
1. map
"""
k = [1, 2, 3, 4, 5, 6]
k2 = map(lambda x: x ** 2, k)
print(k, list(k2))

"""
2. filter
"""
k = [1, 2, 3, 4, 5, 6]
k2 = filter(lambda x: x % 2 == 0, k)
print(k, list(k2))

"""
3. reduce
"""
import functools

k = [1, 2, 3, 4, 5, 6]
print(functools.reduce(lambda total, current: total + current, k, 100))
