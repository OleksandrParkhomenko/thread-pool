from thread_pool import ThreadPool


def example_func(a, b):
    print(a + b)


pool = ThreadPool(5)
pool.submit(example_func, 2, *(1, 1))
pool.submit(example_func, 3, 1, 2)
pool.submit(example_func, 1, 1, 0)
pool.submit(example_func, 4, 1, 3)
pool.submit(example_func, 5, 1, 4)
pool.submit(example_func, 1, 1, 5)

pool.wait_to_complete()
