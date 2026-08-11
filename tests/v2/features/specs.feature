@endpoint(specs) @endpoint(specs-v2)
Feature: Specs
  View API specs stored in the system.

  @generated @skip @team:DataDog/web-frameworks-test
  Scenario: List API specs returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Specs" API
    And new "ListSpecs" request
    When the request is sent
    Then the response status is 200 OK
