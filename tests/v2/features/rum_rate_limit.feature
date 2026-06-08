@endpoint(rum-rate-limit) @endpoint(rum-rate-limit-v2)
Feature: Rum Rate Limit
  Manage RUM rate limit configurations for your organization's RUM
  applications.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumRateLimit" API

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM rate limit configuration returns "Bad Request" response
    Given operation "UpdateRumRateLimitConfig" enabled
    And new "UpdateRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"adaptive": {"max_retention_rate": 0.5}, "custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "cd73a516-a481-4af5-8352-9b577465c77b", "type": "rum_rate_limit_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM rate limit configuration returns "Not Found" response
    Given operation "UpdateRumRateLimitConfig" enabled
    And new "UpdateRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"adaptive": {"max_retention_rate": 0.5}, "custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "cd73a516-a481-4af5-8352-9b577465c77b", "type": "rum_rate_limit_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create or update a RUM rate limit configuration returns "OK" response
    Given operation "UpdateRumRateLimitConfig" enabled
    And new "UpdateRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"adaptive": {"max_retention_rate": 0.5}, "custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "cd73a516-a481-4af5-8352-9b577465c77b", "type": "rum_rate_limit_config"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM rate limit configuration returns "Bad Request" response
    Given operation "DeleteRumRateLimitConfig" enabled
    And new "DeleteRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM rate limit configuration returns "No Content" response
    Given operation "DeleteRumRateLimitConfig" enabled
    And new "DeleteRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM rate limit configuration returns "Not Found" response
    Given operation "DeleteRumRateLimitConfig" enabled
    And new "DeleteRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM rate limit configuration returns "Bad Request" response
    Given operation "GetRumRateLimitConfig" enabled
    And new "GetRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM rate limit configuration returns "Not Found" response
    Given operation "GetRumRateLimitConfig" enabled
    And new "GetRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM rate limit configuration returns "OK" response
    Given operation "GetRumRateLimitConfig" enabled
    And new "GetRumRateLimitConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
