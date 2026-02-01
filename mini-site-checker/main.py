import aiohttp
import asyncio
import time, logging
import functools

headers = {
    "Accept-Encoding": "gzip, deflate"
}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('benchmark')

def benchmark(function):
    @functools.wraps(function)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = await function(*args, **kwargs)
        end = time.perf_counter()
        logger.info(f'time taken by {function.__name__} = {(end-start):.4f}')
        return value
    return wrapper

#create an async function with context manager for automatic setup and teardown (no memeory leaks + concurrent)
@benchmark
async def check(url):
    async with aiohttp.ClientSession() as client:
        async with client.get(url, headers=headers) as response:
            print(f'response status -> {response.status}')
            html = await response.text()
            print(f'site content -> {html[:17].strip()}')

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://docs.python.org"),
    )

asyncio.run(main())
