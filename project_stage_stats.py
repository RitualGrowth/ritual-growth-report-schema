from datetime import datetime
from .stages import Stages
from .overall_status import OverallStatus

class ProjectStageStats:
    project_id: str
    cohort_id: str
    stage_id: str
    start_date: datetime
    end_date: datetime
    duration: float
    number_of_users: int
    total_entered: int
    total_early_exit: int
    total_completed: int
    percentage_completed: float
    status: OverallStatus
    stages: Stages