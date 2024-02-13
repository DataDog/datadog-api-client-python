@endpoint(cases-projects) @endpoint(cases-projects-v2)
Feature: Cases Projects
  View and manage project within Case Management

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CasesProjects" API

  @generated @skip @team:DataDog/case-management
  Scenario: Create a project returns "Bad Request" response
    Given new "CreateProject" request
    And body with value {"data": {"attributes": {"key": "SEC", "name": "Security Investigation"}, "type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a project returns "CREATED" response
    Given new "CreateProject" request
    And body with value {"data": {"attributes": {"key": "SEC", "name": "Security Investigation"}, "type": "project"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/case-management
  Scenario: Create a project returns "Not Found" response
    Given new "CreateProject" request
    And body with value {"data": {"attributes": {"key": "SEC", "name": "Security Investigation"}, "type": "project"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get all projects returns "Bad Request" response
    Given new "GetProjects" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get all projects returns "Not Found" response
    Given new "GetProjects" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get all projects returns "OK" response
    Given new "GetProjects" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Get the details of a project returns "Bad Request" response
    Given new "GetProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get the details of a project returns "Not Found" response
    Given new "GetProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get the details of a project returns "OK" response
    Given new "GetProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Remove a project returns "API error response" response
    Given new "DeleteProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response

  @generated @skip @team:DataDog/case-management
  Scenario: Remove a project returns "No Content" response
    Given new "DeleteProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content
