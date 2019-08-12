import threading, queue, time

# The worker thread gets jobs off the queue. When the queue is empty,
# it assumes there will be no more work and exits.

def worker():
    print('Running worker')
    # let the thread distributer init other thread
    time.sleep(0.1)
    while True:
        try:
            arg = q.get(block=False)
        except queue.Empty:
            print('Worker', threading.currentThread(), end= ' ')
            print('queue empty.')
            break
        else:
            print('Worker', threading.currentThread(), end = ' ')
            print('running with argument', arg)
            time.sleep(0.5)

q = queue.Queue()

# start pool of 5 workers
for i in range(5):
    t = threading.Thread(target=worker, name='worker {index}'.format(index=i+1))
    t.start()

# begin adding work to the queue
for i in range(50):
    q.put(i)

print('Main Thread sleeping...')
time.sleep(5)