Feature: Login Functionality

  Scenario: Successful Login
    Given I launch the browser
    When I enter valid username and password
    Then I should be redirected to the dashboard

  Scenario: Unsuccessful Login
    Given I launch the browser
    When I enter invalid username and password
    Then I should see a login error message

  Scenario: Validate Input Fields and Submit
    Given I launch the browser
    Then Username, Password fields and Submit button should be visible

  Scenario: Validate Logout
    Given I am logged into the Zen portal
    When I click logout
    Then I should be redirected to the login page
