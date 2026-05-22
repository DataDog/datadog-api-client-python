@endpoint(entity-integration-configs) @endpoint(entity-integration-configs-v2)
Feature: Entity Integration Configs
  Manage per-integration configurations for the Internal Developer Portal
  (IDP). These configurations control which external resources (for example,
  GitHub repositories, Jira projects, or PagerDuty services) are synced as
  entities into the Software Catalog.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "EntityIntegrationConfigs" API

  @generated @skip @team:DataDog/idp
  Scenario: Create or update entity integration configuration returns "Bad Request" response
    Given operation "UpdateEntityIntegrationConfig" enabled
    And new "UpdateEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"enabled_repos": [{"github_org_name": "myorg", "hostname": "github.com", "repo_name": "myrepo"}]}}, "type": "entity_integration_config_requests"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/idp
  Scenario: Create or update entity integration configuration returns "OK" response
    Given operation "UpdateEntityIntegrationConfig" enabled
    And new "UpdateEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"enabled_repos": [{"github_org_name": "myorg", "hostname": "github.com", "repo_name": "myrepo"}]}}, "type": "entity_integration_config_requests"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/idp
  Scenario: Delete an entity integration configuration returns "Bad Request" response
    Given operation "DeleteEntityIntegrationConfig" enabled
    And new "DeleteEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/idp
  Scenario: Delete an entity integration configuration returns "No Content" response
    Given operation "DeleteEntityIntegrationConfig" enabled
    And new "DeleteEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/idp
  Scenario: Delete an entity integration configuration returns "Not Found" response
    Given operation "DeleteEntityIntegrationConfig" enabled
    And new "DeleteEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/idp
  Scenario: Get an entity integration configuration returns "Bad Request" response
    Given operation "GetEntityIntegrationConfig" enabled
    And new "GetEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/idp
  Scenario: Get an entity integration configuration returns "Not Found" response
    Given operation "GetEntityIntegrationConfig" enabled
    And new "GetEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/idp
  Scenario: Get an entity integration configuration returns "OK" response
    Given operation "GetEntityIntegrationConfig" enabled
    And new "GetEntityIntegrationConfig" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
