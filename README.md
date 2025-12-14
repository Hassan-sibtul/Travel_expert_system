# Travel Recommender Expert System

Rule-based expert system that recommends travel destinations using 40+ weighted rules across budget, climate, travel styles, seasonality, continent, trip length, and visa ease.

## Features
- 22 destinations with detailed attributes (cost, climate, styles, best months, visa ease, trip length)
- 40 rules, including specialized compound rules (safari season, ski winter, winter-sun beach, northern lights, food+culture, city shoulder season, surf, etc.)
- Forward-chaining scorer with explainable reasoning steps
- Interactive CLI questionnaire
- Built-in automated test suite (10 scenarios) with documented results

## Quick Start
```
python travel_expert_system.py
```
Follow the prompts; the system prints top-5 destinations with scores and key reasoning steps.

## Run the Test Suite
Uncomment the last line in `travel_expert_system.py`:
```
# run_all_tests()
```
Then run:
```
python travel_expert_system.py
```
Test outputs (all 10 scenarios) are also captured in `test_results.txt`.

## Key Files
- `travel_expert_system.py` — knowledge base, rules, inference, CLI, tests
- `test_results.txt` — recorded outputs of all 10 test scenarios
- `TESTING_EVIDENCE.md` — testing and rule refinement narrative
- `ASSIGNMENT_COMPLETION_CHECKLIST.md` — requirement coverage summary
- `README.md` — this file

## Dependencies
- Python 3.11+ (standard library only; no external packages)

## Notes
- Scoring is additive; all matching rules fire and contribute to the final ranking.
- Explanations list the rules that fired so users can see why destinations were recommended.
