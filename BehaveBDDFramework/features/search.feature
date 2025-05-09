
  Feature: Search functionality

    @search1
    Scenario: Search for a valid product
      Given I got navigated to Home Page
      When I enter valid product into the Search box field
      And I click on Search button
      Then Valid product should get displayed in Search results

    @search
    Scenario: Search for an invalid product
     Given I got navigated to Home Page
      When I enter invalid product into the Search box field
      And I click on Search button
      Then Proper message should be displayed in Search results

    @search
    Scenario: Seach without entering any product
      Given I got navigated to Home Page
      When I dont enter anything into Search box field
      And I click on Search button
      Then Proper message should be displayed in Search results