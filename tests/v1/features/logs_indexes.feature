@endpoint(logs-indexes)
Feature: Logs Indexes
  Manage configuration of [log
  indexes](https://docs.datadoghq.com/logs/indexes/). You need an API and
  application key with Admin rights to interact with this endpoint.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsIndexes" API

  @generated @skip
  Scenario: Get indexes order returns "OK" response
    Given operation "GetLogsIndexOrder" enabled
    And new "GetLogsIndexOrder" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update indexes order returns "OK" response
    Given operation "UpdateLogsIndexOrder" enabled
    And new "UpdateLogsIndexOrder" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all indexes returns "OK" response
    Given operation "ListLogIndexes" enabled
    And new "ListLogIndexes" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an index returns "OK" response
    Given operation "GetLogsIndex" enabled
    And new "GetLogsIndex" request
    And request contains "name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update an index returns "OK" response
    Given operation "UpdateLogsIndex" enabled
    And new "UpdateLogsIndex" request
    And request contains "name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK
