@endpoint(org-connections) @endpoint(org-connections-v2)
Feature: Org Connections
  Manage connections between organizations. Org connections allow for
  controlled sharing of data between different Datadog organizations. See
  the [Cross-Organization Visibiltiy](https://docs.datadoghq.com/account_man
  agement/org_settings/cross_org_visibility/) page for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OrgConnections" API

  @team:DataDog/aaa-granular-access
  Scenario: Create Org Connection returns "Bad Request" response
    Given new "CreateOrgConnections" request
    And body with value {"data": {"type": "org_connection", "relationships": {"sink_org": {"data": {"type": "orgs", "id": "83999dcd-7f97-11f0-8de1-1ecf66f1aa85"}}}, "attributes": {"connection_types": ["logs", "logs"]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-granular-access
  Scenario: Create Org Connection returns "Conflict" response
    Given there is a valid "org_connection" in the system
    And new "CreateOrgConnections" request
    And body with value {"data": {"type": "org_connection", "relationships": {"sink_org": {"data": {"type": "orgs", "id": "83999dcd-7f97-11f0-8de1-1ecf66f1aa85"}}}, "attributes": {"connection_types": ["logs"]}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/aaa-granular-access
  Scenario: Create Org Connection returns "Not Found" response
    Given new "CreateOrgConnections" request
    And body with value {"data": {"type": "org_connection", "relationships": {"sink_org": {"data": {"type": "orgs", "id": "nonexistent-org-id"}}}, "attributes": {"connection_types": ["logs"]}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aaa-granular-access
  Scenario: Create Org Connection returns "OK" response
    Given new "CreateOrgConnections" request
    And body with value {"data": {"type": "org_connection", "relationships": {"sink_org": {"data": {"type": "orgs", "id": "83999dcd-7f97-11f0-8de1-1ecf66f1aa85"}}}, "attributes": {"connection_types": ["logs"]}}}
    When the request is sent
    Then the response status is 200 Created

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/aaa-granular-access
  Scenario: Delete Org Connection returns "Bad Request" response
    Given new "DeleteOrgConnections" request
    And request contains "connection_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-granular-access
  Scenario: Delete Org Connection returns "Not Found" response
    Given new "DeleteOrgConnections" request
    And request contains "connection_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aaa-granular-access
  Scenario: Delete Org Connection returns "OK" response
    Given there is a valid "org_connection" in the system
    And new "DeleteOrgConnections" request
    And request contains "connection_id" parameter from "org_connection.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-granular-access
  Scenario: List Org Connections returns "OK" response
    Given new "ListOrgConnections" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-granular-access
  Scenario: Update Org Connection returns "Bad Request" response
    Given there is a valid "org_connection" in the system
    And new "UpdateOrgConnections" request
    And request contains "connection_id" parameter from "org_connection.data.id"
    And body with value {"data": {"type": "org_connection", "id": "{{ org_connection.data.id }}", "attributes": {"connection_types": ["logs", "logs"]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-granular-access
  Scenario: Update Org Connection returns "Not Found" response
    Given there is a valid "org_connection" in the system
    And new "UpdateOrgConnections" request
    And request contains "connection_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "org_connection", "id": "00000000-0000-0000-0000-000000000000", "attributes": {"connection_types": ["logs", "metrics"]}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aaa-granular-access
  Scenario: Update Org Connection returns "OK" response
    Given there is a valid "org_connection" in the system
    And new "UpdateOrgConnections" request
    And request contains "connection_id" parameter from "org_connection.data.id"
    And body with value {"data": {"type": "org_connection", "id": "{{ org_connection.data.id }}", "attributes": {"connection_types": ["logs", "metrics"]}}}
    When the request is sent
    Then the response status is 200 OK
