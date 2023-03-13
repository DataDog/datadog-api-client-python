@endpoint(fastly-integration) @endpoint(fastly-integration-v2)
Feature: Fastly Integration
  Configure your Datadog Fastly integration directly through the Datadog
  API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "FastlyIntegration" API

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Fastly account returns "Bad Request" response
    Given new "CreateFastlyAccount" request
    And body with value {"data": {"attributes": {"api_key": "ABCDEFG123", "name": "test-name", "services": [{"id": "6abc7de6893AbcDe9fghIj", "tags": ["myTag", "myTag2:myValue"]}]}, "type": "fastly-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/web-integrations
  Scenario: Add Fastly account returns "CREATED" response
    Given new "CreateFastlyAccount" request
    And body with value {"data": {"attributes": {"api_key": "{{ unique_alnum }}", "name": "{{ unique }}", "services": []}, "type": "fastly-accounts"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.type" is equal to "fastly-accounts"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.services" has length 0

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Fastly account returns "Not Found" response
    Given new "CreateFastlyAccount" request
    And body with value {"data": {"attributes": {"api_key": "ABCDEFG123", "name": "test-name", "services": [{"id": "6abc7de6893AbcDe9fghIj", "tags": ["myTag", "myTag2:myValue"]}]}, "type": "fastly-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Fastly service returns "Bad Request" response
    Given new "CreateFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"tags": ["myTag", "myTag2:myValue"]}, "id": "abc123", "type": "fastly-services"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Fastly service returns "CREATED" response
    Given new "CreateFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"tags": ["myTag", "myTag2:myValue"]}, "id": "abc123", "type": "fastly-services"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Fastly service returns "Not Found" response
    Given new "CreateFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"tags": ["myTag", "myTag2:myValue"]}, "id": "abc123", "type": "fastly-services"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Fastly account returns "Bad Request" response
    Given new "DeleteFastlyAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Fastly account returns "Not Found" response
    Given new "DeleteFastlyAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Fastly account returns "OK" response
    Given new "DeleteFastlyAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Fastly service returns "Bad Request" response
    Given new "DeleteFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Fastly service returns "Not Found" response
    Given new "DeleteFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Fastly service returns "OK" response
    Given new "DeleteFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Fastly account returns "Bad Request" response
    Given new "GetFastlyAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Fastly account returns "Not Found" response
    Given new "GetFastlyAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: Get Fastly account returns "OK" response
    Given there is a valid "fastly_account" in the system
    And new "GetFastlyAccount" request
    And request contains "account_id" parameter from "fastly_account.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "fastly-accounts"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.services" has length 0

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Fastly service returns "Bad Request" response
    Given new "GetFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Fastly service returns "Not Found" response
    Given new "GetFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Fastly service returns "OK" response
    Given new "GetFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Fastly accounts returns "Bad Request" response
    Given new "ListFastlyAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Fastly accounts returns "Not Found" response
    Given new "ListFastlyAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: List Fastly accounts returns "OK" response
    Given there is a valid "fastly_account" in the system
    And new "ListFastlyAccounts" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "fastly-accounts"

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Fastly services returns "Bad Request" response
    Given new "ListFastlyServices" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Fastly services returns "Not Found" response
    Given new "ListFastlyServices" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Fastly services returns "OK" response
    Given new "ListFastlyServices" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Fastly account returns "Bad Request" response
    Given new "UpdateFastlyAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "ABCDEFG123"}, "type": "fastly-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Fastly account returns "Not Found" response
    Given new "UpdateFastlyAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "ABCDEFG123"}, "type": "fastly-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: Update Fastly account returns "OK" response
    Given there is a valid "fastly_account" in the system
    And new "UpdateFastlyAccount" request
    And request contains "account_id" parameter from "fastly_account.data.id"
    And body with value {"data": {"attributes": {"api_key": "update-secret"}, "type": "fastly-accounts"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{fastly_account.data.id }}"
    And the response "data.attributes.name" is equal to "{{fastly_account.data.attributes.name }}"

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Fastly service returns "Bad Request" response
    Given new "UpdateFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"tags": ["myTag", "myTag2:myValue"]}, "id": "abc123", "type": "fastly-services"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Fastly service returns "Not Found" response
    Given new "UpdateFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"tags": ["myTag", "myTag2:myValue"]}, "id": "abc123", "type": "fastly-services"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Fastly service returns "OK" response
    Given new "UpdateFastlyService" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"tags": ["myTag", "myTag2:myValue"]}, "id": "abc123", "type": "fastly-services"}}
    When the request is sent
    Then the response status is 200 OK
