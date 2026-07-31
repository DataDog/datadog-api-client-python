@endpoint(elastic-cloud-monitoring) @endpoint(elastic-cloud-monitoring-v2)
Feature: Elastic Cloud Monitoring
  Manage Elastic Cloud accounts for the monitoring interface (`elastic-
  cloud`), served by the Account Management Service (AMS). Concrete,
  strongly typed CRUD operations for the monitoring interface.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ElasticCloudMonitoring" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud monitoring account returns "Bad Request" response
    Given operation "CreateElasticCloudMonitoringAccount" enabled
    And new "CreateElasticCloudMonitoringAccount" request
    And body with value {"data": {"attributes": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "name": "elastic-cloud-prod", "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud monitoring account returns "Created" response
    Given operation "CreateElasticCloudMonitoringAccount" enabled
    And new "CreateElasticCloudMonitoringAccount" request
    And body with value {"data": {"attributes": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "name": "elastic-cloud-prod", "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud monitoring account returns "Not Found" response
    Given operation "CreateElasticCloudMonitoringAccount" enabled
    And new "CreateElasticCloudMonitoringAccount" request
    And body with value {"data": {"attributes": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "name": "elastic-cloud-prod", "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud monitoring account returns "Bad Request" response
    Given operation "DeleteElasticCloudMonitoringAccount" enabled
    And new "DeleteElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud monitoring account returns "No Content" response
    Given operation "DeleteElasticCloudMonitoringAccount" enabled
    And new "DeleteElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud monitoring account returns "Not Found" response
    Given operation "DeleteElasticCloudMonitoringAccount" enabled
    And new "DeleteElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud monitoring account returns "Bad Request" response
    Given operation "GetElasticCloudMonitoringAccount" enabled
    And new "GetElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud monitoring account returns "Not Found" response
    Given operation "GetElasticCloudMonitoringAccount" enabled
    And new "GetElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud monitoring account returns "OK" response
    Given operation "GetElasticCloudMonitoringAccount" enabled
    And new "GetElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud monitoring accounts returns "Bad Request" response
    Given operation "ListElasticCloudMonitoringAccounts" enabled
    And new "ListElasticCloudMonitoringAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud monitoring accounts returns "Not Found" response
    Given operation "ListElasticCloudMonitoringAccounts" enabled
    And new "ListElasticCloudMonitoringAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud monitoring accounts returns "OK" response
    Given operation "ListElasticCloudMonitoringAccounts" enabled
    And new "ListElasticCloudMonitoringAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud monitoring account returns "Bad Request" response
    Given operation "UpdateElasticCloudMonitoringAccount" enabled
    And new "UpdateElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "name": "elastic-cloud-prod", "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud monitoring account returns "Not Found" response
    Given operation "UpdateElasticCloudMonitoringAccount" enabled
    And new "UpdateElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "name": "elastic-cloud-prod", "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud monitoring account returns "OK" response
    Given operation "UpdateElasticCloudMonitoringAccount" enabled
    And new "UpdateElasticCloudMonitoringAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"password": "your-password", "type": "basic", "username": "datadog"}, "dataflows": [{"enabled": true, "id": "elastic-cloud-metrics"}], "name": "elastic-cloud-prod", "settings": {"cat_allocation_stats_enabled": false, "detailed_index_stats_enabled": false, "index_stats_enabled": false, "pending_task_stats_enabled": false, "pshard_graceful_to_enabled": false, "pshard_stats_enabled": false, "slm_stats_enabled": false, "tags": ["env:prod"], "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK
