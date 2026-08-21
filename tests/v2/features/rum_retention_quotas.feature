@endpoint(rum-retention-quotas) @endpoint(rum-retention-quotas-v2)
Feature: RUM Retention Quotas
  Manage RUM retention quota configurations for your organization's RUM
  applications.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMRetentionQuotas" API

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM retention quota config returns "Bad Request" response
    Given new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "cd73a516-a481-4af5-8352-9b577465c77b", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM retention quota config returns "Not Found" response
    Given new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "cd73a516-a481-4af5-8352-9b577465c77b", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM retention quota config returns "OK" response
    Given new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "cd73a516-a481-4af5-8352-9b577465c77b", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "Bad Request" response
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "No Content" response
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "Not Found" response
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM retention quota configuration returns "Bad Request" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM retention quota configuration returns "Not Found" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM retention quota configuration returns "OK" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
