from .common import Status
from typing import List
from .cohort_info import CohortInfo
from .goal_info import GoalInfo
from .user_stage_info import UserStageInfo
from .screen import Screen
from .group_statistics_info import GroupStatisticsInfo


class CohortStageStats:
    cohort_info: CohortInfo
    duration: float
    stage_status: Status
    goal_info = GoalInfo
    group_statistics_info = GroupStatisticsInfo
    user_stage_info = UserStageInfo
    screens = List[Screen]