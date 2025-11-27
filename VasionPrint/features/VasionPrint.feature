Feature: Vasion Print Basic Printer functionality
    As an IT administrator
    I want to be able to create printers that my users will be able to install without having to use Printer servers
    So I can lessen cost and make it easier

Scenario: Login to Vasion Print Admin Portal
    Given I login to the admin portal
    Then I expect that the title is "PrinterLogic"

Scenario: I can add a printer
    When I add a printer named "TempTestPrinter" with IP "0.0.0.0"
    Then the printer "TempTestPrinter" should be visible

Scenario: I can delete a printer
    When I delete the printer "TempTestPrinter"
    Then the printer "TempTestPrinter" should not be visible

Scenario: I can edit a printer's Printer Name
    When I open printer "beepbeep"
    And I set the printer name to "TempTestName"
    Then the printer name should be "TempTestName"
    When I open printer "TempTestName"
    And I set the printer name to "beepbeep"
    Then the printer name should be "beepbeep"
    
Scenario: I can edit a printer's IP address
    When I open printer "beepbeep" Port settings
    Then I expect that element "#int_port_number" is visible
    When I set the printer IP to "1.0.1.0"
    Then the printer IP should be "1.0.1.0"
    When I set the printer IP to "255.255.255.255"
    Then the printer IP should be "255.255.255.255"

Scenario: I can get to the Vasion Print Admin Guide
    Given I pause for 1000ms
    When I open the help menu and click "Product Guide"
    Then I expect that a new tab has opened

Scenario: I can access General Settings
    Given I close the last opened tab
    And I pause for 2000ms
    When I navigate to "General" settings
    Then I should see "General" on the page

Scenario: I can access Printing Settings
    When I navigate to "Printing" settings
    Then I should see "Printing Configuration" on the page

Scenario: I can access Scanning Settings
    When I navigate to "Scanning" settings
    Then I should see "Scan Settings" on the page

Scenario: I can access Output Settings
    When I navigate to "Output" settings
    Then I should see "Output Settings" on the page

Scenario: I can access Portal Settings
    When I navigate to "Portal" settings
    Then I should see "Portal Settings" on the page

Scenario: I can access Client Settings
    When I navigate to "Client" settings
    Then I should see "Client" on the page

Scenario: I can access Mobile Settings
    When I navigate to "Mobile" settings
    Then I should see "Mobile Settings" on the page

Scenario: I can access my account information
    When I access my account information
    Then I should see "License Details" on the page

Scenario: I can Logout
    When I logout
    Then I expect that the title is "Vasion Automate"





