# Text file that describes software features and their test scenarios using plain language. Typical breakdown:
# * Feature description 
# * Background 
# * Scenarios -> Given, When, Then 
# Installed VSCode Extension: Cucumber (Gherkin) Full Support | v2.15.2

Feature: Testing the incrementor
    Scenario: Test increasing a number 
        Given a new incrementor of size 5 
        When we increment 10
        Then we should see 15 

    Scenario: Test decreasing a number 
        Given a new incrementor of size -2
        When we increment 20
        Then we should see 18 

    Scenario: Test doing nothing to a number 
        Given a new incrementor of size 0
        When we increment 15 
        Then we should see 15