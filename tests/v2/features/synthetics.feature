@endpoint(synthetics) @endpoint(synthetics-v2)
Feature: Synthetics
  Synthetic tests use simulated requests and actions so you can monitor the
  availability and performance of systems and applications. Datadog supports
  the following types of synthetic tests: - [API
  tests](https://docs.datadoghq.com/synthetics/api_tests/) - [Browser
  tests](https://docs.datadoghq.com/synthetics/browser_tests) - [Network
  Path tests](https://docs.datadoghq.com/synthetics/network_path_tests/) -
  [Mobile Application
  tests](https://docs.datadoghq.com/synthetics/mobile_app_testing)  You can
  use the Datadog API to create, manage, and organize tests and test suites
  programmatically.  For more information, see the [Synthetic Monitoring
  documentation](https://docs.datadoghq.com/synthetics/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Synthetics" API

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Bulk delete suites returns "API error response." response
    Given new "DeleteSyntheticsSuites" request
    And body with value {"data": {"attributes": {"public_ids": [""]}, "type": "delete_suites_request"}}
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Bulk delete suites returns "OK" response
    Given new "DeleteSyntheticsSuites" request
    And body with value {"data": {"attributes": {"public_ids": [""]}, "type": "delete_suites_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Bulk delete tests returns "API error response." response
    Given new "DeleteSyntheticsTests" request
    And body with value {"data": {"attributes": {"public_ids": [""]}, "type": "delete_tests_request"}}
    When the request is sent
    Then the response status is 404 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Bulk delete tests returns "OK" response
    Given new "DeleteSyntheticsTests" request
    And body with value {"data": {"attributes": {"public_ids": [""]}, "type": "delete_tests_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a Network Path test returns "API error response." response
    Given new "CreateSyntheticsNetworkTest" request
    And body with value {"data": {"attributes": {"config": {"assertions": [{"operator": "lessThan", "property": "avg", "target": 500, "type": "latency"}], "request": {"e2e_queries": 50, "host": "", "max_ttl": 30, "port": 443, "tcp_method": "prefer_sack", "traceroute_queries": 3}}, "locations": ["aws:us-east-1", "agent:my-agent-name"], "message": "Network Path test notification", "name": "Example Network Path test", "options": {"monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "tcp", "tags": ["env:production"], "type": "network"}, "type": "network"}}
    When the request is sent
    Then the response status is 400 API error response.

  @team:DataDog/synthetics-managing
  Scenario: Create a Network Path test returns "OK" response
    Given new "CreateSyntheticsNetworkTest" request
    And body with value {"data": {"attributes": {"config": {"assertions": [{"operator": "lessThan", "property": "avg", "target": 500, "type": "latency"}], "request": {"host": "example.com", "port": 443, "tcp_method": "prefer_sack", "max_ttl": 30, "e2e_queries": 50, "traceroute_queries": 3}}, "locations": ["aws:us-east-1", "agent:my-agent-name"], "message": "Network Path test notification", "name": "Example Network Path test", "options": {"tick_every": 60}, "status": "live", "subtype": "tcp", "tags": ["env:production"], "type": "network"}, "type": "network"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a test suite returns "API error response." response
    Given new "CreateSyntheticsSuite" request
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [{"alerting_criticality": "critical", "public_id": ""}], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 400 API error response.

  @team:DataDog/synthetics-managing
  Scenario: Create a test suite returns "OK" response
    Given new "CreateSyntheticsSuite" request
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a Network Path test returns "API error response." response
    Given new "UpdateSyntheticsNetworkTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"assertions": [{"operator": "lessThan", "property": "avg", "target": 500, "type": "latency"}], "request": {"e2e_queries": 50, "host": "", "max_ttl": 30, "port": 443, "tcp_method": "prefer_sack", "traceroute_queries": 3}}, "locations": ["aws:us-east-1", "agent:my-agent-name"], "message": "Network Path test notification", "name": "Example Network Path test", "options": {"monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "tcp", "tags": ["env:production"], "type": "network"}, "type": "network"}}
    When the request is sent
    Then the response status is 404 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a Network Path test returns "OK" response
    Given new "UpdateSyntheticsNetworkTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"assertions": [{"operator": "lessThan", "property": "avg", "target": 500, "type": "latency"}], "request": {"e2e_queries": 50, "host": "", "max_ttl": 30, "port": 443, "tcp_method": "prefer_sack", "traceroute_queries": 3}}, "locations": ["aws:us-east-1", "agent:my-agent-name"], "message": "Network Path test notification", "name": "Example Network Path test", "options": {"monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "tcp", "tags": ["env:production"], "type": "network"}, "type": "network"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a test suite returns "API error response." response
    Given new "EditSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [{"alerting_criticality": "critical", "public_id": ""}], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a test suite returns "OK" response
    Given new "EditSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"message": "Notification message", "name": "Example suite name", "options": {}, "tags": ["env:production"], "tests": [{"alerting_criticality": "critical", "public_id": ""}], "type": "suite"}, "type": "suites"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a Network Path test returns "API error response." response
    Given new "GetSyntheticsNetworkTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @replay-only @team:DataDog/synthetics-managing
  Scenario: Get a Network Path test returns "OK" response
    Given new "GetSyntheticsNetworkTest" request
    And request contains "public_id" parameter with value "c7a-uwa-wn2"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a suite returns "API error response." response
    Given new "GetSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a suite returns "OK" response
    Given new "GetSyntheticsSuite" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

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

  @team:DataDog/synthetics-managing
  Scenario: Search Synthetics suites returns "OK" response
    Given new "SearchSuites" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Search test suites returns "API error response." response
    Given new "SearchSuites" request
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Search test suites returns "OK" response
    Given new "SearchSuites" request
    When the request is sent
    Then the response status is 200 OK
