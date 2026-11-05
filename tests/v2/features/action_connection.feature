@endpoint(action-connection) @endpoint(action-connection-v2)
Feature: Action Connection
  Action connections extend your installed integrations and allow you to
  take action in your third-party systems (e.g. AWS, GitLab, and Statuspage)
  with Datadog’s Workflow Automation and App Builder products.  Datadog’s
  Integrations automatically provide authentication for Slack, Microsoft
  Teams, PagerDuty, Opsgenie, JIRA, GitHub, and Statuspage. You do not need
  additional connections in order to access these tools within Workflow
  Automation and App Builder.  We offer granular access control for editing
  and resolving connections.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ActionConnection" API

  @team:ddoghq/action-platform
  Scenario: Create a GCP Action Connection with AWS Secrets Manager references
    Given there is a valid "action_connection" in the system
    And new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"GCP Secrets Manager Connection {{ unique_lower_alnum }}","external_secrets_manager":{"type":"aws_secrets_manager","connection_id":"{{ action_connection.data.id }}","region":"us-east-1"},"integration":{"type":"GCP","credentials":{"type":"GCPServiceAccount","private_key":{"type":"aws_secrets_manager","secret_id":"example/gcp/service-account","key":"private_key"},"service_account_email":{"type":"aws_secrets_manager","secret_id":"example/gcp/service-account","key":"client_email"}}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection
    And the response "data.attributes.external_secrets_manager.connection_id" has the same value as "action_connection.data.id"
    And the response "data.attributes.external_secrets_manager.region" is equal to "us-east-1"
    And the response "data.attributes.integration.credentials.private_key.secret_id" is equal to "example/gcp/service-account"
    And the response "data.attributes.integration.credentials.private_key.key" is equal to "private_key"
    And the response "data.attributes.integration.credentials.service_account_email.key" is equal to "client_email"

  @team:ddoghq/action-platform
  Scenario: Create a new Action Connection returns "Bad Request" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"1"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/action-platform
  Scenario: Create a new Action Connection returns "Successfully created Action Connection" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection {{ unique_lower_alnum }}","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection

  @team:ddoghq/action-platform
  Scenario: Create an Action Connection rejects AWS references without connection-level settings
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Missing Secrets Manager Settings {{ unique_lower_alnum }}","integration":{"type":"Anthropic","credentials":{"type":"AnthropicAPIKey","api_token":{"type":"aws_secrets_manager","secret_id":"example/anthropic","key":"api_token"}}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/action-platform
  Scenario: Create an Action Connection rejects conflicting AWS secret version selectors
    Given there is a valid "action_connection" in the system
    And new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Conflicting Secrets Manager Versions {{ unique_lower_alnum }}","external_secrets_manager":{"type":"aws_secrets_manager","connection_id":"{{ action_connection.data.id }}","region":"us-east-1"},"integration":{"type":"Anthropic","credentials":{"type":"AnthropicAPIKey","api_token":{"type":"aws_secrets_manager","secret_id":"example/anthropic","key":"api_token","version_id":"example-version","version_stage":"AWSCURRENT"}}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/action-platform
  Scenario: Create an Anthropic Action Connection with an AWS Secrets Manager API token
    Given there is a valid "action_connection" in the system
    And new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Anthropic Secrets Manager Connection {{ unique_lower_alnum }}","external_secrets_manager":{"type":"aws_secrets_manager","connection_id":"{{ action_connection.data.id }}","region":"us-east-1"},"integration":{"type":"Anthropic","credentials":{"type":"AnthropicAPIKey","api_token":{"type":"aws_secrets_manager","secret_id":"example/anthropic","key":"api_token"}}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection
    And the response "data.attributes.external_secrets_manager.connection_id" has the same value as "action_connection.data.id"
    And the response "data.attributes.integration.credentials.api_token.type" is equal to "aws_secrets_manager"
    And the response "data.attributes.integration.credentials.api_token.key" is equal to "api_token"

  @team:ddoghq/action-platform
  Scenario: Create an HTTP Action Connection with an AWS Secrets Manager token
    Given there is a valid "action_connection" in the system
    And new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"HTTP Secrets Manager Connection {{ unique_lower_alnum }}","external_secrets_manager":{"type":"aws_secrets_manager","connection_id":"{{ action_connection.data.id }}","region":"us-east-1"},"integration":{"type":"HTTP","base_url":"https://example.com","credentials":{"type":"HTTPTokenAuth","tokens":[{"name":"token","type":"SECRET","value":{"type":"aws_secrets_manager","secret_id":"example/http","key":"token"}}],"headers":[{"name":"ApiKey","value":"literal-value"}],"url_parameters":[{"name":"apiKey","value":"literal-value"}],"body":{"content_type":"application/json","content":"{\"example\":\"literal\"}"}}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection
    And the response "data.attributes.external_secrets_manager.connection_id" has the same value as "action_connection.data.id"
    And the response "data.attributes.integration.base_url" is equal to "https://example.com"
    And the response "data.attributes.integration.credentials.http_tokens[0].value.type" is equal to "aws_secrets_manager"
    And the response "data.attributes.integration.credentials.http_tokens[0].value.key" is equal to "token"

  @team:ddoghq/action-platform
  Scenario: Delete an existing Action Connection returns "Not Found" response
    Given new "DeleteActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/action-platform
  Scenario: Delete an existing Action Connection returns "The resource was deleted successfully." response
    Given there is a valid "action_connection" in the system
    And new "DeleteActionConnection" request
    And request contains "connection_id" parameter from "action_connection.data.id"
    When the request is sent
    Then the response status is 204 The resource was deleted successfully.

  @team:ddoghq/action-platform
  Scenario: Get a GCP Action Connection preserves AWS Secrets Manager references
    Given there is a valid "action_connection" in the system
    And there is a valid "gcp_action_connection" in the system
    And new "GetActionConnection" request
    And request contains "connection_id" parameter from "gcp_action_connection.data.id"
    When the request is sent
    Then the response status is 200 Successfully get Action Connection
    And the response "data.attributes.external_secrets_manager.connection_id" has the same value as "action_connection.data.id"
    And the response "data.attributes.integration.credentials.private_key.type" is equal to "aws_secrets_manager"
    And the response "data.attributes.integration.credentials.private_key.key" is equal to "private_key"
    And the response "data.attributes.integration.credentials.service_account_email.key" is equal to "client_email"

  @team:ddoghq/action-platform
  Scenario: Get an existing Action Connection returns "Bad Request" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "bad-format"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/action-platform
  Scenario: Get an existing Action Connection returns "Not Found" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/action-platform
  Scenario: Get an existing Action Connection returns "Successfully get Action Connection" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    When the request is sent
    Then the response status is 200 Successfully get Action Connection

  @team:ddoghq/action-platform
  Scenario: Get an existing App Key Registration returns "Bad request" response
    Given new "GetAppKeyRegistration" request
    And request contains "app_key_id" parameter with value "not_valid_app_key_id"
    When the request is sent
    Then the response status is 400 Bad request

  @team:ddoghq/action-platform
  Scenario: Get an existing App Key Registration returns "Not found" response
    Given new "GetAppKeyRegistration" request
    And request contains "app_key_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not found

  @team:ddoghq/action-platform
  Scenario: Get an existing App Key Registration returns "OK" response
    Given new "GetAppKeyRegistration" request
    And request contains "app_key_id" parameter with value "b7feea52-994e-4714-a100-1bd9eff5aee1"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/action-platform
  Scenario: List App Key Registrations returns "Bad request" response
    Given new "ListAppKeyRegistrations" request
    When the request is sent
    Then the response status is 400 Bad request

  @team:ddoghq/action-platform
  Scenario: List App Key Registrations returns "OK" response
    Given new "ListAppKeyRegistrations" request
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/action-platform
  Scenario: Register a new App Key returns "Bad request" response
    Given new "RegisterAppKey" request
    And request contains "app_key_id" parameter with value "not_valid_app_key_id"
    When the request is sent
    Then the response status is 400 Bad request

  @team:ddoghq/action-platform
  Scenario: Register a new App Key returns "Created" response
    Given new "RegisterAppKey" request
    And request contains "app_key_id" parameter with value "b7feea52-994e-4714-a100-1bd9eff5aee1"
    When the request is sent
    Then the response status is 201 Created

  @team:ddoghq/action-platform
  Scenario: Unregister an App Key returns "Bad request" response
    Given new "UnregisterAppKey" request
    And request contains "app_key_id" parameter with value "not_valid_app_key_id"
    When the request is sent
    Then the response status is 400 Bad request

  @skip @team:ddoghq/action-platform
  Scenario: Unregister an App Key returns "No Content" response
    Given new "UnregisterAppKey" request
    And request contains "app_key_id" parameter with value "57cc69ae-9214-4ecc-8df8-43ecc1d92d99"
    When the request is sent
    Then the response status is 204 No Content

  @team:ddoghq/action-platform
  Scenario: Unregister an App Key returns "Not found" response
    Given new "UnregisterAppKey" request
    And request contains "app_key_id" parameter with value "57cc69ae-9214-4ecc-8df8-43ecc1d92d99"
    When the request is sent
    Then the response status is 404 Not found

  @team:ddoghq/action-platform
  Scenario: Update a GCP Action Connection with a versioned AWS Secrets Manager reference
    Given there is a valid "action_connection" in the system
    And there is a valid "gcp_action_connection" in the system
    And new "UpdateActionConnection" request
    And request contains "connection_id" parameter from "gcp_action_connection.data.id"
    And body with value {"data":{"type":"action_connection","attributes":{"external_secrets_manager":{"type":"aws_secrets_manager","connection_id":"{{ action_connection.data.id }}","region":"us-east-1"},"integration":{"type":"GCP","credentials":{"type":"GCPServiceAccount","private_key":{"type":"aws_secrets_manager","secret_id":"example/gcp/service-account","key":"private_key","version_stage":"AWSCURRENT"},"service_account_email":{"type":"aws_secrets_manager","secret_id":"example/gcp/service-account","key":"client_email"}}}}}}
    When the request is sent
    Then the response status is 200 Successfully updated Action Connection
    And the response "data.attributes.external_secrets_manager.connection_id" has the same value as "action_connection.data.id"
    And the response "data.id" has the same value as "gcp_action_connection.data.id"
    And the response "data.attributes.integration.credentials.private_key.version_stage" is equal to "AWSCURRENT"
    And the response "data.attributes.integration.credentials.private_key.key" is equal to "private_key"
    And the response "data.attributes.integration.credentials.service_account_email.key" is equal to "client_email"

  @team:ddoghq/action-platform
  Scenario: Update an existing Action Connection returns "Bad Request" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"1"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/action-platform
  Scenario: Update an existing Action Connection returns "Not Found" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/action-platform
  Scenario: Update an existing Action Connection returns "Successfully updated Action Connection" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 200 Successfully updated Action Connection
