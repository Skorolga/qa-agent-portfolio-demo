from dataclasses import dataclass
from .interfaces import ChangeAnalyzer, TestPlanGenerator, TestCaseDraft

@dataclass(frozen=True)
class PipelineResult:
    generated: tuple[TestCaseDraft, ...]
    automation_candidates: tuple[TestCaseDraft, ...]

class ReleaseTestPipeline:
    def __init__(self, analyzer: ChangeAnalyzer, generator: TestPlanGenerator, automation_threshold: int = 4) -> None:
        self._analyzer = analyzer
        self._generator = generator
        self._automation_threshold = automation_threshold

    def build_plan(self, release_notes: str) -> PipelineResult:
        changes = self._analyzer.analyze(release_notes)
        generated = tuple(self._generator.generate(changes))
        candidates = tuple(case for case in generated if case.priority >= self._automation_threshold)
        return PipelineResult(generated=generated, automation_candidates=candidates)
