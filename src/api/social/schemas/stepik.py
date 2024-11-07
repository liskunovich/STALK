from typing import List, Optional, Union
from pydantic import BaseModel
from datetime import datetime


class MetaModel(BaseModel):
    page: int
    has_next: bool
    has_previous: bool


class UserActivitySummaryModel(BaseModel):
    id: int
    recent_strike: int
    solved_today: int
    max_strike: int
    solved: int
    days: int
    pins: List[int]


class StepikActivitiesResponseModel(BaseModel):
    meta: MetaModel
    user_activity_summaries: Optional[List[UserActivitySummaryModel]] = None


class CertificateModel(BaseModel):
    id: int
    user: int
    course: int
    issue_date: datetime
    update_date: Optional[datetime] = None
    grade: int
    type: str
    url: str
    preview_url: str
    is_public: bool
    user_rank: Optional[int] = None
    user_rank_max: Optional[int] = None
    leaderboard_size: Optional[int] = None
    saved_fullname: str
    edits_count: int
    allowed_edits_count: int
    course_title: str
    course_title_en: str
    course_is_public: bool
    course_language: str
    is_with_score: bool


class StepikCertificatesResponseModel(BaseModel):
    meta: MetaModel
    certificates: List[CertificateModel]
