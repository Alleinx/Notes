from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 10

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    
    return cc

def download_many(cc_list):
    workers_amount = min(MAX_WORKERS, len(cc_list))

    with futures.ThreadPoolExecutor(workers_amount) as executor:
        res = executor.map(download_one, sorted(cc_list))
        # executor.map(func, iterable)
        # Perform func on each item in iterable.
    # ThreadPoolExecutor.__exit__ will be called:
    # which will call executor.shutdown(wait=True), which will be hung up before all threads finish their
    # job.
    return len(list(res))

if __name__ == "__main__":
    main(download_many)