@endpoint(synthetics) @endpoint(synthetics-v2)
Feature: Synthetics
  Datadog Synthetics uses simulated user requests and browser rendering to
  help you ensure uptime, identify regional issues, and track your
  application performance. Datadog Synthetics tests come in two different
  flavors, [API tests](https://docs.datadoghq.com/synthetics/api_tests/) and
  [browser tests](https://docs.datadoghq.com/synthetics/browser_tests). You
  can use Datadog’s API to manage both test types programmatically.  For
  more information about Synthetics, see the [Synthetics
  overview](https://docs.datadoghq.com/synthetics/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Synthetics" API

  @team:DataDog/synthetics-managing
  Scenario: Get the on-demand concurrency cap returns "OK" response
    Given new "GetOnDemandConcurrencyCap" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/synthetics-managing
  Scenario: Save new value for on-demand concurrency cap returns "OK" response
    Given new "SetOnDemandConcurrencyCap" request
    And body with value {"on_demand_concurrency_cap": 20}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.on_demand_concurrency_cap" is equal to 20

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Search Synthetics suites returns "API error response." response
    Given new "SearchSuites" request
    When the request is sent
    Then the response status is 400 API error response.

  @team:DataDog/synthetics-managing
  Scenario: Search Synthetics suites returns "OK" response
    Given new "SearchSuites" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Synthetics: Bulk delete suites returns "API error response." response
    Given new "DeleteSyntheticsSuites" request
    And body with value {"data": {"attributes": {"public_ids": [""]}, "type": "delete_suites_request"}}
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Synthetics: Bulk delete suites returns "OK" response
    Given new "DeleteSyntheticsSuites" request
    And body with value {"data": {"attributes": {"public_ids": [""]}, "type": "delete_suites_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Synthetics: Create a test suite returns "API error response." response
    Given new "CreateSyntheticsSuite" request
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [{"alerting_criticality": "critical", "public_id": ""}], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 400 API error response.

  @team:DataDog/synthetics-managing
  Scenario: Synthetics: Create a test suite returns "OK" response
    Given new "CreateSyntheticsSuite" request
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Synthetics: Get a suite returns "API error response." response
    Given new "GetSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Synthetics: Get a suite returns "OK" response
    Given new "GetSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Synthetics: edit a test suite returns "API error response." response
    Given new "EditSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [{"alerting_criticality": "critical", "public_id": ""}], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Synthetics: edit a test suite returns "OK" response
    Given new "EditSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [{"alerting_criticality": "critical", "public_id": ""}], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 200 OK
