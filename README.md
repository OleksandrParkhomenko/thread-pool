# Thread Pool implementation

Implementing a thread pool class that accepts a function with a delay after which this function should be executed.

## Example:

```
pool = ThreadPool(num_of_threads)
pool.submit(some_func, delay, *args)
```
