import asyncio, aiohttp

headers = {
    "Accept-Encoding": "gzip, deflate"
}

class AsyncSession:
    def __init__(self, url):
        self.url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self.url, headers=headers)
        return response
    
    async def __aexit__(self, exc_type, exc_value, exc_tb):
        if isinstance(exc_type, Exception):
            print(f"Exception: {exc_type}")
            return True
        await self.session.close()

async def check_url(url):
    async with AsyncSession(url) as response:
        print(f"Status -> {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check_url("https://realpython.com"),
        check_url("https://pycoders.com")  
    )

asyncio.run(main())