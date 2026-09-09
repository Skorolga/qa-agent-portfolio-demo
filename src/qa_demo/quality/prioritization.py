from dataclasses import dataclass

@dataclass(frozen=True)
class Scenario:
    name: str
    business_risk: int
    execution_frequency: int
    manual_cost: int
    automation_cost: int

def automation_score(scenario: Scenario) -> float:
    denominator = max(scenario.automation_cost, 1)
    return scenario.business_risk * scenario.execution_frequency * scenario.manual_cost / denominator
