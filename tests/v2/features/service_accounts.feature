@endpoint(service-accounts) @endpoint(service-accounts-v2)
Feature: Service Accounts
  Create, edit, and disable service accounts.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceAccounts" API

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Create a service account returns "Bad Request" response
    Given new "CreateServiceAccount" request
    And body with value {"data": {"attributes": {"email": "jane.doe@example.com", "service_account": true}, "relationships": {"roles": {"data": [{"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}]}}, "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Create a service account returns "OK" response
    Given there is a valid "role" in the system
    And new "CreateServiceAccount" request
    And body with value {"data": {"type": "users", "attributes": {"name": "Test API Client", "email": "{{ unique }}@datadoghq.com", "service_account": true}, "relationships": {"roles": {"data": [{"id": "{{ role.data.id }}", "type": "roles"}]}}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.email" is equal to "{{ unique_lower }}@datadoghq.com"
    And the response "data.attributes.name" is equal to "Test API Client"
    And the response "data.attributes.disabled" is false
    And the response "data.attributes.service_account" is equal to true
    And the response "data.relationships.roles.data[0].id" is equal to "{{ role.data.id }}"

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Create an application key for this service account returns "Bad Request" response
    Given new "CreateServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "type": "application_keys"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Create an application key for this service account returns "Created" response
    Given there is a valid "service_account_user" in the system
    And new "CreateServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "service_account_user.data.id"
    And body with value {"data": {"attributes": {"name": "{{ unique }}"}, "type": "application_keys"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.relationships.owned_by.data.id" has the same value as "service_account_user.data.id"

  @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Create an application key with scopes for this service account returns "Created" response
    Given there is a valid "service_account_user" in the system
    And new "CreateServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "service_account_user.data.id"
    And body with value {"data": {"attributes": {"name": "{{ unique }}", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "type": "application_keys"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.scopes" is equal to ["dashboards_read", "dashboards_write", "dashboards_public_share"]
    And the response "data.relationships.owned_by.data.id" has the same value as "service_account_user.data.id"

  @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Delete an application key for this service account returns "No Content" response
    Given there is a valid "service_account_user" in the system
    And there is a valid "service_account_application_key" for "service_account_user"
    And new "DeleteServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "service_account_user.data.id"
    And request contains "app_key_id" parameter from "service_account_application_key.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Delete an application key for this service account returns "Not Found" response
    Given new "DeleteServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "REPLACE.ME"
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Edit an application key for this service account returns "Bad Request" response
    Given new "UpdateServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "REPLACE.ME"
    And request contains "app_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "application_keys"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Edit an application key for this service account returns "Not Found" response
    Given new "UpdateServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "REPLACE.ME"
    And request contains "app_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "application_keys"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Edit an application key for this service account returns "OK" response
    Given there is a valid "service_account_user" in the system
    And there is a valid "service_account_application_key" for "service_account_user"
    And new "UpdateServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "service_account_user.data.id"
    And request contains "app_key_id" parameter from "service_account_application_key.data.id"
    And body with value {"data": {"id": "{{ service_account_application_key.data.id }}", "type": "application_keys", "attributes": {"name" : "{{ service_account_application_key.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ service_account_application_key.data.attributes.name }}-updated"
    And the response "data.type" is equal to "application_keys"
    And the response "data.id" is equal to "{{ service_account_application_key.data.id }}"

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Get one application key for this service account returns "Not Found" response
    Given new "GetServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "REPLACE.ME"
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: Get one application key for this service account returns "OK" response
    Given there is a valid "service_account_user" in the system
    And there is a valid "service_account_application_key" for "service_account_user"
    And new "GetServiceAccountApplicationKey" request
    And request contains "service_account_id" parameter from "service_account_user.data.id"
    And request contains "app_key_id" parameter from "service_account_application_key.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "service_account_application_key.data.attributes.name"
    And the response "data.type" is equal to "application_keys"
    And the response "data.id" is equal to "{{ service_account_application_key.data.id }}"

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: List application keys for this service account returns "Bad Request" response
    Given new "ListServiceAccountApplicationKeys" request
    And request contains "service_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: List application keys for this service account returns "Not Found" response
    Given new "ListServiceAccountApplicationKeys" request
    And request contains "service_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/credentials-management @team:DataDog/team-aaa-identity
  Scenario: List application keys for this service account returns "OK" response
    Given there is a valid "service_account_user" in the system
    And new "ListServiceAccountApplicationKeys" request
    And request contains "service_account_id" parameter from "service_account_user.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0
