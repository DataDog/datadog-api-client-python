@v1 @endpoint(monitors) @todo
Feature: Monitors
  [Monitors](https://docs.datadoghq.com/monitors) allow you to watch a
  metric or check that you care about, notifying your team when some defined
  threshold is exceeded. Refer to the Creating Monitors page for more
  information on creating monitors.

  Background:
    Given a valid "apiKeyAuth" key
    And a valid "appKeyAuth" key
    And an instance of "Monitors" API

  Scenario: Get all monitor details leading to OK
    Given new "ListMonitors" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Create a monitor leading to OK
    Given new "CreateMonitor" request
    And body {}
    When the request is sent
    Then the status is 200 OK

  Scenario: Check if a monitor can be deleted leading to OK
    Given new "CheckCanDeleteMonitor" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Validate a monitor leading to OK
    Given new "ValidateMonitor" request
    And body {}
    When the request is sent
    Then the status is 200 OK

  Scenario: Delete a monitor leading to OK
    Given new "DeleteMonitor" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Get a monitor's details leading to OK
    Given new "GetMonitor" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Edit a monitor leading to OK
    Given new "UpdateMonitor" request
    And body {}
    When the request is sent
    Then the status is 200 OK
