@endpoint(governance-console) @endpoint(governance-console-v2)
Feature: Governance Console
  The Governance Console finds issues that build up across a Datadog
  organization over time, such as API keys nobody uses, users who no longer
  need access, or custom metrics that are never queried, and tracks them
  through to a fix.  These endpoints allow you to:  - Read insights:
  measures of how your organization uses Datadog, each with the query behind
  it. - Configure controls: the rules deciding how one kind of issue is
  found and what is done about it. - Act on detections: the issues a control
  found. Assign, defer, accept as an exception, or fix. - Manage settings:
  organization-wide configuration and notification destinations.  See the
  [Governance Console
  page](https://docs.datadoghq.com/account_management/governance_console/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GovernanceConsole" API

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a control returns "Bad Request" response
    Given operation "GetGovernanceControl" enabled
    And new "GetGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a control returns "Not Found" response
    Given operation "GetGovernanceControl" enabled
    And new "GetGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a control returns "OK" response
    Given operation "GetGovernanceControl" enabled
    And new "GetGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a detection returns "Bad Request" response
    Given operation "GetGovernanceDetection" enabled
    And new "GetGovernanceDetection" request
    And request contains "detection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a detection returns "Not Found" response
    Given operation "GetGovernanceDetection" enabled
    And new "GetGovernanceDetection" request
    And request contains "detection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a detection returns "OK" response
    Given operation "GetGovernanceDetection" enabled
    And new "GetGovernanceDetection" request
    And request contains "detection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get control notification settings returns "Bad Request" response
    Given operation "GetGovernanceControlNotificationSettings" enabled
    And new "GetGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get control notification settings returns "OK" response
    Given operation "GetGovernanceControlNotificationSettings" enabled
    And new "GetGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get notification settings returns "Bad Request" response
    Given operation "GetGovernanceNotificationSettings" enabled
    And new "GetGovernanceNotificationSettings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get notification settings returns "OK" response
    Given operation "GetGovernanceNotificationSettings" enabled
    And new "GetGovernanceNotificationSettings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get the Governance Console configuration returns "Bad Request" response
    Given operation "GetGovernanceConfig" enabled
    And new "GetGovernanceConfig" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get the Governance Console configuration returns "OK" response
    Given operation "GetGovernanceConfig" enabled
    And new "GetGovernanceConfig" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List control detections returns "Bad Request" response
    Given operation "ListGovernanceControlDetections" enabled
    And new "ListGovernanceControlDetections" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List control detections returns "OK" response
    Given operation "ListGovernanceControlDetections" enabled
    And new "ListGovernanceControlDetections" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List controls returns "Bad Request" response
    Given operation "ListGovernanceControls" enabled
    And new "ListGovernanceControls" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List controls returns "OK" response
    Given operation "ListGovernanceControls" enabled
    And new "ListGovernanceControls" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List insights returns "Bad Request" response
    Given operation "ListGovernanceInsights" enabled
    And new "ListGovernanceInsights" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List insights returns "OK" response
    Given operation "ListGovernanceInsights" enabled
    And new "ListGovernanceInsights" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Mitigate detections returns "Accepted" response
    Given operation "MitigateGovernanceDetections" enabled
    And new "MitigateGovernanceDetections" request
    And body with value {"data": {"attributes": {"detection_ids": ["3f9b2c1a-8d4e-4a6b-9c2f-1e7d5a0b3c4d"], "detection_type": "unused_api_keys", "mitigation_type": "revoke_api_key"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Mitigate detections returns "Bad Request" response
    Given operation "MitigateGovernanceDetections" enabled
    And new "MitigateGovernanceDetections" request
    And body with value {"data": {"attributes": {"detection_ids": ["3f9b2c1a-8d4e-4a6b-9c2f-1e7d5a0b3c4d"], "detection_type": "unused_api_keys", "mitigation_type": "revoke_api_key"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a control returns "Bad Request" response
    Given operation "UpdateGovernanceControl" enabled
    And new "UpdateGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"detection_frequency": "daily", "mitigation_type": "revoke_api_key"}, "type": "governance_control"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a control returns "Not Found" response
    Given operation "UpdateGovernanceControl" enabled
    And new "UpdateGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"detection_frequency": "daily", "mitigation_type": "revoke_api_key"}, "type": "governance_control"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a control returns "OK" response
    Given operation "UpdateGovernanceControl" enabled
    And new "UpdateGovernanceControl" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"detection_frequency": "daily", "mitigation_type": "revoke_api_key"}, "type": "governance_control"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a detection returns "Bad Request" response
    Given operation "UpdateGovernanceDetection" enabled
    And new "UpdateGovernanceDetection" request
    And request contains "detection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assigned_team": "platform-security", "assigned_to": "11111111-2222-3333-4444-555555555555", "mitigate_after": "2024-03-15T00:00:00Z", "state": "exception"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a detection returns "Not Found" response
    Given operation "UpdateGovernanceDetection" enabled
    And new "UpdateGovernanceDetection" request
    And request contains "detection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assigned_team": "platform-security", "assigned_to": "11111111-2222-3333-4444-555555555555", "mitigate_after": "2024-03-15T00:00:00Z", "state": "exception"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a detection returns "OK" response
    Given operation "UpdateGovernanceDetection" enabled
    And new "UpdateGovernanceDetection" request
    And request contains "detection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assigned_team": "platform-security", "assigned_to": "11111111-2222-3333-4444-555555555555", "mitigate_after": "2024-03-15T00:00:00Z", "state": "exception"}, "type": "governance_control_detection"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update control notification settings returns "Bad Request" response
    Given operation "UpdateGovernanceControlNotificationSettings" enabled
    And new "UpdateGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"event_settings": [{"enabled": true, "event_type": "new_detection", "targets": [{"handle": "#governance-alerts", "type": "slack"}]}]}, "type": "control_notification_settings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update control notification settings returns "OK" response
    Given operation "UpdateGovernanceControlNotificationSettings" enabled
    And new "UpdateGovernanceControlNotificationSettings" request
    And request contains "detection_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"event_settings": [{"enabled": true, "event_type": "new_detection", "targets": [{"handle": "#governance-alerts", "type": "slack"}]}]}, "type": "control_notification_settings"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update notification settings returns "Bad Request" response
    Given operation "UpdateGovernanceNotificationSettings" enabled
    And new "UpdateGovernanceNotificationSettings" request
    And body with value {"data": {"attributes": {"assignment_notifications_enabled": true}, "type": "governance_notification_settings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update notification settings returns "OK" response
    Given operation "UpdateGovernanceNotificationSettings" enabled
    And new "UpdateGovernanceNotificationSettings" request
    And body with value {"data": {"attributes": {"assignment_notifications_enabled": true}, "type": "governance_notification_settings"}}
    When the request is sent
    Then the response status is 200 OK
