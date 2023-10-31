import asyncio
import time
import aiohttp
import requests

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def download_with_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses

def download_with_requests(urls):
    responses = []
    for url in urls:
        response = requests.get(url)
        responses.append(response.text)
    return responses

if __name__ == '__main__':
    urls = ["https://jsonplaceholder.typicode.com/users"] * 100

    start_time = time.time()
    asyncio.run(download_with_async(urls))
    async_time = time.time() - start_time

    start_time = time.time()
    download_with_requests(urls)
    sync_time = time.time() - start_time

    print(f"Aсинхронное время: {async_time} сек.")
    print(f"Синхронное время: {sync_time} сек.")
