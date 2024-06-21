from enum import Enum

class Status(Enum):
    PASS = "pass"
    FAIL = "fail"
    IN_PROGRESS = "in_progress"
    CANCELED = "canceled"
    
class ComponentType(Enum):
    BUTTON = "button"
    RADIO_BUTTON = "radio_button"
    LINK = "link"
    
class GoalType(Enum):
    PERCENTAGE = "percentage"
    ABSOLUTE = "absolute"
