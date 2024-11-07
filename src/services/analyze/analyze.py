from src.services.social.base import WebSite
from src.api.social.schemas.analyze import CandidateProfile, CandidateSocials
from openai import OpenAI
from src.utils.env_file import Environment
import json
from openai import OpenAI


class Analyzator(WebSite):
    def __init__(self):
        super().__init__("https://chatgpt.com/")
        self.env = Environment()
        self.client = OpenAI(
            api_key=self.env.env("API_GPT_KEY"),  # Replace with your OpenAI API key
        )

    async def analyze_cv(self, cv) -> CandidateProfile:
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
        )
