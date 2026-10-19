@endpoint(temporal-cloud-openmetrics-integration) @endpoint(temporal-cloud-openmetrics-integration-v2)
Feature: Temporal Cloud OpenMetrics Integration
  Manage your Datadog Temporal Cloud OpenMetrics integration accounts and
  account resources directly through the Datadog API. See the [Temporal
  Cloud OpenMetrics integration
  page](https://docs.datadoghq.com/integrations/temporal-cloud-openmetrics/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TemporalCloudOpenMetricsIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Temporal Cloud OpenMetrics account returns "Bad Request" response
    Given operation "CreateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "CreateTemporalCloudOpenMetricsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Temporal Cloud OpenMetrics account returns "Created" response
    Given operation "CreateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "CreateTemporalCloudOpenMetricsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Temporal Cloud OpenMetrics account returns "Not Found" response
    Given operation "CreateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "CreateTemporalCloudOpenMetricsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Temporal Cloud OpenMetrics account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "CreateTemporalCloudOpenMetricsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a Temporal Cloud OpenMetrics account returns "Bad Request" response
    Given operation "DeleteTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "DeleteTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a Temporal Cloud OpenMetrics account returns "Not Found" response
    Given operation "DeleteTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "DeleteTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a Temporal Cloud OpenMetrics account returns "OK" response
    Given operation "DeleteTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "DeleteTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a Temporal Cloud OpenMetrics account returns "Bad Request" response
    Given operation "GetTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "GetTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a Temporal Cloud OpenMetrics account returns "Not Found" response
    Given operation "GetTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "GetTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a Temporal Cloud OpenMetrics account returns "OK" response
    Given operation "GetTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "GetTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Temporal Cloud OpenMetrics accounts returns "Bad Request" response
    Given operation "ListTemporalCloudOpenMetricsIntegrationAccounts" enabled
    And new "ListTemporalCloudOpenMetricsIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Temporal Cloud OpenMetrics accounts returns "Not Found" response
    Given operation "ListTemporalCloudOpenMetricsIntegrationAccounts" enabled
    And new "ListTemporalCloudOpenMetricsIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Temporal Cloud OpenMetrics accounts returns "OK" response
    Given operation "ListTemporalCloudOpenMetricsIntegrationAccounts" enabled
    And new "ListTemporalCloudOpenMetricsIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Temporal Cloud OpenMetrics account returns "Bad Request" response
    Given operation "UpdateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "UpdateTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "id": "7c2d4e91-5a3b-4f68-b0e2-9d1f6a8c3e57", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Temporal Cloud OpenMetrics account returns "Not Found" response
    Given operation "UpdateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "UpdateTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "id": "7c2d4e91-5a3b-4f68-b0e2-9d1f6a8c3e57", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Temporal Cloud OpenMetrics account returns "OK" response
    Given operation "UpdateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "UpdateTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "id": "7c2d4e91-5a3b-4f68-b0e2-9d1f6a8c3e57", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Temporal Cloud OpenMetrics account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateTemporalCloudOpenMetricsIntegrationAccount" enabled
    And new "UpdateTemporalCloudOpenMetricsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "temporal-cloud-prod", "settings": {"include_opt_in_labels": false, "namespaces_to_include": "prod-*,billing.a1b2c"}}, "id": "7c2d4e91-5a3b-4f68-b0e2-9d1f6a8c3e57", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
