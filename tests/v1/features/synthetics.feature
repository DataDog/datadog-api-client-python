@endpoint(synthetics)
Feature: Synthetics
  Datadog Synthetics uses simulated user requests and browser rendering to
  help you ensure uptime, identify regional issues, and track your
  application performance. Datadog Synthetics tests come in two different
  flavors, [API
  tests](https://docs.datadoghq.com/synthetics/api_tests/?tab=httptest) and
  [browser tests](https://docs.datadoghq.com/synthetics/browser_tests). You
  can use Datadog’s API to manage both test types programmatically.  For
  more information about Synthetics, see the [Synthetics
  overview](https://docs.datadoghq.com/synthetics/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Synthetics" API

  @generated @skip
  Scenario: Get all locations (public and private) returns "OK" response
    Given new "ListLocations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a list of tests returns "OK - Returns the list of all Synthetic tests (properly filtered by type)." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 200 OK - Returns the list of all Synthetic tests (properly filtered by type).

  @generated @skip
  Scenario: Create a test returns "OK - Returns the created test details." response
    Given new "CreateTest" request
    And body {}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip
  Scenario: Get a test configuration (browser) returns "OK" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the test's latest results summaries (browser) returns "OK" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a test result (browser) returns "OK" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete tests returns "OK." response
    Given new "DeleteTests" request
    And body {}
    When the request is sent
    Then the response status is 200 OK.

  @generated @skip
  Scenario: Get a test configuration (API) returns "OK" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a test returns "OK" response
    Given new "UpdateTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the test's latest results summaries (API) returns "OK" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a test result (API) returns "OK" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Pause or start a test returns "OK - Returns a boolean indicating if the update was successful." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK - Returns a boolean indicating if the update was successful.

  @generated @skip
  Scenario: Delete a global variable returns "OK" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a global variable returns "OK" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a global variable returns "OK" response
    Given new "CreateGlobalVariable" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Trigger some Synthetics tests for CI returns "OK" response
    Given new "TriggerCITests" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
