@endpoint(okta-integration) @endpoint(okta-integration-v2)
Feature: Okta Integration
  Configure your Datadog Okta integration directly through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OktaIntegration" API

  @replay-only @team:Datadog/web-integrations
  Scenario: Okta Public - Add account returns "Bad Request" response
    Given new "CreateOktaAccount" request
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - Add account returns "Not Found" response
    Given new "CreateOktaAccount" request
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/web-integrations
  Scenario: Okta Public - Add account returns "OK" response
    Given new "CreateOktaAccount" request
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod", "client_id": "client_id", "client_secret":"client_secret"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - Delete account returns "Bad Request" response
    Given new "DeleteOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - Delete account returns "Not Found" response
    Given new "DeleteOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - Delete account returns "OK" response
    Given new "DeleteOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - Get account returns "Bad Request" response
    Given new "GetOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - Get account returns "Not Found" response
    Given new "GetOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/web-integrations
  Scenario: Okta Public - Get account returns "OK" response
    Given new "GetOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - List accounts returns "Bad Request" response
    Given new "ListOktaAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - List accounts returns "Not Found" response
    Given new "ListOktaAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/web-integrations
  Scenario: Okta Public - List accounts returns "OK" response
    Given new "ListOktaAccounts" request
    When the request is sent
    Then the response status is 201 OK

  @replay-only @team:Datadog/web-integrations
  Scenario: Okta Public - Update account returns "Bad Request" response
    Given new "UpdateOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Okta Public - Update account returns "Not Found" response
    Given new "UpdateOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/web-integrations
  Scenario: Okta Public - Update account returns "OK" response
    Given new "UpdateOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 200 OK
