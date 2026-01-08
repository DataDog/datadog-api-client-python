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

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Patch a global variable returns "Bad Request" response
    Given new "PatchGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"json_patch": [{"op": "add", "path": "/name"}]}, "type": "global_variables_json_patch"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Patch a global variable returns "Not Found" response
    Given new "PatchGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"json_patch": [{"op": "add", "path": "/name"}]}, "type": "global_variables_json_patch"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Patch a global variable returns "OK" response
    Given new "PatchGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"json_patch": [{"op": "add", "path": "/name"}]}, "type": "global_variables_json_patch"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/synthetics-managing
  Scenario: Save new value for on-demand concurrency cap returns "OK" response
    Given new "SetOnDemandConcurrencyCap" request
    And body with value {"on_demand_concurrency_cap": 20}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.on_demand_concurrency_cap" is equal to 20
