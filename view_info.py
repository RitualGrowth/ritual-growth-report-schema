from .goal_info import GoalInfo
from .date_time_info import DateTimeInfo
from .visit_info import VisitInfo
from typing import List


class ViewInfo:
    view: str
    visits: List[VisitInfo]
    overall_duration: DateTimeInfo
    goal_info: GoalInfo