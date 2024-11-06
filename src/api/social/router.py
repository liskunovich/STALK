from fastapi import APIRouter

from src.services.social.leetcode import LeetCode
from src.services.social.stepik import StepikCertificates, StepikActivities
from src.services.social.codeforces import CodeForces
from src.services.social.github import Github
from .schemas.codeforces import CodeforcesResponse
from .schemas.stepik import (
    StepikActivitiesResponseModel,
    StepikCertificatesResponseModel,
)
from .schemas.leetcode import LeetCodeResponseModel
from .schemas.github import GitHubUserResponseModel, UserRepositoriesResponseModel

social_router = APIRouter()


@social_router.get("/codeforce")
async def get_codeforce(username: str) -> CodeforcesResponse:
    return await CodeForces().get_response(username)


@social_router.get("/stepik-activities")
async def get_stepik_activities(user_id: str) -> StepikActivitiesResponseModel:
    return await StepikActivities().get_response(user_id)


@social_router.get("/stepik-certificates")
async def get_stepik_certificates(user_id: str) -> StepikCertificatesResponseModel:
    return await StepikCertificates().get_response(user_id)


@social_router.get("/leetcode")
async def get_leetcode(username: str) -> LeetCodeResponseModel:
    return await LeetCode().get_response(username)


@social_router.get("/github-user")
async def get_github(username: str) -> GitHubUserResponseModel:
    return await Github().get_user(username)


@social_router.get("/github-user-repos")
async def get_github_repos(username: str) -> UserRepositoriesResponseModel:
    return await Github().get_user_repos(username)
