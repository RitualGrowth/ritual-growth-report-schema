from .common import GoalType
from typing import Union
from .target_info_absolute import TargetInfoAbsolute
from .target_info_absolute import TargetInfoPercentage

class GoalInfo:
    goal_name: str
    goal_type: GoalType
    target: Union[TargetInfoAbsolute, TargetInfoPercentage]