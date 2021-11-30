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
    n = HUNDRED_THOUSAND // 10
    write_sequent(n)
    end = time.time()
    print(f"Sequential: {n} files in {end - start:.2f} seconds")
