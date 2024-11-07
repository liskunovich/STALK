from src.services.social.base import WebSite
from src.api.social.schemas.analyze import CandidateProfile, CandidateSocials
from src.services.social.leetcode import LeetCode
from src.services.social.github import Github
from src.services.social.stepik import StepikCertificates, StepikActivities
from src.services.social.codeforces import CodeForces
from openai import OpenAI
from src.utils.env_file import Environment
import json


class Analyzator(WebSite):
    def __init__(self):
        super().__init__("https://chatgpt.com/")
        self.env = Environment()
        self.cv = None
        self.client = OpenAI(
            api_key=self.env.env("API_GPT_KEY"),  # Replace with your OpenAI API key
        )

    async def parse_socials(self):
        candidate_profile = CandidateSocials()

        if self.cv.socials.leetcode is not None:
            leetcode = await LeetCode().get_response(self.cv.socials.leetcode)
        if self.cv.socials.codeforces is not None:
            codeforces = await CodeForces().get_response(self.cv.socials.codeforces)
        if self.cv.socials.github is not None:
            github = await Github().get_user(self.cv.socials.github)
        if self.cv.socials.stepik is not None:
            stepik = await StepikCertificates().get_response(self.cv.socials.stepik)

        if self.cv.socials.leetcode is not None and leetcode.get("status") == "success":
            candidate_profile.leetcode = (
                "https://leetcode.com/" + self.cv.socials.leetcode
            )
        if self.cv.socials.codeforces is not None and codeforces.get("status") == "OK":
            candidate_profile.codeforces = (
                "https://codeforces.com/profile/" + self.cv.socials.codeforces
            )
        if self.cv.socials.github is not None and github.get("status") != "404":
            candidate_profile.github = "https://github.com/" + self.cv.socials.github

        if self.cv.socials.stepik is not None and stepik.get("certificates"):
            candidate_profile.stepik = (
                "https://stepik.org/user/" + self.cv.socials.stepik
            )
        return candidate_profile

    async def analyze_cv(self, cv) -> CandidateProfile:
        self.cv = cv
        candidate_socials = await self.parse_socials()

        f = open(self.env.env("TUNE_GPT"))
        gpt_Tune = f.read()
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": gpt_Tune + cv.vacancy},
                {"role": "user", "content": cv.cv},
            ],
        )
        json_string = response.choices[0].message.content
        json_string = json_string.replace("json", "")
        json_string = json_string.replace("```", "")

        data = json.loads(json_string)
        return CandidateProfile(
            salaryTop=data[0]["salaryTop"],
            salary=data[0]["salary"],
            salaryDown=data[0]["salaryDown"],
            rating=data[0]["rating"],
            comment=data[0]["comment"],
            commentToSkillPositive=data[0]["commentToScillPositive"],
            commentToSkillNegative=data[0]["commentToScillNegative"],
            recommend=data[0]["recomend"],
            recommended_position=data[0]["recommended_position"],
            socials=candidate_socials,
        )
