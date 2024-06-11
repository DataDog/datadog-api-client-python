@endpoint(api-management) @endpoint(api-management-v2)
Feature: API Management
  Configure your API endpoints through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "APIManagement" API

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/api-management
  Scenario: Create a new API returns "API created successfully" response
    Given operation "CreateOpenAPI" enabled
    And new "CreateOpenAPI" request
    And request contains "openapi_spec_file" parameter with value "openapi-spec.yaml"
    When the request is sent
    Then the response status is 201 API created successfully
    And the response "data.attributes.failed_endpoints" has length 0

  @generated @skip @team:DataDog/api-management
  Scenario: Create a new API returns "Bad request" response
    Given operation "CreateOpenAPI" enabled
    And new "CreateOpenAPI" request
    When the request is sent
    Then the response status is 400 Bad request

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/api-management
  Scenario: Delete an API returns "API deleted successfully" response
    Given operation "DeleteOpenAPI" enabled
    And there is a valid "managed_api" in the system
    And new "DeleteOpenAPI" request
    And request contains "id" parameter from "managed_api.data.id"
    When the request is sent
    Then the response status is 204 API deleted successfully

  @generated @skip @team:DataDog/api-management
  Scenario: Delete an API returns "API not found error" response
    Given operation "DeleteOpenAPI" enabled
    And new "DeleteOpenAPI" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API not found error

  @generated @skip @team:DataDog/api-management
  Scenario: Delete an API returns "Bad request" response
    Given operation "DeleteOpenAPI" enabled
    And new "DeleteOpenAPI" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/api-management
  Scenario: Get an API returns "API not found error" response
    Given operation "GetOpenAPI" enabled
    And new "GetOpenAPI" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API not found error

  @generated @skip @team:DataDog/api-management
  Scenario: Get an API returns "Bad request" response
    Given operation "GetOpenAPI" enabled
    And new "GetOpenAPI" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/api-management
  Scenario: Get an API returns "OK" response
    Given operation "GetOpenAPI" enabled
    And there is a valid "managed_api" in the system
    And new "GetOpenAPI" request
    And request contains "id" parameter from "managed_api.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/api-management
  Scenario: List APIs returns "Bad request" response
    Given operation "ListAPIs" enabled
    And new "ListAPIs" request
    When the request is sent
    Then the response status is 400 Bad request

  @generated @skip @team:DataDog/api-management
  Scenario: List APIs returns "OK" response
    Given operation "ListAPIs" enabled
    And new "ListAPIs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/api-management
  Scenario: Update an API returns "API not found error" response
    Given operation "UpdateOpenAPI" enabled
    And new "UpdateOpenAPI" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API not found error

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/api-management
  Scenario: Update an API returns "API updated successfully" response
    Given operation "UpdateOpenAPI" enabled
    And there is a valid "managed_api" in the system
    And new "UpdateOpenAPI" request
    And request contains "id" parameter from "managed_api.data.id"
    And request contains "openapi_spec_file" parameter with value "openapi-spec.yaml"
    When the request is sent
    Then the response status is 200 API updated successfully
    And the response "data.attributes.failed_endpoints" has length 0

  @generated @skip @team:DataDog/api-management
  Scenario: Update an API returns "Bad request" response
    Given operation "UpdateOpenAPI" enabled
    And new "UpdateOpenAPI" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request
