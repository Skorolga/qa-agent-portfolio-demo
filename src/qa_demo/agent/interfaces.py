from dataclasses import dataclass
from typing import Protocol, Sequence

@dataclass(frozen=True)
class Change:
    area: str
    description: str
    business_risk: int

@dataclass(frozen=True)
class TestCaseDraft:
    title: str
    area: str
    expected_result: str
    priority: int

class ChangeAnalyzer(Protocol):
    def analyze(self, release_notes: str) -> Sequence[Change]:
        ...

class TestPlanGenerator(Protocol):
    def generate(self, changes: Sequence[Change]) -> Sequence[TestCaseDraft]:
        ...
