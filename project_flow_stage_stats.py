from datetime import datetime
from typing import List
from .common import Status
from .flow import Flow

class ProjectFlowStageStats:
    project_id: str
    start_date: datetime
    end_date: datetime
    duration: float
    number_of_cohorts: int
    status: Status
    flows_run: List[Flow]