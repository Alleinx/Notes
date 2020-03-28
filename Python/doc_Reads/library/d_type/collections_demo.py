import collections

deq = collections.deque()
deq.extend([i for i in range (10)])

print(deq)
deq.popleft()
print(deq)
deq.pop()
deq.appendleft('p')
print(deq)
deq.insert(100, -1)
