@endpoint(snapshots) @endpoint(snapshots-v1)
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

  @integration-only
  Scenario: Take graph snapshots returns "OK" response
    Given request contains "start" parameter with value {{ timestamp("now - 1d") }}
    And request contains "end" parameter with value {{ timestamp("now") }}
    And request contains "metric_query" parameter with value "avg:system.load.1{*}"
    And request contains "title" parameter with value "System load"
    When the request is sent
    Then the response status is 200 OK
