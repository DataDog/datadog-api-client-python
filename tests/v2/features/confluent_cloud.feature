@endpoint(confluent-cloud) @endpoint(confluent-cloud-v2)
Feature: Confluent Cloud
  Configure your Datadog Confluent Cloud integration directly through the
  Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ConfluentCloud" API

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Confluent account returns "Bad Request" response
    Given new "CreateConfluentAccount" request
    And body with value {"data": {"attributes": {"api_key": "TESTAPIKEY123", "api_secret": "test-api-secret-123", "resources": [{"id": "resource-id-123", "resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}], "tags": ["myTag", "myTag2:myValue"]}, "type": "confluent-cloud-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Confluent account returns "Not Found" response
    Given new "CreateConfluentAccount" request
    And body with value {"data": {"attributes": {"api_key": "TESTAPIKEY123", "api_secret": "test-api-secret-123", "resources": [{"id": "resource-id-123", "resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}], "tags": ["myTag", "myTag2:myValue"]}, "type": "confluent-cloud-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add Confluent account returns "OK" response
    Given new "CreateConfluentAccount" request
    And body with value {"data": {"attributes": {"api_key": "TESTAPIKEY123", "api_secret": "test-api-secret-123", "resources": [{"id": "resource-id-123", "resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}], "tags": ["myTag", "myTag2:myValue"]}, "type": "confluent-cloud-accounts"}}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add resource to Confluent account returns "Bad Request" response
    Given new "CreateConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}, "id": "resource-id-123", "type": "confluent-cloud-resources"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Add resource to Confluent account returns "Not Found" response
    Given new "CreateConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}, "id": "resource-id-123", "type": "confluent-cloud-resources"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: Add resource to Confluent account returns "OK" response
    Given there is a valid "confluent_account" in the system
    And new "CreateConfluentResource" request
    And request contains "account_id" parameter from "confluent_account.data.id"
    And body with value {"data": {"attributes": {"resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}, "id": "{{ unique_lower_alnum }}", "type": "confluent-cloud-resources"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.id" is equal to "{{ unique_lower_alnum }}"
    And the response "data.attributes.resource_type" is equal to "kafka"
    And the response "data.attributes.tags[0]" is equal to "myTag"

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Confluent account returns "Bad Request" response
    Given new "DeleteConfluentAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Confluent account returns "Not Found" response
    Given new "DeleteConfluentAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete Confluent account returns "OK" response
    Given new "DeleteConfluentAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete resource from Confluent account returns "Bad Request" response
    Given new "DeleteConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete resource from Confluent account returns "Not Found" response
    Given new "DeleteConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: Delete resource from Confluent account returns "OK" response
    Given there is a valid "confluent_account" in the system
    And new "DeleteConfluentAccount" request
    And request contains "account_id" parameter from "confluent_account.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Confluent account returns "Bad Request" response
    Given new "GetConfluentAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get Confluent account returns "Not Found" response
    Given new "GetConfluentAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: Get Confluent account returns "OK" response
    Given there is a valid "confluent_account" in the system
    And new "GetConfluentAccount" request
    And request contains "account_id" parameter from "confluent_account.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get resource from Confluent account returns "Bad Request" response
    Given new "GetConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get resource from Confluent account returns "Not Found" response
    Given new "GetConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get resource from Confluent account returns "OK" response
    Given new "GetConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Confluent Account resources returns "Bad Request" response
    Given new "ListConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Confluent Account resources returns "Not Found" response
    Given new "ListConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Confluent Account resources returns "OK" response
    Given new "ListConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Confluent accounts returns "Bad Request" response
    Given new "ListConfluentAccount" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: List Confluent accounts returns "Not Found" response
    Given new "ListConfluentAccount" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: List Confluent accounts returns "OK" response
    Given there is a valid "confluent_account" in the system
    And new "ListConfluentAccount" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Confluent account returns "Bad Request" response
    Given new "UpdateConfluentAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "TESTAPIKEY123", "api_secret": "test-api-secret-123", "tags": ["myTag", "myTag2:myValue"]}, "type": "confluent-cloud-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update Confluent account returns "Not Found" response
    Given new "UpdateConfluentAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "TESTAPIKEY123", "api_secret": "test-api-secret-123", "tags": ["myTag", "myTag2:myValue"]}, "type": "confluent-cloud-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/web-integrations
  Scenario: Update Confluent account returns "OK" response
    Given there is a valid "confluent_account" in the system
    And new "UpdateConfluentAccount" request
    And request contains "account_id" parameter from "confluent_account.data.id"
    And body with value {"data": {"attributes": {"api_key": "{{confluent_account.data.attributes.api_key}}", "api_secret": "update-secret", "tags": ["updated_tag:val"]}, "type": "confluent-cloud-accounts"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.tags[0]" is equal to "updated_tag:val"
    And the response "data.attributes.api_key" is equal to "{{ confluent_account.data.attributes.api_key }}"

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update resource in Confluent account returns "Bad Request" response
    Given new "UpdateConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}, "id": "resource-id-123", "type": "confluent-cloud-resources"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update resource in Confluent account returns "Not Found" response
    Given new "UpdateConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}, "id": "resource-id-123", "type": "confluent-cloud-resources"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update resource in Confluent account returns "OK" response
    Given new "UpdateConfluentResource" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_type": "kafka", "tags": ["myTag", "myTag2:myValue"]}, "id": "resource-id-123", "type": "confluent-cloud-resources"}}
    When the request is sent
    Then the response status is 200 OK
