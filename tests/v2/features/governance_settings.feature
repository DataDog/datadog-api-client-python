@endpoint(governance-settings) @endpoint(governance-settings-v2)
Feature: Governance Settings
  Governance Settings cover organization-wide Governance Console
  configuration, usage limits and resource limits, and notification
  preferences that determine when and how the Console alerts users about
  governance activity.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GovernanceSettings" API

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get governance notification settings returns "Bad Request" response
    Given operation "GetGovernanceNotificationSettings" enabled
    And new "GetGovernanceNotificationSettings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get governance notification settings returns "OK" response
    Given operation "GetGovernanceNotificationSettings" enabled
    And new "GetGovernanceNotificationSettings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get the governance console configuration returns "Bad Request" response
    Given operation "GetGovernanceConfig" enabled
    And new "GetGovernanceConfig" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get the governance console configuration returns "OK" response
    Given operation "GetGovernanceConfig" enabled
    And new "GetGovernanceConfig" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance limits returns "Bad Request" response
    Given operation "ListGovernanceLimits" enabled
    And new "ListGovernanceLimits" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance limits returns "OK" response
    Given operation "ListGovernanceLimits" enabled
    And new "ListGovernanceLimits" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance resource limits returns "Bad Request" response
    Given operation "ListGovernanceResourceLimits" enabled
    And new "ListGovernanceResourceLimits" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List governance resource limits returns "OK" response
    Given operation "ListGovernanceResourceLimits" enabled
    And new "ListGovernanceResourceLimits" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update governance notification settings returns "Bad Request" response
    Given operation "UpdateGovernanceNotificationSettings" enabled
    And new "UpdateGovernanceNotificationSettings" request
    And body with value {"data": {"attributes": {"assignment_notifications_enabled": true}, "type": "governance_notification_settings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update governance notification settings returns "OK" response
    Given operation "UpdateGovernanceNotificationSettings" enabled
    And new "UpdateGovernanceNotificationSettings" request
    And body with value {"data": {"attributes": {"assignment_notifications_enabled": true}, "type": "governance_notification_settings"}}
    When the request is sent
    Then the response status is 200 OK
