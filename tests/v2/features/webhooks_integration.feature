@endpoint(webhooks-integration) @endpoint(webhooks-integration-v2)
Feature: Webhooks Integration
  Configure your [Datadog Webhooks
  integration](https://docs.datadoghq.com/integrations/webhooks/) directly
  through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "WebhooksIntegration" API

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create an OAuth2 client credentials auth method returns "Bad Request" response
    Given new "CreateOAuth2ClientCredentials" request
    And body with value {"data": {"attributes": {"access_token_url": "https://example.com/oauth/token", "audience": "https://api.example.com", "client_id": "my-client-id", "client_secret": "my-client-secret", "name": "my-oauth2-auth", "scope": "read:webhooks write:webhooks"}, "type": "webhooks-auth-method-oauth2-client-credentials"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create an OAuth2 client credentials auth method returns "CREATED" response
    Given new "CreateOAuth2ClientCredentials" request
    And body with value {"data": {"attributes": {"access_token_url": "https://example.com/oauth/token", "audience": "https://api.example.com", "client_id": "my-client-id", "client_secret": "my-client-secret", "name": "my-oauth2-auth", "scope": "read:webhooks write:webhooks"}, "type": "webhooks-auth-method-oauth2-client-credentials"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create an OAuth2 client credentials auth method returns "Conflict" response
    Given new "CreateOAuth2ClientCredentials" request
    And body with value {"data": {"attributes": {"access_token_url": "https://example.com/oauth/token", "audience": "https://api.example.com", "client_id": "my-client-id", "client_secret": "my-client-secret", "name": "my-oauth2-auth", "scope": "read:webhooks write:webhooks"}, "type": "webhooks-auth-method-oauth2-client-credentials"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete an OAuth2 client credentials auth method returns "Not Found" response
    Given new "DeleteOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete an OAuth2 client credentials auth method returns "OK" response
    Given new "DeleteOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all auth methods returns "OK" response
    Given new "GetAllAuthMethods" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get an OAuth2 client credentials auth method returns "Not Found" response
    Given new "GetOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get an OAuth2 client credentials auth method returns "OK" response
    Given new "GetOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an OAuth2 client credentials auth method returns "Bad Request" response
    Given new "UpdateOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"access_token_url": "https://example.com/oauth/token", "audience": "https://api.example.com", "client_id": "my-client-id", "client_secret": "my-client-secret", "name": "my-oauth2-auth", "scope": "read:webhooks write:webhooks"}, "type": "webhooks-auth-method-oauth2-client-credentials"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an OAuth2 client credentials auth method returns "Conflict" response
    Given new "UpdateOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"access_token_url": "https://example.com/oauth/token", "audience": "https://api.example.com", "client_id": "my-client-id", "client_secret": "my-client-secret", "name": "my-oauth2-auth", "scope": "read:webhooks write:webhooks"}, "type": "webhooks-auth-method-oauth2-client-credentials"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an OAuth2 client credentials auth method returns "Not Found" response
    Given new "UpdateOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"access_token_url": "https://example.com/oauth/token", "audience": "https://api.example.com", "client_id": "my-client-id", "client_secret": "my-client-secret", "name": "my-oauth2-auth", "scope": "read:webhooks write:webhooks"}, "type": "webhooks-auth-method-oauth2-client-credentials"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an OAuth2 client credentials auth method returns "OK" response
    Given new "UpdateOAuth2ClientCredentials" request
    And request contains "auth_method_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"access_token_url": "https://example.com/oauth/token", "audience": "https://api.example.com", "client_id": "my-client-id", "client_secret": "my-client-secret", "name": "my-oauth2-auth", "scope": "read:webhooks write:webhooks"}, "type": "webhooks-auth-method-oauth2-client-credentials"}}
    When the request is sent
    Then the response status is 200 OK
