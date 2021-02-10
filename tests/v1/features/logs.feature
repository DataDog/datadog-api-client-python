@endpoint(logs)
Feature: Logs
  Search your logs and send them to your Datadog platform over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Logs" API
    And new "ListLogs" request
    And body {}

  @generated @skip
  Scenario: Search logs returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Search logs returns "OK" response
    When the request is sent
    Then the response status is 200 OK
