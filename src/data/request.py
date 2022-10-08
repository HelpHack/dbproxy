from enum import Enum

class RequestStatus(Enum):
    NEW = 0,
    ONGOING = 1,
    COMPLETED = 2,
    CANCELLED = 3
