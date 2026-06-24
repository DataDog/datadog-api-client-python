@endpoint(governance-controls) @endpoint(governance-controls-v2)
Feature: Governance Controls
  Governance Controls pair a detection definition with an organization's
  detection, notification, and mitigation configuration within the
  Governance Console. Each control reports how a class of governance issue
  (such as unused API keys or unqueried metrics) is detected and remediated,
  along with counts of active and mitigated detections.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GovernanceControls" API

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a governance control returns "Bad Request" response
    Given operation "GetGovernanceControl" enabled
    And new "GetGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a governance control returns "Not Found" response
    Given operation "GetGovernanceControl" enabled
    And new "GetGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a governance control returns "OK" response
    Given operation "GetGovernanceControl" enabled
    And new "GetGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance controls returns "Bad Request" response
    Given operation "ListGovernanceControls" enabled
    And new "ListGovernanceControls" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance controls returns "OK" response
    Given operation "ListGovernanceControls" enabled
    And new "ListGovernanceControls" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a governance control returns "Bad Request" response
    Given operation "UpdateGovernanceControl" enabled
    And new "UpdateGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"detection_frequency": "daily", "mitigation_type": "revoke_api_key", "name": "Unused API Keys", "notification_frequency": "daily", "notification_type": "slack"}, "id": "0d4e6f8a-1b2c-3d4e-5f6a-7b8c9d0e1f2a", "type": "governance_control"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a governance control returns "Not Found" response
    Given operation "UpdateGovernanceControl" enabled
    And new "UpdateGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"detection_frequency": "daily", "mitigation_type": "revoke_api_key", "name": "Unused API Keys", "notification_frequency": "daily", "notification_type": "slack"}, "id": "0d4e6f8a-1b2c-3d4e-5f6a-7b8c9d0e1f2a", "type": "governance_control"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a governance control returns "OK" response
    Given operation "UpdateGovernanceControl" enabled
    And new "UpdateGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"detection_frequency": "daily", "mitigation_type": "revoke_api_key", "name": "Unused API Keys", "notification_frequency": "daily", "notification_type": "slack"}, "id": "0d4e6f8a-1b2c-3d4e-5f6a-7b8c9d0e1f2a", "type": "governance_control"}}
    When the request is sent
    Then the response status is 200 OK
