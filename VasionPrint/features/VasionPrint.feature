Feature: Vasion Print Basic Printer functionality
    As an IT administrator
    I want to be able to create printers that my users will be able to install without having to use Printer servers
    So I can lessen cost and make it easier

Scenario: Login to Vasion Print Admin Portal
    Given I open the url "https://jordansnow.printercloudnow.com/admin/"
    And I pause for 2000ms
    When I set "VasionTest" to the inputfield "#login-username-field"
    And I set "VasionTest" to the inputfield "#login-password-field"
    And I click on the element "#sign-in-button"
    And I pause for 2000ms
    Then I expect that the title is "PrinterLogic"

Scenario: I can add a printer
    Given I pause for 1000ms
    When I click on the link "New"
    And I pause for 1000ms
    Then I expect that element "#addip_link" is visible
    When I click on the element "#addip_link"
    And I pause for 1000ms
    When I set "TempTestPrinter" to the inputfield "#PrinterName"
    And I set "0.0.0.0" to the inputfield "#IPAddress"
    And I click on the element "#add_ip_close"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "TempTestPrinter"

Scenario: I can delete a printer
    Given I pause for 1000ms
    When I right click on the link "TempTestPrinter"
    And I pause for 1000ms
    And I click on the link "Delete"
    And I pause for 1000ms
    And I set "DELETE" to the inputfield "#delete_confirm_text"
    And I click on the element "#delete_confirm_btn_ok"
    And I pause for 1000ms
    Then I expect that element "body" not contains the text "TempTestPrinter"

Scenario: I can edit a printer's Printer Name
    Given I pause for 1000ms
    When I click on the link "beepbeep"
    And I pause for 1000ms
    And I set "TempTestName" to the inputfield "#str_title"
    And I click on the link "Save"
    And I pause for 1000ms
    Then I expect that element "#str_title" contains the text "TempTestName"
    When I click on the link "TempTestName"
    And I pause for 1000ms
    And I set "beepbeep" to the inputfield "#str_title"
    And I click on the link "Save"
    And I pause for 1000ms
    Then I expect that element "#str_title" contains the text "beepbeep"
    
Scenario: I can edit a printer's IP address
    Given I pause for 1000ms
    When I click on the link "beepbeep"
    And I pause for 1000ms
    And I click on the tab "Port"
    And I pause for 1000ms
    Then I expect that element "#int_port_number" is visible
    When I set "1.0.1.0" to the inputfield "#str_host_address"
    And I click on the link "Save"
    And I pause for 1000ms
    Then I expect that element "#str_host_address" contains the text "1.0.1.0"
    When I set "255.255.255.255" to the inputfield "#str_host_address"
    And I click on the link "Save"
    And I pause for 1000ms
    Then I expect that element "#str_host_address" contains the text "255.255.255.255"

Scenario: I can get to the Vasion Print Admin Guide
    Given I pause for 1000ms
    When I click on the element "#help-menu"
    And I click on the link "Product Guide"
    And I pause for 2000ms
    Then I expect that a new tab has opened

Scenario: I can access General Settings
    Given I close the last opened tab
    And I pause for 2000ms
    When I click on the element "#gear-menu"
    And I pause for 1000ms
    And I click on the link "Settings"
    And I pause for 1000ms
    And I click on the link "General"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "General"

Scenario: I can access Printing Settings
    Given I pause for 2000ms
    When I click on the element "#gear-return-button"
    And I pause for 2000ms
    And I click on the element "#gear-menu"
    And I pause for 1000ms
    And I click on the link "Settings"
    And I pause for 1000ms
    And I click on the link "Printing"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "Printing Configuration"

Scenario: I can access Scanning Settings
    Given I pause for 2000ms
    When I click on the element "#gear-return-button"
    And I pause for 2000ms
    And I click on the element "#gear-menu"
    And I pause for 1000ms
    And I click on the link "Settings"
    And I pause for 1000ms
    And I click on the link "Scanning"
    And I pause for 2000ms
    Then I expect that element "body" contains the text "Scan Settings"

Scenario: I can access Output Settings
    Given I pause for 2000ms
    When I click on the element "#gear-return-button"
    And I pause for 2000ms
    And I click on the element "#gear-menu"
    And I pause for 1000ms
    And I click on the link "Settings"
    And I pause for 1000ms
    And I click on the link "Output"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "Output Settings"

Scenario: I can access Portal Settings
    Given I pause for 2000ms
    When I click on the element "#gear-return-button"
    And I pause for 2000ms
    And I click on the element "#gear-menu"
    And I pause for 1000ms
    And I click on the link "Settings"
    And I pause for 1000ms
    And I click on the link "Portal"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "Portal Settings"

Scenario: I can access Client Settings
    Given I pause for 2000ms
    When I click on the element "#gear-return-button"
    And I pause for 2000ms
    And I click on the element "#gear-menu"
    And I pause for 1000ms
    And I click on the link "Settings"
    And I pause for 1000ms
    And I click on the link "Client"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "Client"

Scenario: I can access Mobile Settings
    Given I pause for 2000ms
    When I click on the element "#gear-return-button"
    And I pause for 2000ms
    And I click on the element "#gear-menu"
    And I pause for 1000ms
    And I click on the link "Settings"
    And I pause for 1000ms
    And I click on the link "Mobile"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "Mobile Settings"

Scenario: I can access my account information
    Given I pause for 1000ms
    When I click on the element "#user-menu"
    And I pause for 1000ms
    And I click on the link "My Account"
    And I pause for 1000ms
    Then I expect that element "body" contains the text "License Details"

Scenario: I can Logout
    Given I pause for 1000ms
    When I click on the element "#user-menu"
    And I pause for 1000ms
    And I click on the link "Sign Out"
    And I pause for 3000ms
    Then I expect that the title is "Vasion Automate"





