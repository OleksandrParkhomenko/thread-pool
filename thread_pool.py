from threading import Thread
from queue import Queue
from time import sleep


class Worker(Thread):
    def __init__(self, jobs):
        Thread.__init__(self)
        self.jobs = jobs
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, delay, args = self.jobs.get()
            try:
                sleep(delay)
                func(*args)
            except Exception as e:
                print(e)
            finally:
                self.jobs.task_done()


class ThreadPool:
    def __init__(self, num_of_threads):
        self.jobs = Queue(num_of_threads)
        for _ in range(num_of_threads):
            Worker(self.jobs)

    def submit(self, job, delay, *args):
        self.jobs.put((job, delay, args))

    def wait_to_complete(self):
        self.jobs.join()

