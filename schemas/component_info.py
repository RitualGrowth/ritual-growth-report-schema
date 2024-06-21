from .date_time_info import DateTimeInfo
from .common import ComponentType

class ComponentInfo:
    duration: DateTimeInfo
    component_type: ComponentType
    component_id: str
    action: str
    next_view: str