from abc import ABC

import aiohttp
from fake_headers import Headers


class WebSite(ABC):
    headers = Headers(headers=True).generate()

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_response(self, request_url: str, *args, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(request_url, headers=self.headers) as resp:
                return await resp.json()

    async def send_post(self, request_url: str, *args, data: dict = {}, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(request_url, data=data) as response:
                try:
                    data = await response.json(encoding="utf-8")
                    return data
                except:
                    return await response.text()
