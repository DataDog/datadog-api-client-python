@endpoint(test-examples) @endpoint(test-examples-v2)
Feature: Test Examples
  Manage test example resources.

  @generated @skip @team:DataDog/webframeworks-test
  Scenario: List test examples returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TestExamples" API
    And new "ListTestExamples" request
    When the request is sent
    Then the response status is 200 OK
