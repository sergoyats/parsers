# import aiohttp
# import asyncio
# from src.utils import read_links_txt
#
# links = read_links_txt('../input/images_links.txt')
#
#
# async def get(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, ssl=False) as response:
#             return response.status
#
# loop = asyncio.get_event_loop()
# tasks = [get(link) for link in links]
# results = loop.run_until_complete(asyncio.gather(*tasks))
# print("Results: %s" % results)

import os
import pathlib
import aiohttp
import aiofiles
import asyncio
from src.utils import read_links_txt, get_file_name_from_url

links = read_links_txt('../input/images_links.txt')
img_dir = '../img/async'

pathlib.Path(img_dir).mkdir(parents=True, exist_ok=True)


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            f = await aiofiles.open(os.path.join(img_dir, get_file_name_from_url(url)), mode='wb')
            await f.write(await response.read())
            await f.close()

loop = asyncio.get_event_loop()
tasks = [download(link) for link in links]
loop.run_until_complete(asyncio.gather(*tasks))
