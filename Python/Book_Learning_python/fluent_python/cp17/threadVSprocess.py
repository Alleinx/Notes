import concurrent.futures
import time

number_list = [i for i in range(100)]

def count(number):
    result = 0
    for i in range(0, 1000000):
        result += i
    
    return result * number

if __name__ == "__main__":
    # Sequential execution
    start_time = time.time()
    for item in number_list:
        count(item)
    
    print('Sequential execution in ' + str(time.time() - start_time), 'seconds.')

    #ThreadPoolExecutor:
    #Restricted by GIL.
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(count, number_list)

    print('Thread pool execution in ' + str(time.time() - start_time), 'seconds.')

    #ProcessPoolExecutor:
    #Not restricted by GIL.
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(count, number_list)
    
    print('Process pool execution in ' + str(time.time() - start_time), 'seconds.')
