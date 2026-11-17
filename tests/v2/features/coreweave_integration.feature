@endpoint(coreweave-integration) @endpoint(coreweave-integration-v2)
Feature: CoreWeave Integration
  Manage your Datadog CoreWeave integration accounts and account resources
  directly through the Datadog API. See the [CoreWeave integration
  page](https://docs.datadoghq.com/integrations/coreweave/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CoreWeaveIntegration" API

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a CoreWeave integration account returns "Bad Request" response
    Given operation "CreateCoreWeaveCloudIntegrationAccount" enabled
    And new "CreateCoreWeaveCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a CoreWeave integration account returns "Created" response
    Given operation "CreateCoreWeaveCloudIntegrationAccount" enabled
    And new "CreateCoreWeaveCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a CoreWeave integration account returns "Not Found" response
    Given operation "CreateCoreWeaveCloudIntegrationAccount" enabled
    And new "CreateCoreWeaveCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a CoreWeave integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateCoreWeaveCloudIntegrationAccount" enabled
    And new "CreateCoreWeaveCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Delete a CoreWeave integration account returns "Bad Request" response
    Given operation "DeleteCoreWeaveCloudIntegrationAccount" enabled
    And new "DeleteCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Delete a CoreWeave integration account returns "Not Found" response
    Given operation "DeleteCoreWeaveCloudIntegrationAccount" enabled
    And new "DeleteCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Delete a CoreWeave integration account returns "OK" response
    Given operation "DeleteCoreWeaveCloudIntegrationAccount" enabled
    And new "DeleteCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Get a CoreWeave integration account returns "Bad Request" response
    Given operation "GetCoreWeaveCloudIntegrationAccount" enabled
    And new "GetCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Get a CoreWeave integration account returns "Not Found" response
    Given operation "GetCoreWeaveCloudIntegrationAccount" enabled
    And new "GetCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Get a CoreWeave integration account returns "OK" response
    Given operation "GetCoreWeaveCloudIntegrationAccount" enabled
    And new "GetCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: List CoreWeave integration accounts returns "Bad Request" response
    Given operation "ListCoreWeaveCloudIntegrationAccounts" enabled
    And new "ListCoreWeaveCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: List CoreWeave integration accounts returns "Not Found" response
    Given operation "ListCoreWeaveCloudIntegrationAccounts" enabled
    And new "ListCoreWeaveCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: List CoreWeave integration accounts returns "OK" response
    Given operation "ListCoreWeaveCloudIntegrationAccounts" enabled
    And new "ListCoreWeaveCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a CoreWeave integration account returns "Bad Request" response
    Given operation "UpdateCoreWeaveCloudIntegrationAccount" enabled
    And new "UpdateCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "id": "f7a8b9c0-d1e2-4f3a-9b4c-5d6e7f8091a2", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a CoreWeave integration account returns "Not Found" response
    Given operation "UpdateCoreWeaveCloudIntegrationAccount" enabled
    And new "UpdateCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "id": "f7a8b9c0-d1e2-4f3a-9b4c-5d6e7f8091a2", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a CoreWeave integration account returns "OK" response
    Given operation "UpdateCoreWeaveCloudIntegrationAccount" enabled
    And new "UpdateCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "id": "f7a8b9c0-d1e2-4f3a-9b4c-5d6e7f8091a2", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a CoreWeave integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateCoreWeaveCloudIntegrationAccount" enabled
    And new "UpdateCoreWeaveCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_token": "CW-SECRET-xxxxxxxxxxxxxxxxxxxx", "auth_type": "coreweave_api_token"}, "dataflows": {"coreweave-cloud-logs": {"enabled": true}, "coreweave-cloud-metrics": {"enabled": true}}, "name": "coreweave-prod", "settings": {"account_tags": ["env:prod", "team:gpu"], "cluster_filters": ["cluster:prod-*", "!cluster:dev"]}}, "id": "f7a8b9c0-d1e2-4f3a-9b4c-5d6e7f8091a2", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
