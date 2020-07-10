@endpoint(snapshots)
Feature: Snapshots
  Take graph snapshots using the API.

  @generated @skip
  Scenario: Take graph snapshots returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Snapshots" API
    And new "GetGraphSnapshot" request
    When the request is sent
    Then the response status is 200 OK
