from pydantic import BaseModel, HttpUrl
from typing import List


class CodeforcesUser(BaseModel):
    contribution: int
    lastOnlineTimeSeconds: int
    friendOfCount: int
    titlePhoto: HttpUrl
    handle: str
    avatar: HttpUrl
    registrationTimeSeconds: int


class CodeforcesResponse(BaseModel):
    status: str
    result: List[CodeforcesUser]
