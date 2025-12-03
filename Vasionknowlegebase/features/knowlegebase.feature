Feature: Vasion Print Documentation
    As an IT administrator
    I want to be able to find documentation on helping me troubleshoot and configure my instance
    So I can troubleshoot on my own

Scenario: Access the knowledge base homepage
    Given I open the url "https://kb.printerlogic.com/s/knowledge-base"
    Then I expect that the url is "https://kb.printerlogic.com/s/knowledge-base"
    And I expect that the title is "Knowledge Base"
    And I expect a new window has not been opened

# The following search input tests are commented out because the search input field
# does not render properly in headless mode (used by GitHub Actions CI)

# Scenario: Search is blank
#     Given I open the url "https://kb.printerlogic.com/s/knowledge-base" and wait
#     Then I wait and expect that element "input" is visible
#     Then I wait and expect that element "input" is empty

# Scenario: Search for printer documentation
#     Given I open the url "https://kb.printerlogic.com/s/knowledge-base" and wait
#     When I wait and set "printer" to the inputfield "input.search-input"
#     And I pause for 3000ms
#     Then I expect that element "input.search-input" contains the text "printer"

# Scenario: Search and submit query
#     Given I open the url "https://kb.printerlogic.com/s/knowledge-base" and wait
#     When I wait and set "printer" to the inputfield "input.search-input"
#     And I press "Enter"
#     And I pause for 3000ms
#     Then I expect that the url is "https://kb.printerlogic.com/s/KnowledgeBase/printer"

# Scenario: Search brings results
#     Given I open the url "https://kb.printerlogic.com/s/knowledge-base" and wait
#     When I wait and set "push trust" to the inputfield "input.search-input"
#     And I press "Enter"
#     And I pause for 3000ms
#     Then I expect that element "body" contains the text "push trust"

Scenario: Administrator Console quick suggestions brings correct results
    Given I open the url "https://kb.printerlogic.com/s/knowledge-base"
    And I pause for 3000ms
    When I click on the link "Administrator Console"
    And I pause for 3000ms
    Then I expect that element "body" contains the text "Admin"

Scenario: Self Service Portal quick suggestions brings correct results
    Given I open the url "https://kb.printerlogic.com/s/knowledge-base"
    And I pause for 3000ms
    When I click on the link "Self-Service Portal"
    And I pause for 3000ms
    Then I expect that element "body" contains the text "Self-Service Portal"

Scenario: Server quick suggestions brings correct results
    Given I open the url "https://kb.printerlogic.com/s/knowledge-base"
    And I pause for 3000ms
    When I click on the link "Server"
    And I pause for 3000ms
    Then I expect that element "body" contains the text "Server"

Scenario: PrinterLogic WebStack quick suggestions brings correct results
    Given I open the url "https://kb.printerlogic.com/s/knowledge-base"
    And I pause for 3000ms
    When I click on the link "PrinterLogic Web Stack"
    And I pause for 3000ms
    Then I expect that element "body" contains the text "Web Stack"


Scenario: Vasion quick suggestions brings correct results
    Given I open the url "https://kb.printerlogic.com/s/knowledge-base"
    And I pause for 3000ms
    When I click on the link "Vasion"
    And I pause for 3000ms
    Then I expect that element "body" contains the text "Vasion"