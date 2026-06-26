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
  Scenario: Get a governance control detection returns "Bad Request" response
    Given operation "GetGovernanceControlDetection" enabled
    And new "GetGovernanceControlDetection" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And request contains "detection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a governance control detection returns "Not Found" response
    Given operation "GetGovernanceControlDetection" enabled
    And new "GetGovernanceControlDetection" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And request contains "detection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a governance control detection returns "OK" response
    Given operation "GetGovernanceControlDetection" enabled
    And new "GetGovernanceControlDetection" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And request contains "detection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

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
  Scenario: Get governance control notification settings returns "Bad Request" response
    Given operation "GetGovernanceControlNotificationSettings" enabled
    And new "GetGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get governance control notification settings returns "OK" response
    Given operation "GetGovernanceControlNotificationSettings" enabled
    And new "GetGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance control detections returns "Bad Request" response
    Given operation "ListGovernanceControlDetections" enabled
    And new "ListGovernanceControlDetections" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance control detections returns "OK" response
    Given operation "ListGovernanceControlDetections" enabled
    And new "ListGovernanceControlDetections" request
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
  Scenario: Mitigate governance detections returns "Accepted" response
    Given operation "CreateGovernanceMitigation" enabled
    And new "CreateGovernanceMitigation" request
    And body with value {"data": {"attributes": {"detection_ids": ["3f9b2c1a-8d4e-4a6b-9c2f-1e7d5a0b3c4d"], "detection_type": "unused_api_keys", "mitigation_type": "revoke_api_key"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Mitigate governance detections returns "Bad Request" response
    Given operation "CreateGovernanceMitigation" enabled
    And new "CreateGovernanceMitigation" request
    And body with value {"data": {"attributes": {"detection_ids": ["3f9b2c1a-8d4e-4a6b-9c2f-1e7d5a0b3c4d"], "detection_type": "unused_api_keys", "mitigation_type": "revoke_api_key"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a governance control detection returns "Bad Request" response
    Given operation "UpdateGovernanceControlDetection" enabled
    And new "UpdateGovernanceControlDetection" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And request contains "detection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assigned_team": "platform-security", "assigned_to": "11111111-2222-3333-4444-555555555555", "mitigate_after": "2024-03-15T00:00:00Z", "state": "exception"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a governance control detection returns "Not Found" response
    Given operation "UpdateGovernanceControlDetection" enabled
    And new "UpdateGovernanceControlDetection" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And request contains "detection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assigned_team": "platform-security", "assigned_to": "11111111-2222-3333-4444-555555555555", "mitigate_after": "2024-03-15T00:00:00Z", "state": "exception"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a governance control detection returns "OK" response
    Given operation "UpdateGovernanceControlDetection" enabled
    And new "UpdateGovernanceControlDetection" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And request contains "detection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assigned_team": "platform-security", "assigned_to": "11111111-2222-3333-4444-555555555555", "mitigate_after": "2024-03-15T00:00:00Z", "state": "exception"}, "type": "governance_control_detection"}}
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

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update governance control notification settings returns "Bad Request" response
    Given operation "UpdateGovernanceControlNotificationSettings" enabled
    And new "UpdateGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"event_settings": [{"enabled": true, "event_type": "new_detection", "targets": [{"handle": "#governance-alerts", "type": "slack"}]}]}, "type": "control_notification_settings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update governance control notification settings returns "OK" response
    Given operation "UpdateGovernanceControlNotificationSettings" enabled
    And new "UpdateGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"event_settings": [{"enabled": true, "event_type": "new_detection", "targets": [{"handle": "#governance-alerts", "type": "slack"}]}]}, "type": "control_notification_settings"}}
    When the request is sent
    Then the response status is 200 OK
