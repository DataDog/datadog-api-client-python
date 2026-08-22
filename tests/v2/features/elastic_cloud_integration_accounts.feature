@endpoint(elastic-cloud-integration-accounts) @endpoint(elastic-cloud-integration-accounts-v2)
Feature: Elastic Cloud Integration Accounts
  Manage your Datadog Elastic Cloud integration accounts directly through
  the Datadog API. Create, update, and delete accounts, configure
  authentication and settings, and enable or disable dataflows such as
  cluster metrics, index stats, shard stats, pending tasks, and snapshot
  lifecycle management stats. See the [Elastic Cloud integration
  page](https://docs.datadoghq.com/integrations/elastic-cloud/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ElasticCloudIntegrationAccounts" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud integration account returns "Bad Request" response
    Given operation "CreateElasticCloudIntegrationAccount" enabled
    And new "CreateElasticCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud integration account returns "Created" response
    Given operation "CreateElasticCloudIntegrationAccount" enabled
    And new "CreateElasticCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud integration account returns "Not Found" response
    Given operation "CreateElasticCloudIntegrationAccount" enabled
    And new "CreateElasticCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an Elastic Cloud integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateElasticCloudIntegrationAccount" enabled
    And new "CreateElasticCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud integration account returns "Bad Request" response
    Given operation "DeleteElasticCloudIntegrationAccount" enabled
    And new "DeleteElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud integration account returns "Not Found" response
    Given operation "DeleteElasticCloudIntegrationAccount" enabled
    And new "DeleteElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an Elastic Cloud integration account returns "OK" response
    Given operation "DeleteElasticCloudIntegrationAccount" enabled
    And new "DeleteElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud integration account returns "Bad Request" response
    Given operation "GetElasticCloudIntegrationAccount" enabled
    And new "GetElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud integration account returns "Not Found" response
    Given operation "GetElasticCloudIntegrationAccount" enabled
    And new "GetElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an Elastic Cloud integration account returns "OK" response
    Given operation "GetElasticCloudIntegrationAccount" enabled
    And new "GetElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud integration accounts returns "Bad Request" response
    Given operation "ListElasticCloudIntegrationAccounts" enabled
    And new "ListElasticCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud integration accounts returns "Not Found" response
    Given operation "ListElasticCloudIntegrationAccounts" enabled
    And new "ListElasticCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Elastic Cloud integration accounts returns "OK" response
    Given operation "ListElasticCloudIntegrationAccounts" enabled
    And new "ListElasticCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud integration account returns "Bad Request" response
    Given operation "UpdateElasticCloudIntegrationAccount" enabled
    And new "UpdateElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud integration account returns "Not Found" response
    Given operation "UpdateElasticCloudIntegrationAccount" enabled
    And new "UpdateElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud integration account returns "OK" response
    Given operation "UpdateElasticCloudIntegrationAccount" enabled
    And new "UpdateElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an Elastic Cloud integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateElasticCloudIntegrationAccount" enabled
    And new "UpdateElasticCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"elastic-cloud-detailed-index-stats": {"enabled": true}, "elastic-cloud-index-stats": {"enabled": true}, "elastic-cloud-pending-task-stats": {"enabled": true}, "elastic-cloud-primary-shard-graceful-timeout": {"enabled": true}, "elastic-cloud-primary-shard-stats": {"enabled": true}, "elastic-cloud-shard-allocation-stats": {"enabled": true}, "elastic-cloud-slm-stats": {"enabled": true}}, "name": "elastic-cloud-prod", "settings": {"tags": "env:prod,team:saasint", "url": "https://example.es.us-central1.gcp.cloud.es.io:9243"}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
