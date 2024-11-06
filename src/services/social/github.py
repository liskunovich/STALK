from .base import WebSite


class Github(WebSite):
    def __init__(self):
        super().__init__("https://api.github.com/users/")

    async def get_response(self, username: str = "", *args, **kwargs):
        return await super().get_response(self.base_url + username, *args, **kwargs)

    async def get_user(self, username: str, *args, **kwargs):
        return await self.get_response(username, *args, **kwargs)

    async def get_user_repos(self, username: str, *args, **kwargs):
        return await self.get_response(username + "/repos", *args, **kwargs)
