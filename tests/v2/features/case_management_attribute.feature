@endpoint(case-management-attribute) @endpoint(case-management-attribute-v2)
Feature: Case Management Attribute
  View and configure custom attributes within Case Management. See the [Case
  Management
  page](https://docs.datadoghq.com/service_management/case_management/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CaseManagementAttribute" API

  @team:DataDog/case-management
  Scenario: Create custom attribute config for a case type returns "Bad Request" response
    Given new "CreateCustomAttributeConfig" request
    And there is a valid "case_type" in the system
    And request contains "case_type_id" parameter from "case_type.id"
    And body with value {"data": {"attributes": {"display_name": "AWS Region {{uuid}}", "is_multi": true, "key": "region_{{unique_hash}}", "type": "FLOAT"}, "type": "custom_attribute"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Create custom attribute config for a case type returns "CREATED" response
    Given new "CreateCustomAttributeConfig" request
    And there is a valid "case_type" in the system
    And request contains "case_type_id" parameter from "case_type.id"
    And body with value {"data": {"attributes": {"display_name": "AWS Region {{uuid}}", "is_multi": true, "key": "region_{{unique_hash}}", "type": "NUMBER"}, "type": "custom_attribute"}}
    When the request is sent
    Then the response status is 201 CREATED

  @team:DataDog/case-management
  Scenario: Create custom attribute config for a case type returns "Not Found" response
    Given new "CreateCustomAttributeConfig" request
    And request contains "case_type_id" parameter with value "9fd476d7-a955-454a-851d-980c655c02d3"
    And body with value {"data": {"attributes": {"display_name": "AWS Region {{unique_hash}}", "is_multi": true, "key": "region_{{unique_hash}}", "type": "NUMBER"}, "type": "custom_attribute"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Delete custom attributes config returns "Bad Request" response
    Given new "DeleteCustomAttributeConfig" request
    And there is a valid "case_type" in the system
    And request contains "case_type_id" parameter from "case_type.id"
    And request contains "custom_attribute_id" parameter with value "not-an-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/case-management
  Scenario: Delete custom attributes config returns "No Content" response
    Given new "DeleteCustomAttributeConfig" request
    And there is a valid "case_type" in the system
    And there is a valid "custom_attribute" in the system
    And request contains "case_type_id" parameter from "case_type.id"
    And request contains "custom_attribute_id" parameter from "custom_attribute.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip @team:DataDog/case-management
  Scenario: Get all custom attributes config of case type returns "Bad Request" response
    Given new "GetAllCustomAttributeConfigsByCaseType" request
    And request contains "case_type_id" parameter with value "not-an-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Get all custom attributes config of case type returns "OK" response
    Given new "GetAllCustomAttributeConfigsByCaseType" request
    And there is a valid "case_type" in the system
    And request contains "case_type_id" parameter from "case_type.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Get all custom attributes returns "OK" response
    Given new "GetAllCustomAttributes" request
    When the request is sent
    Then the response status is 200 OK
