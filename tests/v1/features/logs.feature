@endpoint(logs)
Feature: Logs
  Search your logs and send them to your Datadog platform over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "Logs" API

  @generated @skip
  Scenario: Search logs returns "Bad Request" response
    Given body {}
    And a valid "appKeyAuth" key in the system
    And new "ListLogs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Search logs returns "OK" response
    Given body {}
    And a valid "appKeyAuth" key in the system
    And new "ListLogs" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: Send logs returns "Response from server (always 200 empty JSON)." response
    Given new "SubmitLog" request
    And body [{"message": "{{ unique }}", "tags": "host:{{ unique_alnum }}"}]
    When the request is sent
    Then the response status is 200 Response from server (always 200 empty JSON).

  @generated @skip
  Scenario: Send logs returns "unexpected error" response
    Given body {}
    And new "SubmitLog" request
    When the request is sent
    Then the response status is 400 unexpected error
