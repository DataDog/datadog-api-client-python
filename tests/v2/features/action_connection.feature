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

  @team:DataDog/workflow-automation-dev
  Scenario: Create a new Action Connection returns "Bad Request" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"1"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/workflow-automation-dev
  Scenario: Create a new Action Connection returns "Successfully created Action Connection" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection {{ unique_lower_alnum }}","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection

  @team:DataDog/workflow-automation-dev
  Scenario: Create a new Action Connection with HTTPBasicAuth returns "Successfully created Action Connection" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"HTTP Basic Auth Connection {{ unique_lower_alnum }}","integration":{"type":"HTTP","base_url":"https://api.example.com","credentials":{"type":"HTTPBasicAuth","username":"test-user","password":"test-password"}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection

  @team:DataDog/workflow-automation-dev
  Scenario: Create a new Action Connection with HTTPMtlsAuth returns "Successfully created Action Connection" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"HTTP mTLS Connection {{ unique_lower_alnum }}","integration":{"type":"HTTP","base_url":"https://api.example.com","credentials":{"type":"HTTPMtlsAuth","certificate":"-----BEGIN CERTIFICATE-----\nMIICXjCCAUYCCQDOGcCfCHfhPzANBgkqhkiG9w0BAQsFADAzMQswCQYDVQQGEwJV\nUzELMAkGA1UECAwCQ0ExFTATBgNVBAoMDERhdGFkb2cgSW5jLjAeFw0yNDA1MTQw\nMDA1NThaFw0yNTA1MTQwMDA1NThaMDMxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJD\nQTEVMBMGA1UECgwMRGF0YWRvZyBJbmMuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A\nMIIBCgKCAQEAwQDTmLqWv2L6YhzBcjKgPEzd3kE+9dZ4hBXBCjK6HgF/3aOKOSYq\nM9KPFHgJj6SjUJ+8TqX4sV6yW5xGX8dKjOpTYQfExEjGYcVrqKoOGg2k6dGkHyGm\n2VzL4zKyK1C3zJ4KpJnMYK8dPPcgzJvO7jGxGKMgLVU3VNdxKGTrqKmC6RbZLQOz\nM3fLp7bF2VcJ6VkGKW+yBK6vVMbQKMvjTbGqr3vIRd8SZzKRTsyIzXQDKgOv2vPn\nSqYJjKFJ8vJ7JeH6zGyLjQ1cGVy9jJ3+TjJoJhCGOyGzJpBGIcXfYjFDLcSRh7KE\nQIDAQABo1MwUTAdBgNVHQ4EFgQU/V8vJkPJ8b9yQnC/9bJ2kJGJ5MjoyEwHwYDVR0j\nBBgwFoAU/V8vJkPJ8b9yQnC/9bJ2kJGJ5Mjo\n-----END CERTIFICATE-----","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDBaNOMV7V8T7gR\nOmNcNfqGHxPrLLo1w2J7J8h6S8bVD9yCH2JKV8J5G2J8J0V8J3Jg8b3Jg8LxJgV\nV8J6JgV8J9JgJg8LJg8VJgV5JgLLJgVVJg8V4Jg8VLJg8V6JgV8JqJgVV8J3JgV\nV8J7JgVV8J5JgVV8J8JgVVJg8LJgJVLJgLVJgVVJgLJgVVJgVVJgVVJgLVJgVV\nJgVVJgVVJgLJgVVJgLVJgLLJgVVJgVLJgVVJgVLJgVVJgVVJgVVJgVVJgVVJg\nVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJgVVJ\nAgMBAAECggEBAKoJkJJJJkJJkJ\n-----END PRIVATE KEY-----"}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection

  @team:DataDog/workflow-automation-dev
  Scenario: Create a new Action Connection with HTTPTokenAuth returns "Successfully created Action Connection" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"HTTP Token Connection {{ unique_lower_alnum }}","integration":{"type":"HTTP","base_url":"https://api.example.com","credentials":{"type":"HTTPTokenAuth","tokens":[{"name":"ApiKey","type":"SECRET","value":"secret-token-value"}],"headers":[{"name":"Authorization","value":"Bearer token-value"}]}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection

  @team:DataDog/workflow-automation-dev
  Scenario: Create a new Action Connection with invalid HTTPCredentials returns "Bad Request" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Invalid HTTP Connection","integration":{"type":"HTTP","base_url":"https://api.example.com","credentials":{"type":"HTTPBasicAuth","username":"test-user"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/workflow-automation-dev
  Scenario: Create a new Action Connection with missing base_url returns "Bad Request" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Missing Base URL Connection","integration":{"type":"HTTP","credentials":{"type":"HTTPBasicAuth","username":"test-user","password":"test-password"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/workflow-automation-dev
  Scenario: Delete an existing Action Connection returns "Not Found" response
    Given new "DeleteActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/workflow-automation-dev
  Scenario: Delete an existing Action Connection returns "The resource was deleted successfully." response
    Given there is a valid "action_connection" in the system
    And new "DeleteActionConnection" request
    And request contains "connection_id" parameter from "action_connection.data.id"
    When the request is sent
    Then the response status is 204 The resource was deleted successfully.

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing Action Connection returns "Bad Request" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "bad-format"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing Action Connection returns "Not Found" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing Action Connection returns "Successfully get Action Connection" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    When the request is sent
    Then the response status is 200 Successfully get Action Connection

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing App Key Registration returns "Bad request" response
    Given new "GetAppKeyRegistration" request
    And request contains "app_key_id" parameter with value "not_valid_app_key_id"
    When the request is sent
    Then the response status is 400 Bad request

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing App Key Registration returns "Not found" response
    Given new "GetAppKeyRegistration" request
    And request contains "app_key_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing App Key Registration returns "OK" response
    Given new "GetAppKeyRegistration" request
    And request contains "app_key_id" parameter with value "b7feea52-994e-4714-a100-1bd9eff5aee1"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/workflow-automation-dev
  Scenario: List App Key Registrations returns "Bad request" response
    Given new "ListAppKeyRegistrations" request
    When the request is sent
    Then the response status is 400 Bad request

  @team:DataDog/workflow-automation-dev
  Scenario: List App Key Registrations returns "OK" response
    Given new "ListAppKeyRegistrations" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/workflow-automation-dev
  Scenario: Register a new App Key returns "Bad request" response
    Given new "RegisterAppKey" request
    And request contains "app_key_id" parameter with value "not_valid_app_key_id"
    When the request is sent
    Then the response status is 400 Bad request

  @team:DataDog/workflow-automation-dev
  Scenario: Register a new App Key returns "Created" response
    Given new "RegisterAppKey" request
    And request contains "app_key_id" parameter with value "b7feea52-994e-4714-a100-1bd9eff5aee1"
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/workflow-automation-dev
  Scenario: Unregister an App Key returns "Bad request" response
    Given new "UnregisterAppKey" request
    And request contains "app_key_id" parameter with value "not_valid_app_key_id"
    When the request is sent
    Then the response status is 400 Bad request

  @skip @team:DataDog/workflow-automation-dev
  Scenario: Unregister an App Key returns "No Content" response
    Given new "UnregisterAppKey" request
    And request contains "app_key_id" parameter with value "57cc69ae-9214-4ecc-8df8-43ecc1d92d99"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/workflow-automation-dev
  Scenario: Unregister an App Key returns "Not found" response
    Given new "UnregisterAppKey" request
    And request contains "app_key_id" parameter with value "57cc69ae-9214-4ecc-8df8-43ecc1d92d99"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/workflow-automation-dev
  Scenario: Update an existing Action Connection returns "Bad Request" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"1"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/workflow-automation-dev
  Scenario: Update an existing Action Connection returns "Not Found" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/workflow-automation-dev
  Scenario: Update an existing Action Connection returns "Successfully updated Action Connection" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 200 Successfully updated Action Connection

  @team:DataDog/workflow-automation-dev
  Scenario: Update an existing Action Connection with HTTPBasicAuth returns "Successfully updated Action Connection" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"HTTP Basic Auth Updated","integration":{"type":"HTTP","base_url":"https://api.updated.com","credentials":{"type":"HTTPBasicAuth","username":"updated-user","password":"updated-password"}}}}}
    When the request is sent
    Then the response status is 200 Successfully updated Action Connection
