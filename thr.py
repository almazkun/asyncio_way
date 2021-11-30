import time
from tempfile import TemporaryDirectory
from secrets import token_urlsafe
import os
import threading
from queue import Queue


CONTENT_SIZE = 1
HUNDRED_THOUSAND = 10 ** 5


def write_file(path):
    p = os.path.join(path, f"{token_urlsafe(64)}.txt")
    c = token_urlsafe(CONTENT_SIZE)
    with open(p, "w+") as f:
        time.sleep(1)
        f.write(c)
        print(p)


def do_job(jobs):
    while not jobs.empty():
        job = jobs.get()
        write_file(job)
        jobs.task_done()


def write_threaded(size):
    p = "/tmp/thr"
    os.makedirs(p, exist_ok=True)
    jobs = Queue()

    for i in range(size):
        jobs.put(p)

    for i in range(1000):
        worker = threading.Thread(target=do_job, args=(jobs,))
        worker.start()
    return jobs


if __name__ == "__main__":
    start = time.time()
    n = HUNDRED_THOUSAND // 100
    write_threaded(n).join()
    end = time.time()
    print(f"Threaded: {n} files in {end - start:.2f} seconds")
