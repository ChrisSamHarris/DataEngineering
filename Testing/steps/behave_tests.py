# Run via 'cd Testing && behave'

# Output:
# Feature: Testing the incrementor # features/test.feature:7

#   Scenario: Test increasing a number  # features/test.feature:8
#     Given a new incrementor of size 5 # steps/behave_tests.py:7 0.000s
#     When we increment 10              # steps/behave_tests.py:11 0.000s
#     Then we should see 15             # steps/behave_tests.py:15 0.000s

#   Scenario: Test decreasing a number   # features/test.feature:13
#     Given a new incrementor of size -2 # steps/behave_tests.py:7 0.000s
#     When we increment 20               # steps/behave_tests.py:11 0.000s
#     Then we should see 18              # steps/behave_tests.py:15 0.000s

#   Scenario: Test doing nothing to a number  # features/test.feature:18
#     Given a new incrementor of size 0       # steps/behave_tests.py:7 0.000s
#     When we increment 15                    # steps/behave_tests.py:11 0.000s
#     Then we should see 15                   # steps/behave_tests.py:15 0.000s

# 1 feature passed, 0 failed, 0 skipped
# 3 scenarios passed, 0 failed, 0 skipped
# 9 steps passed, 0 failed, 0 skipped, 0 undefined
# Took 0m0.001s


from behave import Given, When, Then 
from main import incrementor

@Given("a new incrementor of size {stride}")
def given_incrementor(context, stride: str):
    context.incrementor = incrementor(int(stride))
    
@When("we increment {num}")
def when_increment(context, num: str):
    context.results = context.incrementor(int(num))
    
@Then("we should see {results}")
def then_results(context, results: str):
    assert(context.results == int(results))