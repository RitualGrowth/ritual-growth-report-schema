from datetime import datetime
from .component_info import ComponentInfo
from typing import List

class VisitInfo:
    component_info: List[ComponentInfo]
    duration: datetime