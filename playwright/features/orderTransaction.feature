
Feature: Order Transaction
  Tests related to Order Transaction


  Scenario Outline: Verify Order Success message shown in details page
    Given Place the itme order with <userEmail> and <userPassword>
    And the user is on landing page
    When I login to portal with <userEmail> and <userPassword>
    And navigate to orders page
    And select the orderId
    Then order message is successfully displayed
    Examples:
      | userEmail             | userPassword |
      | roynijaraa@gmail.com  | Testing@123  |