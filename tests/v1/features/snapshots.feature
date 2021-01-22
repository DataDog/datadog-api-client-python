@endpoint(snapshots)
Feature: Snapshots
  Take graph snapshots using the API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Snapshots" API
    And new "GetGraphSnapshot" request

  @generated @skip
  Scenario: Take graph snapshots returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Take graph snapshots returns "OK" response
    When the request is sent
    Then the response status is 200 OK
