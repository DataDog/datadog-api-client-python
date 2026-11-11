@endpoint(nebius-cloud-integration) @endpoint(nebius-cloud-integration-v2)
Feature: Nebius Cloud Integration
  Manage your Datadog Nebius Cloud integration accounts and account
  resources directly through the Datadog API. See the [Nebius Cloud
  integration page](https://docs.datadoghq.com/integrations/nebius_cloud/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "NebiusCloudIntegration" API

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a Nebius Cloud integration account returns "Bad Request" response
    Given operation "CreateNebiusCloudIntegrationAccount" enabled
    And new "CreateNebiusCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a Nebius Cloud integration account returns "Created" response
    Given operation "CreateNebiusCloudIntegrationAccount" enabled
    And new "CreateNebiusCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a Nebius Cloud integration account returns "Not Found" response
    Given operation "CreateNebiusCloudIntegrationAccount" enabled
    And new "CreateNebiusCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Create a Nebius Cloud integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateNebiusCloudIntegrationAccount" enabled
    And new "CreateNebiusCloudIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Delete a Nebius Cloud integration account returns "Bad Request" response
    Given operation "DeleteNebiusCloudIntegrationAccount" enabled
    And new "DeleteNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Delete a Nebius Cloud integration account returns "Not Found" response
    Given operation "DeleteNebiusCloudIntegrationAccount" enabled
    And new "DeleteNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Delete a Nebius Cloud integration account returns "OK" response
    Given operation "DeleteNebiusCloudIntegrationAccount" enabled
    And new "DeleteNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Get a Nebius Cloud integration account returns "Bad Request" response
    Given operation "GetNebiusCloudIntegrationAccount" enabled
    And new "GetNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Get a Nebius Cloud integration account returns "Not Found" response
    Given operation "GetNebiusCloudIntegrationAccount" enabled
    And new "GetNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Get a Nebius Cloud integration account returns "OK" response
    Given operation "GetNebiusCloudIntegrationAccount" enabled
    And new "GetNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: List Nebius Cloud integration accounts returns "Bad Request" response
    Given operation "ListNebiusCloudIntegrationAccounts" enabled
    And new "ListNebiusCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: List Nebius Cloud integration accounts returns "Not Found" response
    Given operation "ListNebiusCloudIntegrationAccounts" enabled
    And new "ListNebiusCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: List Nebius Cloud integration accounts returns "OK" response
    Given operation "ListNebiusCloudIntegrationAccounts" enabled
    And new "ListNebiusCloudIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a Nebius Cloud integration account returns "Bad Request" response
    Given operation "UpdateNebiusCloudIntegrationAccount" enabled
    And new "UpdateNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "id": "e5f6a7b8-c9d0-4e1f-8a2b-3c4d5e6f7081", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a Nebius Cloud integration account returns "Not Found" response
    Given operation "UpdateNebiusCloudIntegrationAccount" enabled
    And new "UpdateNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "id": "e5f6a7b8-c9d0-4e1f-8a2b-3c4d5e6f7081", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a Nebius Cloud integration account returns "OK" response
    Given operation "UpdateNebiusCloudIntegrationAccount" enabled
    And new "UpdateNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "id": "e5f6a7b8-c9d0-4e1f-8a2b-3c4d5e6f7081", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/emerging-cloud-integrations
  Scenario: Update a Nebius Cloud integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateNebiusCloudIntegrationAccount" enabled
    And new "UpdateNebiusCloudIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "nebius_service_account", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----", "public_key_id": "publickey-yyyyyyyy", "service_account_id": "serviceaccount-xxxxxxxx", "static_api_key": "eyJhbGciOi...static-api-key"}, "dataflows": {"nebius-cloud-cost-collection": {"enabled": true, "settings": {"access_key_id": "AKID0123456789ABCDEF", "access_key_secret": "wJalrXUtnFEMIstaticaccesskey", "bucket_name": "nebius-cost-exports", "bucket_prefix_path": "cost-export/2026/", "bucket_region": "eu-north1"}}, "nebius-cloud-logs": {"enabled": true, "settings": {"enabled_services": ["nebius-cloud-compute", "nebius-cloud-kubernetes", "default"]}}, "nebius-cloud-resources": {"enabled": true}, "nebius-cloud-service-quota-collection": {"enabled": true}}, "name": "nebius-prod", "settings": {"account_tags": ["env:prod", "team:ai"], "tenant_id": "tenant-12345678"}}, "id": "e5f6a7b8-c9d0-4e1f-8a2b-3c4d5e6f7081", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
