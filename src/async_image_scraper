import os
import pathlib
import re
import aiohttp
import aiofiles
import asyncio
from src.utils import get_file_name_from_url

page_url = 'http://komotoz.ru/photo/priroda/pejzazhy_prirody.php'
img_dir = '../img/async'

pathlib.Path(img_dir).mkdir(parents=True, exist_ok=True)


async def parse_images(page_url):
    response = await aiohttp.request('GET', page_url)
    url = re.findall('img .*?src="(.*?)"', response)
    
    async def download(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                f = await aiofiles.open(os.path.join(img_dir, get_file_name_from_url(url)), mode='wb')
                await f.write(await response.read())
                await f.close()
    
    result = [download(link) for link in url]
    return result


loop = asyncio.get_event_loop()
tasks = parse_images(page_url)
loop.run_until_complete(asyncio.gather(*tasks))
