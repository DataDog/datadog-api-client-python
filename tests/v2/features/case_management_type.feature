@endpoint(case-management-type) @endpoint(case-management-type-v2)
Feature: Case Management Type
  View and configure case types within Case Management. See the [Case
  Management
  page](https://docs.datadoghq.com/service_management/case_management/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CaseManagementType" API

  @team:DataDog/case-management
  Scenario: Create a case type returns "Bad Request" response
    Given new "CreateCaseType" request
    And body with value {"data": {"attributes": {"description": "Investigations done in case management", "emoji": "notanemoji", "name": "Investigation"}, "type": "case_type"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Create a case type returns "CREATED" response
    Given new "CreateCaseType" request
    And body with value {"data": {"attributes": {"description": "Investigations done in case management", "emoji": "👑", "name": "Investigation"}, "type": "case_type"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a case type returns "No Content" response
    Given new "DeleteCaseType" request
    And request contains "case_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/case-management
  Scenario: Delete a case type returns "NotContent" response
    Given new "DeleteCaseType" request
    And there is a valid "case_type" in the system
    And request contains "case_type_id" parameter from "case_type.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/case-management
  Scenario: Get all case types returns "OK" response
    Given new "GetAllCaseTypes" request
    When the request is sent
    Then the response status is 200 OK
