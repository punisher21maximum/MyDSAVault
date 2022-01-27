import heapq

# 1
h = [5, 7, 9, 1, 3]

heapq.heapify(h)

# 2
heapq.heappush(h, 4)

# 3
heapq.heappop(h)

# 4
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, h))

print(heapq.nsmallest(3, h))


# max heap
'''
By default Min Heap is implemented by this class. But we multiply each value by -1 so that we can use it as MaxHeap.
heappush(heap, -1 * 10)
heapop(heap) * -1
'''
