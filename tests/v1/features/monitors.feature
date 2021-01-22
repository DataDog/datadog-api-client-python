@endpoint(monitors)
Feature: Monitors
  [Monitors](https://docs.datadoghq.com/monitors) allow you to watch a
  metric or check that you care about, notifying your team when some defined
  threshold is exceeded. Refer to the Creating Monitors page for more
  information on creating monitors.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Monitors" API

  @generated @skip
  Scenario: Check if a monitor can be deleted returns "Bad Request" response
    Given new "CheckCanDeleteMonitor" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Check if a monitor can be deleted returns "Deletion conflict error" response
    Given new "CheckCanDeleteMonitor" request
    When the request is sent
    Then the response status is 409 Deletion conflict error

  @generated @skip
  Scenario: Check if a monitor can be deleted returns "OK" response
    Given new "CheckCanDeleteMonitor" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a monitor returns "Bad Request" response
    Given new "CreateMonitor" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a monitor returns "OK" response
    Given new "CreateMonitor" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a monitor returns "Bad Request" response
    Given new "DeleteMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete a monitor returns "Item not found error" response
    Given new "DeleteMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item not found error

  @generated @skip
  Scenario: Delete a monitor returns "OK" response
    Given new "DeleteMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a monitor returns "Bad Request" response
    Given new "UpdateMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Edit a monitor returns "Monitor Not Found error" response
    Given new "UpdateMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Monitor Not Found error

  @generated @skip
  Scenario: Edit a monitor returns "OK" response
    Given new "UpdateMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a monitor's details returns "Bad Request" response
    Given new "GetMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Get a monitor's details returns "Monitor Not Found error" response
    Given new "GetMonitor" request
    And request contains "monitor_id" parameter with value 12345
    When the request is sent
    Then the response status is 404 Monitor Not Found error

  @generated @skip
  Scenario: Get a monitor's details returns "OK" response
    Given new "GetMonitor" request
    And request contains "monitor_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all monitor details returns "Bad Request" response
    Given new "ListMonitors" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get all monitor details returns "OK" response
    Given new "ListMonitors" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Validate a monitor returns "Invalid JSON" response
    Given new "ValidateMonitor" request
    And body {}
    When the request is sent
    Then the response status is 400 Invalid JSON

  @generated @skip
  Scenario: Validate a monitor returns "OK" response
    Given new "ValidateMonitor" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
