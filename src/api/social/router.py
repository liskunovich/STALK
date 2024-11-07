from fastapi import APIRouter, HTTPException

from src.services.social.leetcode import LeetCode
from src.services.social.stepik import StepikCertificates, StepikActivities
from src.services.social.codeforces import CodeForces
from src.services.social.github import Github
from src.services.analyze.analyze import Analyzator

from .schemas.codeforces import CodeforcesResponse
from .schemas.stepik import (
    StepikActivitiesResponseModel,
    StepikCertificatesResponseModel,
)
from .schemas.leetcode import LeetCodeResponseModel
from .schemas.github import GitHubUserResponseModel, UserRepositoriesResponseModel
from .schemas.analyze import CandidateProfile, CandidateCV


social_router = APIRouter()


@social_router.get("/codeforce")
async def get_codeforce(username: str) -> CodeforcesResponse:
    response = await CodeForces().get_response(username)
    if response.get("status") == "OK":
        return response
    raise HTTPException(status_code=404, detail="User not found")


@social_router.get("/stepik-activities")
async def get_stepik_activities(user_id: str) -> StepikActivitiesResponseModel:
    return await StepikActivities().get_response(user_id)


@social_router.get("/stepik-certificates")
async def get_stepik_certificates(user_id: str) -> StepikCertificatesResponseModel:
    return await StepikCertificates().get_response(user_id)


@social_router.get("/leetcode")
async def get_leetcode(username: str) -> LeetCodeResponseModel:
    response = await LeetCode().get_response(username)
    if response.get("status") == "success":
        return response
    raise HTTPException(status_code=404, detail="User not found")


@social_router.get("/github-user")
async def get_github(username: str) -> GitHubUserResponseModel:
    response = await Github().get_user(username)
    if response.get("status") != "404":
        return response
    raise HTTPException(status_code=404, detail="User not found")


@social_router.get("/github-user-repos")
async def get_github_repos(username: str) -> UserRepositoriesResponseModel:
    response = await Github().get_user_repos(username)
    if response.get("status") != "404":
        return response
    raise HTTPException(status_code=404, detail="User not found")


@social_router.post("/analyze-cv/")
async def analyze_cv(cv: CandidateCV) -> CandidateProfile:
    return await Analyzator().analyze_cv(cv)
