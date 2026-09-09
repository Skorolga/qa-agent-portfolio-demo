from qa_demo.quality.prioritization import Scenario, automation_score

def test_high_risk_frequent_scenario_gets_higher_score():
    critical = Scenario("payment", 5, 5, 4, 2)
    cosmetic = Scenario("avatar", 1, 1, 1, 3)

    assert automation_score(critical) > automation_score(cosmetic)
