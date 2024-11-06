from .base import WebSite


class StepikCertificates(WebSite):
    def __init__(self):
        super().__init__("https://stepik.org/api/certificates?order=-id&page=1&user=")

    async def get_response(self, username: str, *args, **kwargs):
        return await super().get_response(self.base_url + username, *args, **kwargs)


class StepikActivities(WebSite):
    def __init__(self):
        super().__init__("https://stepik.org/api/user-activity-summaries/")

    async def get_response(self, username: str, *args, **kwargs):
        return await super().get_response(self.base_url + username, *args, **kwargs)
