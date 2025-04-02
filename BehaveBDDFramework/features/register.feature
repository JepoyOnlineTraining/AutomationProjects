Feature: Register Account functionality

  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter mandatory fields
    And I click on Continue button
    Then Account should get created

  Scenario: Register with all fields
     Given I navigate to Register Page
    When I enter all fields
    And I click on Continue button
    Then Account should get created

  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter details into all fields except email filed
    And I enter existing accounts email into email field
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be display


  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning messages for every mandatory fields should be displayed