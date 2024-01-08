@endpoint(cloudflare-integration) @endpoint(cloudflare-integration-v2)
Feature: Cloudflare Integration
  Configure your Datadog Cloudflare integration directly through the Datadog
  API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudflareIntegration" API

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Cloudflare account returns "Bad Request" response
    Given new "CreateCloudflareAccount" request
    And body with value {"data": {"attributes": {"api_key": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3", "email": "test-email@example.com", "name": "test-name", "resources": ["web", "dns"], "zones": ["zone_id_1", "zone_id_2"]}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/web-integrations
  Scenario: Add Cloudflare account returns "Bad Request" response due to missing email
    Given new "CreateCloudflareAccount" request
    And body with value {"data": {"attributes": {"api_key": "fakekey", "name": "{{ unique_lower_alnum }}"}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/web-integrations
  Scenario: Add Cloudflare account returns "Bad Request" response using invalid auth key
    Given new "CreateCloudflareAccount" request
    And body with value {"data": {"attributes": {"api_key": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "name": "{{ unique_lower_alnum }}"}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/web-integrations
  Scenario: Add Cloudflare account returns "CREATED" response
    Given new "CreateCloudflareAccount" request
    And body with value {"data": {"attributes": {"api_key": "fakekey", "email": "dev@datadoghq.com", "name": "{{ unique_lower_alnum }}"}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.type" is equal to "cloudflare-accounts"
    And the response "data.attributes.email" is equal to "dev@datadoghq.com"
    And the response "data.attributes.name" is equal to "{{ unique_lower_alnum }}"

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Cloudflare account returns "Not Found" response
    Given new "CreateCloudflareAccount" request
    And body with value {"data": {"attributes": {"api_key": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3", "email": "test-email@example.com", "name": "test-name", "resources": ["web", "dns"], "zones": ["zone_id_1", "zone_id_2"]}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Cloudflare account returns "Bad Request" response
    Given new "DeleteCloudflareAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Cloudflare account returns "Not Found" response
    Given new "DeleteCloudflareAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Cloudflare account returns "OK" response
    Given new "DeleteCloudflareAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Cloudflare account returns "Bad Request" response
    Given new "GetCloudflareAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Cloudflare account returns "Not Found" response
    Given new "GetCloudflareAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/web-integrations
  Scenario: Get Cloudflare account returns "OK" response
    Given there is a valid "cloudflare_account" in the system
    And new "GetCloudflareAccount" request
    And request contains "account_id" parameter from "cloudflare_account.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "cloudflare-accounts"
    And the response "data.attributes.email" is equal to "dev@datadog.com"
    And the response "data.attributes.name" is equal to "{{ unique_lower_alnum }}"

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Cloudflare accounts returns "Bad Request" response
    Given new "ListCloudflareAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Cloudflare accounts returns "Not Found" response
    Given new "ListCloudflareAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/web-integrations
  Scenario: List Cloudflare accounts returns "OK" response
    Given there is a valid "cloudflare_account" in the system
    And new "ListCloudflareAccounts" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "cloudflare-accounts"

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Cloudflare account returns "Bad Request" response
    Given new "UpdateCloudflareAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3", "email": "test-email@example.com", "resources": ["web", "dns"], "zones": ["zone_id_1", "zone_id_2"]}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/web-integrations
  Scenario: Update Cloudflare account returns "Bad Request" response due to invalid api key
    Given there is a valid "cloudflare_account" in the system
    And new "UpdateCloudflareAccount" request
    And request contains "account_id" parameter from "cloudflare_account.data.id"
    And body with value {"data": {"attributes": {"api_key": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/web-integrations
  Scenario: Update Cloudflare account returns "Bad Request" response due to missing required email
    Given there is a valid "cloudflare_account" in the system
    And new "UpdateCloudflareAccount" request
    And request contains "account_id" parameter from "cloudflare_account.data.id"
    And body with value {"data": {"attributes": {"api_key": "fakekey"}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Cloudflare account returns "Not Found" response
    Given new "UpdateCloudflareAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3", "email": "test-email@example.com", "resources": ["web", "dns"], "zones": ["zone_id_1", "zone_id_2"]}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/web-integrations
  Scenario: Update Cloudflare account returns "OK" response
    Given there is a valid "cloudflare_account" in the system
    And new "UpdateCloudflareAccount" request
    And request contains "account_id" parameter from "cloudflare_account.data.id"
    And body with value {"data": {"attributes": {"api_key": "fakekey", "email": "dev@datadoghq.com", "zones": ["zone-id-3"]}, "type": "cloudflare-accounts"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{cloudflare_account.data.attributes.name }}"
    And the response "data.attributes.zones" array contains value "zone-id-3"
