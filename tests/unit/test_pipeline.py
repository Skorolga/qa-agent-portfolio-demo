from qa_demo.agent.demo_llm import DemoChangeAnalyzer, DemoTestPlanGenerator
from qa_demo.agent.pipeline import ReleaseTestPipeline

def test_pipeline_selects_only_high_risk_cases_for_automation():
    pipeline = ReleaseTestPipeline(
        analyzer=DemoChangeAnalyzer(),
        generator=DemoTestPlanGenerator(),
        automation_threshold=4,
    )

    result = pipeline.build_plan("Changed login flow and updated profile page")

    assert len(result.generated) == 2
    assert [case.area for case in result.automation_candidates] == ["auth"]
