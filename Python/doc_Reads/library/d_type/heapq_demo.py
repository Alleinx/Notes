# This is a program demonstrate the usage of heapq built-in lib.

import heapq
import random
import collections.abc

def heapsort(h: collections.abc.Iterable):
    # Version1:
    result_heap = []
    for item in h:
        heapq.heappush(result_heap, item)
    # Version2:
    # result_heap = h[:]
    # heapq.heapify(result_heap)

    return [heapq.heappop(result_heap) for _ in range(len(result_heap))]

if __name__ == '__main__':
    times = 15
    h = [random.randint(0, 100) for _ in range(times)]
    print(h)
    # Construct a heap:
    heapq.heapify(h)
    print(h)

    print('Smallest Value:', h[0])

    # Perform heapsort:
    result = heapsort(h)
    print('Results After heapsort', result)
    # Get the largest value of the heap
