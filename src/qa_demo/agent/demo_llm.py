from .interfaces import Change, TestCaseDraft

class DemoChangeAnalyzer:
    """Deterministic stand-in for an external LLM."""

    def analyze(self, release_notes: str) -> list[Change]:
        notes = release_notes.lower()
        changes: list[Change] = []

        if "login" in notes or "auth" in notes:
            changes.append(Change("auth", "Authentication flow changed", 5))
        if "profile" in notes:
            changes.append(Change("profile", "Profile behavior changed", 3))
        return changes

class DemoTestPlanGenerator:
    def generate(self, changes: list[Change]) -> list[TestCaseDraft]:
        return [
            TestCaseDraft(
                title=f"Validate critical flow for {change.area}",
                area=change.area,
                expected_result="Behavior matches the release requirement",
                priority=change.business_risk,
            )
            for change in changes
        ]
