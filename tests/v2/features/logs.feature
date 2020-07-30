@endpoint(logs)
Feature: Logs
  Search your logs in the Datadog platform over HTTP.  [See API version
  1](/api/v1/logs/) for sending logs.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Logs" API

  @generated @skip
  Scenario: Get a quick list of logs returns "OK" response
    Given new "ListLogsGet" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a list of logs returns "OK" response
    Given new "ListLogs" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Aggregate events returns "OK" response
    Given new "AggregateLogs" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
