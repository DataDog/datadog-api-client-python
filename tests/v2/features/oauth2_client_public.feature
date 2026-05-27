@endpoint(oauth2-client-public) @endpoint(oauth2-client-public-v2)
Feature: OAuth2 Client Public
  Configure OAuth2 clients for Datadog. Supports RFC 7591 Dynamic Client
  Registration and management of OAuth2 client scopes restrictions.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OAuth2ClientPublic" API

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an OAuth2 client scopes restriction returns "Bad Request" response
    Given operation "DeleteScopesRestriction" enabled
    And new "DeleteScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an OAuth2 client scopes restriction returns "No Content" response
    Given operation "DeleteScopesRestriction" enabled
    And new "DeleteScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an OAuth2 client scopes restriction returns "Not Found" response
    Given operation "DeleteScopesRestriction" enabled
    And new "DeleteScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an OAuth2 client scopes restriction returns "Bad Request" response
    Given operation "GetScopesRestriction" enabled
    And new "GetScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an OAuth2 client scopes restriction returns "Not Found" response
    Given operation "GetScopesRestriction" enabled
    And new "GetScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an OAuth2 client scopes restriction returns "OK" response
    Given operation "GetScopesRestriction" enabled
    And new "GetScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Register an OAuth2 client returns "Bad Request" response
    Given operation "RegisterOAuthClient" enabled
    And new "RegisterOAuthClient" request
    And body with value {"client_name": "Example MCP Client", "client_uri": "https://example.com", "grant_types": ["authorization_code", "refresh_token"], "jwks_uri": "https://example.com/.well-known/jwks.json", "logo_uri": "https://example.com/logo.png", "policy_uri": "https://example.com/privacy", "redirect_uris": ["https://example.com/oauth/callback"], "response_types": ["code"], "scope": "openid profile", "token_endpoint_auth_method": "none", "tos_uri": "https://example.com/tos"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Register an OAuth2 client returns "Created" response
    Given operation "RegisterOAuthClient" enabled
    And new "RegisterOAuthClient" request
    And body with value {"client_name": "Example MCP Client", "client_uri": "https://example.com", "grant_types": ["authorization_code", "refresh_token"], "jwks_uri": "https://example.com/.well-known/jwks.json", "logo_uri": "https://example.com/logo.png", "policy_uri": "https://example.com/privacy", "redirect_uris": ["https://example.com/oauth/callback"], "response_types": ["code"], "scope": "openid profile", "token_endpoint_auth_method": "none", "tos_uri": "https://example.com/tos"}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Upsert an OAuth2 client scopes restriction returns "Bad Request" response
    Given operation "UpsertScopesRestriction" enabled
    And new "UpsertScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"oidc_scopes": ["openid", "email"], "permission_scopes": ["dashboards_read", "metrics_read"]}, "type": "upsert_scopes_restriction"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Upsert an OAuth2 client scopes restriction returns "Not Found" response
    Given operation "UpsertScopesRestriction" enabled
    And new "UpsertScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"oidc_scopes": ["openid", "email"], "permission_scopes": ["dashboards_read", "metrics_read"]}, "type": "upsert_scopes_restriction"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Upsert an OAuth2 client scopes restriction returns "OK" response
    Given operation "UpsertScopesRestriction" enabled
    And new "UpsertScopesRestriction" request
    And request contains "client_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"oidc_scopes": ["openid", "email"], "permission_scopes": ["dashboards_read", "metrics_read"]}, "type": "upsert_scopes_restriction"}}
    When the request is sent
    Then the response status is 200 OK
