from .base import WebSite


class CodeForces(WebSite):
    def __init__(self):
        super().__init__("https://codeforces.com/api/user.info?handles=")

    async def get_response(self, username: str, *args, **kwargs):
        return await super().get_response(self.base_url + username, *args, **kwargs)
