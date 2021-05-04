import html5lib
import aiohttp
from bs4 import BeautifulSoup
async def get_topic():
    url="https://www.conversationstarters.com/generator.php"
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            output=await r.read()
            soup = BeautifulSoup(output, 'html5lib')
            topics=soup.find("div", {"id": "random"})
            return topics.contents[1]



