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
  Scenario: Create a browser test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsBrowserTest" request
    And body {}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Create a browser test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsBrowserTest" request
    And body {}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip
  Scenario: Create a browser test returns "Test quota is reached" response
    Given new "CreateSyntheticsBrowserTest" request
    And body {}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @generated @skip
  Scenario: Create a global variable returns "Invalid request" response
    Given new "CreateGlobalVariable" request
    And body {}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip
  Scenario: Create a global variable returns "OK" response
    Given new "CreateGlobalVariable" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a private location returns "OK" response
    Given new "CreatePrivateLocation" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a private location returns "Private locations are not activated for the user" response
    Given new "CreatePrivateLocation" request
    And body {}
    When the request is sent
    Then the response status is 404 Private locations are not activated for the user

  @generated @skip
  Scenario: Create a private location returns "Quota reached for private locations" response
    Given new "CreatePrivateLocation" request
    And body {}
    When the request is sent
    Then the response status is 402 Quota reached for private locations

  @generated @skip
  Scenario: Create a test returns "- JSON format is wrong" response
    Given new "CreateTest" request
    And body {}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Create a test returns "OK - Returns the created test details." response
    Given new "CreateTest" request
    And body {}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip
  Scenario: Create a test returns "Test quota is reached" response
    Given new "CreateTest" request
    And body {}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @generated @skip
  Scenario: Create an API test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsAPITest" request
    And body {}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Create an API test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body {}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip
  Scenario: Create an API test returns "Test quota is reached" response
    Given new "CreateSyntheticsAPITest" request
    And body {}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @generated @skip
  Scenario: Delete a global variable returns "JSON format is wrong" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip
  Scenario: Delete a global variable returns "Not found" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Delete a global variable returns "OK" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a private location returns "- Private locations are not activated for the user" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip
  Scenario: Delete a private location returns "OK" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Delete tests returns "- JSON format is wrong" response
    Given new "DeleteTests" request
    And body {}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Delete tests returns "- Tests to be deleted can't be found" response
    Given new "DeleteTests" request
    And body {}
    When the request is sent
    Then the response status is 404 - Tests to be deleted can't be found

  @generated @skip
  Scenario: Delete tests returns "OK." response
    Given new "DeleteTests" request
    And body {}
    When the request is sent
    Then the response status is 200 OK.

  @generated @skip
  Scenario: Edit a browser test returns "- JSON format is wrong" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Edit a browser test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip
  Scenario: Edit a browser test returns "OK" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a global variable returns "Invalid request" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip
  Scenario: Edit a global variable returns "OK" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a private location returns "- Private locations are not activated for the user" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip
  Scenario: Edit a private location returns "OK" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a test returns "- JSON format is wrong" response
    Given new "UpdateTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Edit a test returns "- Synthetic is not activated for the user" response
    Given new "UpdateTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Edit a test returns "OK" response
    Given new "UpdateTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit an API test returns "- JSON format is wrong" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Edit an API test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip
  Scenario: Edit an API test returns "OK" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a global variable returns "Not found" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Get a global variable returns "OK" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a private location returns "- Synthetic private locations are not activated for the user" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic private locations are not activated for the user

  @generated @skip
  Scenario: Get a private location returns "OK" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a test configuration (API) returns "- Synthetic is not activated for the user" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a test configuration (API) returns "OK" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a test configuration (browser) returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a test configuration (browser) returns "OK" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a test result (API) returns "- Synthetic is not activated for the user" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a test result (API) returns "OK" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a test result (browser) returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a test result (browser) returns "OK" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all locations (public and private) returns "OK" response
    Given new "ListLocations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the list of all tests returns "OK - Returns the list of all Synthetic tests." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 200 OK - Returns the list of all Synthetic tests.

  @generated @skip
  Scenario: Get the list of all tests returns "Synthetics is not activated for the user." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 404 Synthetics is not activated for the user.

  @generated @skip
  Scenario: Get the test's latest results summaries (API) returns "- Synthetic is not activated for the user" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get the test's latest results summaries (API) returns "OK" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the test's latest results summaries (browser) returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get the test's latest results summaries (browser) returns "OK" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Pause or start a test returns "- Synthetic is not activated for the user" response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Pause or start a test returns "JSON format is wrong." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 JSON format is wrong.

  @generated @skip
  Scenario: Pause or start a test returns "OK - Returns a boolean indicating if the update was successful." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK - Returns a boolean indicating if the update was successful.

  @generated @skip
  Scenario: Trigger some Synthetics tests for CI returns "JSON format is wrong" response
    Given new "TriggerCITests" request
    And body {}
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip
  Scenario: Trigger some Synthetics tests for CI returns "OK" response
    Given new "TriggerCITests" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
