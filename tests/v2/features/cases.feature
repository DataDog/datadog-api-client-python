@endpoint(cases) @endpoint(cases-v2)
Feature: Cases
  View and manage cases within Datadog

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Cases" API

  @team:DataDog/case-management
  Scenario: Archive case returns "Bad Request" response
    Given new "ArchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Archive case returns "Not Found" response
    Given new "ArchiveCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Archive case returns "OK" response
    Given new "ArchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Assign case returns "Bad Request" response
    Given new "AssignCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"assignee_id": "invalid-uuid"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Assign case returns "Not Found" response
    Given new "AssignCase" request
    And there is a valid "user" in the system
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"assignee_id": "{{user.data.id}}"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Assign case returns "OK" response
    Given new "AssignCase" request
    And there is a valid "case" in the system
    And there is a valid "user" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"assignee_id": "{{user.data.id}}"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Create a case returns "Bad Request" response
    Given new "CreateCase" request
    And body with value {"data": {"attributes": {"priority": "NOT_DEFINED", "title": "Security breach investigation", "type": "STANDARD"}, "relationships": {"assignee": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "userx"}}, "project": {"data": {"id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "type": "project"}}}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Create a case returns "CREATED" response
    Given new "CreateCase" request
    And there is a valid "user" in the system
    And body with value {"data": {"attributes": {"priority": "NOT_DEFINED", "title": "Security breach investigation in {{ unique_hash }}", "type": "STANDARD"}, "relationships": {"assignee": {"data": {"id": "{{user.data.id}}", "type": "user"} }, "project": {"data": {"id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e", "type": "project"}}}, "type": "case"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data" has field "id"
    And the response "data.attributes.title" is equal to "Security breach investigation in {{ unique_hash }}"
    And the response "data.attributes.type" is equal to "STANDARD"
    And the response "data.attributes.priority" is equal to "NOT_DEFINED"

  @generated @skip @team:DataDog/case-management
  Scenario: Create a case returns "Not Found" response
    Given new "CreateCase" request
    And body with value {"data": {"attributes": {"priority": "NOT_DEFINED", "title": "Security breach investigation", "type": "STANDARD"}, "relationships": {"assignee": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "user"}}, "project": {"data": {"id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "type": "project"}}}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/case-management
  Scenario: Get the details of a case returns "Bad Request" response
    Given new "GetCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Get the details of a case returns "Not Found" response
    Given new "GetCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Get the details of a case returns "OK" response
    Given new "GetCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Search cases returns "Bad Request" response
    Given new "SearchCases" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Search cases returns "Not Found" response
    Given new "SearchCases" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Search cases returns "OK" response
    Given new "SearchCases" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management @with-pagination
  Scenario: Search cases returns "OK" response with pagination
    Given new "SearchCases" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Unarchive case returns "Bad Request" response
    Given new "UnarchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Unarchive case returns "Not Found" response
    Given new "UnarchiveCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Unarchive case returns "OK" response
    Given new "UnarchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Unassign case returns "Bad Request" response
    Given new "UnassignCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Unassign case returns "Not Found" response
    Given new "UnassignCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Unassign case returns "OK" response
    Given new "UnassignCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Update case priority returns "Bad Request" response
    Given new "UpdatePriority" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"priority": "P1234"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case priority returns "Not Found" response
    Given new "UpdatePriority" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"priority": "P3"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update case priority returns "OK" response
    Given new "UpdatePriority" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"priority": "P3"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.priority" is equal to "P3"

  @team:DataDog/case-management
  Scenario: Update case status returns "Bad Request" response
    Given new "UpdateStatus" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"status": "OPENED"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case status returns "Not Found" response
    Given new "UpdateStatus" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"status": "OPEN"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update case status returns "OK" response
    Given new "UpdateStatus" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"status": "IN_PROGRESS"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.status" is equal to "IN_PROGRESS"
