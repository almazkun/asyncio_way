# asyncio_way
Way to asyncio world

# Threads vd Processes
    * Threads are small components of the program that can be run in parallel.
    * Processes are the collection of threads that can be run in parallel.

# IO blocking and CPU blocking
    * IO blocking: When CPU is waiting
        * Call to the storage (read/write to disk)
        * Call to DB (read/write to DB)
        * Call to network (request/response to network)
    * CPU blocking: When CPU is busy thinking
        * When a program is waiting for a long-running operation to finish, it is blocking.

# Threads for IO blocking
    * Threads are used to run IO blocking operations.

# Processes for CPU blocking
    * Processes are used to run CPU blocking operations.

# Examples
## Sequential:
```py
import time
from tempfile import TemporaryDirectory
from secrets import token_urlsafe
import os


CONTENT_SIZE = 1
HUNDRED_THOUSAND = 10 ** 5


def write_file(path):
    p = os.path.join(path, f"{token_urlsafe(64)}.txt")
    c = token_urlsafe(CONTENT_SIZE)
    with open(p, "w+") as f:
        f.write(c)


def write_sequent(size):
    p = "/tmp/seq"
    os.makedirs(p, exist_ok=True)
    for i in range(size):
        write_file(p)


if __name__ == "__main__":
    start = time.time()
    n = HUNDRED_THOUSAND
    write_sequent(n)
    end = time.time()
    print(f"Sequential: {n} files in {end - start:.2f} seconds")

```
```bash
Sequential: 100000 files in 22.07 seconds
```


## Threaded:
```py   
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
        f.write(c)

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
    
    for i in range(100):
        worker = threading.Thread(target=do_job, args=(jobs,))
        worker.start()
    return jobs

if __name__ == "__main__":
    start = time.time()
    n = HUNDRED_THOUSAND
    write_threaded(n).join()
    end = time.time()
    print(f"Threaded: {n} files in {end - start:.2f} seconds")
```
```bash
Threaded: 100000 files in 18.66 seconds
```

## Processes:
```py
```
```bash
```

## Visiting many sites:
```py
import asyncio
import concurrent.futures
from time import time

import requests


url_list = [
    "https://akun.dev",
    "https://anya.kr",
    "https://yelena.kim",
    "https://finlaw.kz",
    "https://focuskeeper.app",
    "https://law-protection.kz",
    "https://pper.men",
    "https://zangerka.kz",
] * 10


def get_url(url: str) -> None:
    s = time()
    try:
        print(f"\t{url}: {requests.get(url).status_code} in {(time()-s):.2f}")
    except Exception as e:
        print(f"\t{url}: Error: {str(e)[:10]} {(time()-s):.2f}")


async def all_urls(url_list: url_list, executor) -> None:
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(executor, get_url, url) for url in url_list]
    await asyncio.gather(*futures)


if __name__ == "__main__":
    print("Start")
    s = time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(all_urls(url_list, executor))
    print(f"Total time: {len(url_list)} sites in {(time()-s):.2f}")
```
```bash
Total time: 80 sites in 2.64
```
