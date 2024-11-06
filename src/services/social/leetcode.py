from .base import WebSite


class LeetCode(WebSite):
    def __init__(self):
        super().__init__("https://leetcode-stats-api.herokuapp.com/")

    async def get_response(self, username: str, *args, **kwargs):
        return await super().get_response(self.base_url + username, *args, **kwargs)
