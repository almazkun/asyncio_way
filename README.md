# asyncio_way
Way to asyncio world

# Asyncio and requests
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
]


def get_url(url: str) -> None:
    s = time()
    try:
        print(f"\t{url}: {requests.get(url).status_code} in {(time()-s):.2f}")
    except Exception as e:
        print(f"\t{url}: Error: {str(e)[:10]} {(time()-s):.2f}")


async def all_urls(url_list: url_list, executor: ThreadPoolExecutor) -> None:
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(executor, get_url, url) for url in url_list]
    await asyncio.gather(*futures)


if __name__ == "__main__":
    print("Start")
    s = time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(all_urls(url_list, executor))
    print(f"Total time: {(time()-s):.2f}")
```
```bash
Start
	https://pper.men: Error: HTTPSConne 0.02
	https://akun.dev: 200 in 0.94
	https://zangerka.kz: 200 in 1.17
	https://anya.kr: 200 in 1.22
	https://yelena.kim: 200 in 1.43
	https://focuskeeper.app: 200 in 1.72
	https://law-protection.kz: 200 in 2.06
	https://finlaw.kz: 200 in 2.65
Total time: 2.66
```
