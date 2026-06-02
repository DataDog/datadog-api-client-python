@endpoint(opsgenie-integration) @endpoint(opsgenie-integration-v2)
Feature: Opsgenie Integration
  Configure your [Datadog Opsgenie
  integration](https://docs.datadoghq.com/integrations/opsgenie/) directly
  through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OpsgenieIntegration" API

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a new Opsgenie account returns "Bad Request" response
    Given new "CreateOpsgenieAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "type": "opsgenie-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a new Opsgenie account returns "CREATED" response
    Given new "CreateOpsgenieAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "type": "opsgenie-account"}}
    When the request is sent
    Then the response status is 201 CREATED

  @skip @team:Datadog/collaboration-integrations
  Scenario: Create a new service object returns "Bad Request" response
    Given new "CreateOpsgenieService" request
    And body with value {"data": {"attributes": {"name": "fake-opsgenie-service-name", "opsgenie_api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "type": "opsgenie-service"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/collaboration-integrations
  Scenario: Create a new service object returns "CREATED" response
    Given new "CreateOpsgenieService" request
    And body with value {"data": {"attributes": {"name": "{{unique}}", "opsgenie_api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "type": "opsgenie-service" }}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{unique}}"
    And the response "data.attributes.region" is equal to "us"

  @skip @team:Datadog/collaboration-integrations
  Scenario: Create a new service object returns "Conflict" response
    Given new "CreateOpsgenieService" request
    And body with value {"data": {"attributes": {"name": "fake-opsgenie-service-name", "opsgenie_api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "type": "opsgenie-service"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a single service object returns "Bad Request" response
    Given new "DeleteOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a single service object returns "Not Found" response
    Given new "DeleteOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/collaboration-integrations
  Scenario: Delete a single service object returns "OK" response
    Given there is a valid "opsgenie_service" in the system
    And new "DeleteOpsgenieService" request
    And request contains "integration_service_id" parameter from "opsgenie_service.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete an Opsgenie account returns "Bad Request" response
    Given new "DeleteOpsgenieAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete an Opsgenie account returns "Not Found" response
    Given new "DeleteOpsgenieAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete an Opsgenie account returns "OK" response
    Given new "DeleteOpsgenieAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a single service object returns "Bad Request" response
    Given new "GetOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a single service object returns "Conflict" response
    Given new "GetOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a single service object returns "Not Found" response
    Given new "GetOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/collaboration-integrations
  Scenario: Get a single service object returns "OK" response
    Given there is a valid "opsgenie_service" in the system
    And new "GetOpsgenieService" request
    And request contains "integration_service_id" parameter from "opsgenie_service.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "opsgenie_service.data.attributes.name"
    And the response "data.attributes.region" is equal to "us"

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all Opsgenie accounts returns "OK" response
    Given new "ListOpsgenieAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @team:Datadog/collaboration-integrations
  Scenario: Get all service objects returns "OK" response
    Given there is a valid "opsgenie_service" in the system
    And new "ListOpsgenieServices" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "opsgenie-service"

  @skip @team:Datadog/collaboration-integrations
  Scenario: Update a single service object returns "Bad Request" response
    Given new "UpdateOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-opsgenie-service-name", "opsgenie_api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "opsgenie-service"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:Datadog/collaboration-integrations
  Scenario: Update a single service object returns "Conflict" response
    Given new "UpdateOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-opsgenie-service-name", "opsgenie_api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "opsgenie-service"}}
    When the request is sent
    Then the response status is 409 Conflict

  @skip @team:Datadog/collaboration-integrations
  Scenario: Update a single service object returns "Not Found" response
    Given new "UpdateOpsgenieService" request
    And request contains "integration_service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-opsgenie-service-name", "opsgenie_api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "opsgenie-service"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/collaboration-integrations
  Scenario: Update a single service object returns "OK" response
    Given there is a valid "opsgenie_service" in the system
    And new "UpdateOpsgenieService" request
    And request contains "integration_service_id" parameter from "opsgenie_service.data.id"
    And body with value {"data": {"attributes": {"name": "{{ opsgenie_service.data.attributes.name }}--updated", "opsgenie_api_key": "00000000-0000-0000-0000-000000000000", "region": "eu"}, "id": "{{opsgenie_service.data.id}}", "type": "opsgenie-service"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ opsgenie_service.data.attributes.name }}--updated"
    And the response "data.attributes.region" is equal to "eu"

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an Opsgenie account returns "Bad Request" response
    Given new "UpdateOpsgenieAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "opsgenie-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an Opsgenie account returns "Not Found" response
    Given new "UpdateOpsgenieAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "opsgenie-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an Opsgenie account returns "OK" response
    Given new "UpdateOpsgenieAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "opsgenie-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update an Opsgenie account returns "The server cannot process the request because it contains invalid data." response
    Given new "UpdateOpsgenieAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000", "region": "us"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "opsgenie-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
