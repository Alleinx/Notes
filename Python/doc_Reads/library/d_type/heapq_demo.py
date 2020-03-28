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
    times = 20

    # Indicate the priority of task
    priority = [random.randint(0, 2) for _ in range(times)]
    # Indicate the enqueue order of the task.
    enqueue_order = [i for i in range(times)]
    # Indicate the task itself
    task = ['task' for _ in range(times)]

    task_list = zip(priority, enqueue_order, task)

    print(task_list)
    # Construct a heap:
    # heapq.heapify(h)
    # print(h)
    # print('Smallest Value:', h[0])

    # Perform heapsort:
    result = heapsort(task_list)
    print('Results After heapsort', result)
    # Get the largest value of the heap
