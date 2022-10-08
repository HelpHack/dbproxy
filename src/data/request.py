from enum import Enum

class RequestStatus(Enum):
    NEW = 'New',
    ONGOING = 'Ongoing',
    COMPLETED = 'Completed',
    CANCELLED = 'Cancelled'
