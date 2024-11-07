from typing import Optional
from pydantic import BaseModel


class CandidateSocials(BaseModel):
    leetcode: Optional[str] = None
    codeforces: Optional[str] = None
    github: Optional[str] = None
    stepik: Optional[str] = None


class CandidateCV(BaseModel):
    vacancy: str
    cv: str
    socials: CandidateSocials


class CandidateProfile(BaseModel):
    salaryTop: int
    salary: int
    salaryDown: int
    rating: int
    comment: str
    commentToSkillPositive: str
    commentToSkillNegative: str
    recommend: str
    recommended_position: str
