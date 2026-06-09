@endpoint(csm-settings) @endpoint(csm-settings-v2)
Feature: CSM Settings
  Datadog Cloud Security Management (CSM) Settings APIs allow you to list
  and filter your cloud hosts monitored by CSM, covering both agentless and
  agent-based discovery. For more information, see [Cloud Security Managemen
  t](https://docs.datadoghq.com/security/cloud_security_management).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CSMSettings" API

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get agentless host facet info returns "Bad Request" response
    Given operation "GetCSMAgentlessHostFacetInfo" enabled
    And new "GetCSMAgentlessHostFacetInfo" request
    And request contains "facet" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get agentless host facet info returns "OK" response
    Given operation "GetCSMAgentlessHostFacetInfo" enabled
    And new "GetCSMAgentlessHostFacetInfo" request
    And request contains "facet" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get unified host facet info returns "Bad Request" response
    Given operation "GetCSMUnifiedHostFacetInfo" enabled
    And new "GetCSMUnifiedHostFacetInfo" request
    And request contains "facet" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get unified host facet info returns "OK" response
    Given operation "GetCSMUnifiedHostFacetInfo" enabled
    And new "GetCSMUnifiedHostFacetInfo" request
    And request contains "facet" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List agentless host facets returns "OK" response
    Given operation "ListCSMAgentlessHostFacets" enabled
    And new "ListCSMAgentlessHostFacets" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List agentless hosts returns "Bad Request" response
    Given operation "ListCSMAgentlessHosts" enabled
    And new "ListCSMAgentlessHosts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List agentless hosts returns "OK" response
    Given operation "ListCSMAgentlessHosts" enabled
    And new "ListCSMAgentlessHosts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List unified host facets returns "OK" response
    Given operation "ListCSMUnifiedHostFacets" enabled
    And new "ListCSMUnifiedHostFacets" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List unified hosts returns "Bad Request" response
    Given operation "ListCSMUnifiedHosts" enabled
    And new "ListCSMUnifiedHosts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: List unified hosts returns "OK" response
    Given operation "ListCSMUnifiedHosts" enabled
    And new "ListCSMUnifiedHosts" request
    When the request is sent
    Then the response status is 200 OK
