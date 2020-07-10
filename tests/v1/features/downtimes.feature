@endpoint(downtimes)
Feature: Downtimes
  [Downtiming](https://docs.datadoghq.com/monitors/downtimes) gives you
  greater control over monitor notifications by allowing you to globally
  exclude scopes from alerting. Downtime settings, which can be scheduled
  with start and end times, prevent all alerting related to specified
  Datadog tags.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Downtimes" API

  @generated @skip
  Scenario: Get all downtimes returns "OK" response
    Given new "ListDowntimes" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Schedule a downtime returns "OK" response
    Given new "CreateDowntime" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Cancel downtimes by scope returns "OK" response
    Given new "CancelDowntimesByScope" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Cancel a downtime returns "OK" response
    Given new "CancelDowntime" request
    And request contains "downtime_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Get a downtime returns "OK" response
    Given new "GetDowntime" request
    And request contains "downtime_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a downtime returns "OK" response
    Given new "UpdateDowntime" request
    And request contains "downtime_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK
