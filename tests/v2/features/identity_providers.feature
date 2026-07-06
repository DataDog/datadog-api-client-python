@endpoint(identity-providers) @endpoint(identity-providers-v2)
Feature: Identity Providers
  Manage identity providers and user authentication method overrides.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IdentityProviders" API

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List identity providers returns "OK" response
    Given new "ListIdentityProviders" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List users with an identity provider override returns "Bad Request" response
    Given new "ListIdentityProviderUsers" request
    And request contains "idp_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List users with an identity provider override returns "Not found" response
    Given new "ListIdentityProviderUsers" request
    And request contains "idp_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List users with an identity provider override returns "OK" response
    Given new "ListIdentityProviderUsers" request
    And request contains "idp_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login @with-pagination
  Scenario: List users with an identity provider override returns "OK" response with pagination
    Given new "ListIdentityProviderUsers" request
    And request contains "idp_id" parameter from "REPLACE.ME"
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Update an identity provider returns "Bad Request" response
    Given new "UpdateIdentityProvider" request
    And request contains "idp_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true}, "id": "00000000-0000-0000-0000-000000000001", "type": "identity_providers"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Update an identity provider returns "Not found" response
    Given new "UpdateIdentityProvider" request
    And request contains "idp_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true}, "id": "00000000-0000-0000-0000-000000000001", "type": "identity_providers"}}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Update an identity provider returns "OK" response
    Given new "UpdateIdentityProvider" request
    And request contains "idp_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true}, "id": "00000000-0000-0000-0000-000000000001", "type": "identity_providers"}}
    When the request is sent
    Then the response status is 200 OK
