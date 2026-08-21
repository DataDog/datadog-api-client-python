@endpoint(rum-retention-quota) @endpoint(rum-retention-quota-v2)
Feature: RUM Retention Quota
  Manage RUM retention quota configurations for your organization's RUM
  applications.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMRetentionQuota" API

  @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM retention quota config returns "Bad Request" response
    Given new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "invalid-scope-id"
    And body with value {"data": {"attributes": {"adaptive": {"max_retention_rate": 0.5}, "custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "cd73a516-a481-4af5-8352-9b577465c77b", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM retention quota config returns "Not Found" response
    Given new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "{{ unique }}"
    And body with value {"data": {"attributes": {"adaptive": {"max_retention_rate": 0.5}, "custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "{{ unique }}", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM retention quota config returns "OK" response
    Given new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "ced16651-97b6-4e67-8590-8caec3af0695"
    And body with value {"data": {"attributes": {"adaptive": {"max_retention_rate": 0.5}, "custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "ced16651-97b6-4e67-8590-8caec3af0695", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "Bad Request" response
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "No Content" response
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "ced16651-97b6-4e67-8590-8caec3af0695"
    When the request is sent
    Then the response status is 204 No Content

  @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "Not Found" response
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "Not Found" response for an invalid scope_id
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "invalid-scope-id"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM retention quota configuration returns "Bad Request" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/rum-backend
  Scenario: Get a RUM retention quota configuration returns "Not Found" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "1d4b9c34-7ac4-423a-91cf-9902d926e9b3"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/rum-backend
  Scenario: Get a RUM retention quota configuration returns "Not Found" response for an invalid scope_id
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "invalid-scope-id"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/rum-backend
  Scenario: Get a RUM retention quota configuration returns "OK" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "ced16651-97b6-4e67-8590-8caec3af0695"
    When the request is sent
    Then the response status is 200 OK
