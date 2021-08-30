from dataclasses import dataclass
from enum import Enum


class Type(Enum):
    BILLABLE = "BILLABLE"
    NOT_BILLABLE = "NOT_BILLABLE"


@dataclass
class Claim:
    id: int
    merchant_name: str
    type: Type
    total: float
