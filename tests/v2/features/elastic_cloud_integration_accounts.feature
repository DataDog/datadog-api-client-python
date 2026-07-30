@endpoint(elastic-cloud-integration-accounts) @endpoint(elastic-cloud-integration-accounts-v2)
Feature: Elastic Cloud Integration Accounts
  Manage Elastic Cloud accounts for the Elastic Cloud integration, served by
  the Account Management Service (AMS). The account payload is strongly
  typed to Elastic Cloud; the supported interfaces (monitoring and Cloud
  Cost Management) are modeled as a nested union.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ElasticCloudIntegrationAccounts" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud integration account returns "Bad Request" response
    Given operation "CreateElasticCloudIntegrationAccount" enabled
    And new "CreateElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}, "type": "elastic-cloud"}, "name": "elastic-cloud-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud integration account returns "Created" response
    Given operation "CreateElasticCloudIntegrationAccount" enabled
    And new "CreateElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}, "type": "elastic-cloud"}, "name": "elastic-cloud-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud integration account returns "Not Found" response
    Given operation "CreateElasticCloudIntegrationAccount" enabled
    And new "CreateElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}, "type": "elastic-cloud"}, "name": "elastic-cloud-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud integration account returns "Bad Request" response
    Given operation "DeleteElasticCloudIntegrationAccount" enabled
    And new "DeleteElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud integration account returns "No Content" response
    Given operation "DeleteElasticCloudIntegrationAccount" enabled
    And new "DeleteElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud integration account returns "Not Found" response
    Given operation "DeleteElasticCloudIntegrationAccount" enabled
    And new "DeleteElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud integration account returns "Bad Request" response
    Given operation "GetElasticCloudIntegrationAccount" enabled
    And new "GetElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud integration account returns "Not Found" response
    Given operation "GetElasticCloudIntegrationAccount" enabled
    And new "GetElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud integration account returns "OK" response
    Given operation "GetElasticCloudIntegrationAccount" enabled
    And new "GetElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud integration accounts returns "Bad Request" response
    Given operation "ListElasticCloudIntegrationAccounts" enabled
    And new "ListElasticCloudIntegrationAccounts" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud integration accounts returns "Not Found" response
    Given operation "ListElasticCloudIntegrationAccounts" enabled
    And new "ListElasticCloudIntegrationAccounts" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud integration accounts returns "OK" response
    Given operation "ListElasticCloudIntegrationAccounts" enabled
    And new "ListElasticCloudIntegrationAccounts" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud integration account returns "Bad Request" response
    Given operation "UpdateElasticCloudIntegrationAccount" enabled
    And new "UpdateElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}, "type": "elastic-cloud"}, "name": "elastic-cloud-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud integration account returns "Not Found" response
    Given operation "UpdateElasticCloudIntegrationAccount" enabled
    And new "UpdateElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}, "type": "elastic-cloud"}, "name": "elastic-cloud-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud integration account returns "OK" response
    Given operation "UpdateElasticCloudIntegrationAccount" enabled
    And new "UpdateElasticCloudIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}, "type": "elastic-cloud"}, "name": "elastic-cloud-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK
