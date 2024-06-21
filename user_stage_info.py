from typing import List

from .stage_info import StageInfo
from .duration_info import DurationInfo
from .goal_info import GoalInfo
from .view_info import ViewInfo


class UserStageInfo:
    stage_info: StageInfo
    duration: DurationInfo
    goal_info: GoalInfo
    view_info: List[ViewInfo]