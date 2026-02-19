@endpoint(change-management) @endpoint(change-management-v2)
Feature: Change Management
  View and manage change requests within Change Management. See the [Case
  Management
  page](https://docs.datadoghq.com/service_management/case_management/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ChangeManagement" API

  @generated @skip @team:DataDog/case-management
  Scenario: Create a change request branch returns "Bad Request" response
    Given operation "CreateChangeRequestBranch" enabled
    And new "CreateChangeRequestBranch" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"branch_name": "chm/CHM-1234", "repo_id": "DataDog/dd-source"}, "type": "change_request_branch"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a change request branch returns "Not Found" response
    Given operation "CreateChangeRequestBranch" enabled
    And new "CreateChangeRequestBranch" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"branch_name": "chm/CHM-1234", "repo_id": "DataDog/dd-source"}, "type": "change_request_branch"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create a change request branch returns "OK" response
    Given operation "CreateChangeRequestBranch" enabled
    And new "CreateChangeRequestBranch" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"branch_name": "chm/CHM-1234", "repo_id": "DataDog/dd-source"}, "type": "change_request_branch"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Create a change request returns "Bad Request" response
    Given operation "CreateChangeRequest" enabled
    And new "CreateChangeRequest" request
    And body with value {"data": {"attributes": {"change_request_linked_incident_uuid": "00000000-0000-0000-0000-000000000000", "change_request_maintenance_window_query": "", "change_request_plan": "1. Deploy to staging 2. Run tests 3. Deploy to production", "change_request_risk": "LOW", "change_request_type": "NORMAL", "description": "Deploying new payment service v2.1", "end_date": "2024-01-02T15:00:00Z", "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e", "requested_teams": ["team-handle-1"], "start_date": "2024-01-01T03:00:00Z", "title": "Deploy new payment service"}, "type": "change_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a change request returns "Created" response
    Given operation "CreateChangeRequest" enabled
    And new "CreateChangeRequest" request
    And body with value {"data": {"attributes": {"change_request_linked_incident_uuid": "00000000-0000-0000-0000-000000000000", "change_request_maintenance_window_query": "", "change_request_plan": "1. Deploy to staging 2. Run tests 3. Deploy to production", "change_request_risk": "LOW", "change_request_type": "NORMAL", "description": "Deploying new payment service v2.1", "end_date": "2024-01-02T15:00:00Z", "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e", "requested_teams": ["team-handle-1"], "start_date": "2024-01-01T03:00:00Z", "title": "Deploy new payment service"}, "type": "change_request"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a change request decision returns "Bad Request" response
    Given operation "DeleteChangeRequestDecision" enabled
    And new "DeleteChangeRequestDecision" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And request contains "decision_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a change request decision returns "Not Found" response
    Given operation "DeleteChangeRequestDecision" enabled
    And new "DeleteChangeRequestDecision" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And request contains "decision_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a change request decision returns "OK" response
    Given operation "DeleteChangeRequestDecision" enabled
    And new "DeleteChangeRequestDecision" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And request contains "decision_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Get a change request returns "Bad Request" response
    Given operation "GetChangeRequest" enabled
    And new "GetChangeRequest" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get a change request returns "Not Found" response
    Given operation "GetChangeRequest" enabled
    And new "GetChangeRequest" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get a change request returns "OK" response
    Given operation "GetChangeRequest" enabled
    And new "GetChangeRequest" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Update a change request decision returns "Bad Request" response
    Given operation "UpdateChangeRequestDecision" enabled
    And new "UpdateChangeRequestDecision" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And request contains "decision_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"id": "CHM-1234"}, "relationships": {"change_request_decisions": {"data": [{"id": "decision-id-0", "type": "change_request_decision"}]}}, "type": "change_request"}, "included": [{"attributes": {"change_request_status": "REQUESTED", "request_reason": "Please review and approve this change"}, "id": "decision-id-0", "relationships": {"requested_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "user"}}}, "type": "change_request_decision"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update a change request decision returns "Not Found" response
    Given operation "UpdateChangeRequestDecision" enabled
    And new "UpdateChangeRequestDecision" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And request contains "decision_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"id": "CHM-1234"}, "relationships": {"change_request_decisions": {"data": [{"id": "decision-id-0", "type": "change_request_decision"}]}}, "type": "change_request"}, "included": [{"attributes": {"change_request_status": "REQUESTED", "request_reason": "Please review and approve this change"}, "id": "decision-id-0", "relationships": {"requested_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "user"}}}, "type": "change_request_decision"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update a change request decision returns "OK" response
    Given operation "UpdateChangeRequestDecision" enabled
    And new "UpdateChangeRequestDecision" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And request contains "decision_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"id": "CHM-1234"}, "relationships": {"change_request_decisions": {"data": [{"id": "decision-id-0", "type": "change_request_decision"}]}}, "type": "change_request"}, "included": [{"attributes": {"change_request_status": "REQUESTED", "request_reason": "Please review and approve this change"}, "id": "decision-id-0", "relationships": {"requested_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "user"}}}, "type": "change_request_decision"}]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Update a change request returns "Bad Request" response
    Given operation "UpdateChangeRequest" enabled
    And new "UpdateChangeRequest" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"change_request_plan": "Updated deployment plan", "change_request_risk": "LOW", "change_request_type": "NORMAL", "end_date": "2024-01-02T15:00:00Z", "id": "CHM-1234", "start_date": "2024-01-01T03:00:00Z"}, "relationships": {"change_request_decisions": {"data": [{"id": "decision-id-0", "type": "change_request_decision"}]}}, "type": "change_request"}, "included": [{"attributes": {"change_request_status": "REQUESTED", "request_reason": "Please review and approve this change"}, "id": "decision-id-0", "relationships": {"requested_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "user"}}}, "type": "change_request_decision"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update a change request returns "Not Found" response
    Given operation "UpdateChangeRequest" enabled
    And new "UpdateChangeRequest" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"change_request_plan": "Updated deployment plan", "change_request_risk": "LOW", "change_request_type": "NORMAL", "end_date": "2024-01-02T15:00:00Z", "id": "CHM-1234", "start_date": "2024-01-01T03:00:00Z"}, "relationships": {"change_request_decisions": {"data": [{"id": "decision-id-0", "type": "change_request_decision"}]}}, "type": "change_request"}, "included": [{"attributes": {"change_request_status": "REQUESTED", "request_reason": "Please review and approve this change"}, "id": "decision-id-0", "relationships": {"requested_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "user"}}}, "type": "change_request_decision"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update a change request returns "OK" response
    Given operation "UpdateChangeRequest" enabled
    And new "UpdateChangeRequest" request
    And request contains "change_request_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"change_request_plan": "Updated deployment plan", "change_request_risk": "LOW", "change_request_type": "NORMAL", "end_date": "2024-01-02T15:00:00Z", "id": "CHM-1234", "start_date": "2024-01-01T03:00:00Z"}, "relationships": {"change_request_decisions": {"data": [{"id": "decision-id-0", "type": "change_request_decision"}]}}, "type": "change_request"}, "included": [{"attributes": {"change_request_status": "REQUESTED", "request_reason": "Please review and approve this change"}, "id": "decision-id-0", "relationships": {"requested_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "user"}}}, "type": "change_request_decision"}]}
    When the request is sent
    Then the response status is 200 OK
