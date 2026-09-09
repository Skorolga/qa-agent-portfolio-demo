from dataclasses import dataclass
from enum import Enum

class FailureKind(str, Enum):
    PRODUCT = "product_defect"
    TEST = "test_issue"
    ENVIRONMENT = "environment_issue"
    UNKNOWN = "unknown"

@dataclass(frozen=True)
class Failure:
    test_name: str
    message: str

def classify_failure(failure: Failure) -> FailureKind:
    message = failure.message.lower()
    if "connection refused" in message or "timeout connecting" in message:
        return FailureKind.ENVIRONMENT
    if "locator" in message or "element not found" in message:
        return FailureKind.TEST
    if "expected status 200" in message and "got 500" in message:
        return FailureKind.PRODUCT
    return FailureKind.UNKNOWN
