import time
from tempfile import TemporaryDirectory
from secrets import token_urlsafe
import os
from concurrent.futures import ProcessPoolExecutor


CONTENT_SIZE = 1
HUNDRED_THOUSAND = 10 ** 5


def write_file(path):
    p = os.path.join(path, f"{token_urlsafe(64)}.txt")
    c = token_urlsafe(CONTENT_SIZE)
    with open(p, "w+") as f:
        f.write(c)
    return "done"


def write_processed(size):
    p = "/tmp/prs"
    os.makedirs(p, exist_ok=True)

    with ProcessPoolExecutor(max_workers=10) as executor:
        for arg, res in zip(range(size), executor.map(write_file, p, chunksize=2)):
            pass
        return "done"


if __name__ == "__main__":
    start = time.time()
    n = HUNDRED_THOUSAND // 10
    write_processed(n)
    end = time.time()
    print(f"Processed: {n} files in {end - start:.2f} seconds")
