from src.services.social.base import WebSite
from src.api.social.schemas.analyze import CandidateProfile, CandidateSocials


class Analyzator(WebSite):
    def __init__(self):
        super().__init__("https://chatgpt.com/")

    async def analyze_cv(self) -> CandidateProfile:
        return CandidateProfile(
            salaryTop=0,
            salary=0,
            salaryDown=0,
            rating=0,
            comment="",
            commentToSkillPositive="",
            commentToSkillNegative="",
            recommend="",
            recommended_position="",
            socials=CandidateSocials(),
        )
