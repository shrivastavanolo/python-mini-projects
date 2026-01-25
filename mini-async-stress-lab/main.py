from fastapi import FastAPI
import aiohttp
import time
import logging
import functools
from typing import Callable
import asyncio
import inspect

app = FastAPI()
logging.basicConfig(level=logging.INFO)

def get_benchmark(func):
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Callable:
            logging.info(f'Function {func.__name__} has started.')
            start_time = time.perf_counter()
            value = await func(*args, **kwargs)
            end_time = time.perf_counter()
            logging.info(f'Function {func.__name__} has executed and took a time of {end_time - start_time:.4f}s.')

            return value
        
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            logging.info(f'Function {func.__name__} has started.')
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            logging.info(f'Function {func.__name__} has executed and took a time of {end_time - start_time:.4f}s.')

            return value
    return wrapper

@app.get("/sync")
@get_benchmark
def get_poke():
    time.sleep(5)
    print("this is sync funtion")

@app.get("/async")
@get_benchmark
async def get_async_poke():
    await asyncio.sleep(5)
    print("this is async function")

