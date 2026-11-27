@endpoint(rum-retention-quotas) @endpoint(rum-retention-quotas-v2)
Feature: RUM Retention Quotas
  Manage RUM retention quota configurations for your organization's RUM
  applications.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMRetentionQuotas" API

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create or update a RUM retention quota config returns "Bad Request" response
    Given there is a valid "rum_application" in the system
    And new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter from "rum_application.data.id"
    And body with value {"data": {"attributes": {"custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "00000000-0000-0000-0000-000000000000", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create or update a RUM retention quota config returns "Not Found" response
    Given new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"attributes": {"custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "00000000-0000-0000-0000-000000000000", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Create or update a RUM retention quota config returns "OK" response
    Given there is a valid "rum_application" in the system
    And new "UpsertRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter from "rum_application.data.id"
    And body with value {"data": {"attributes": {"custom": {"daily_reset_time": "08:00", "daily_reset_timezone": "+09:00", "quota_reached_action": "stop", "session_limit": 1000000, "window_type": "daily"}, "mode": "custom"}, "id": "{{ rum_application.data.id }}", "type": "rum_quota_config"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ rum_application.data.id }}"
    And the response "data.attributes.mode" is equal to "custom"
    And the response "data.attributes.custom.session_limit" is equal to 1000000

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "Bad Request" response
    Given new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "No Content" response
    Given there is a valid "rum_application" in the system
    And there is a valid "rum_quota_config" in the system
    And new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter from "rum_application.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Delete a RUM retention quota configuration returns "Not Found" response
    Given there is a valid "rum_application" in the system
    And new "DeleteRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter from "rum_application.data.id"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get a RUM retention quota configuration returns "Bad Request" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter from "REPLACE.ME"
    And request contains "scope_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get a RUM retention quota configuration returns "Not Found" response
    Given new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter with value "{{ uuid }}"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:ddoghq/rum-backend
  Scenario: Get a RUM retention quota configuration returns "OK" response
    Given there is a valid "rum_application" in the system
    And there is a valid "rum_quota_config" in the system
    And new "GetRumQuotaConfig" request
    And request contains "scope_type" parameter with value "application"
    And request contains "scope_id" parameter from "rum_application.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ rum_application.data.id }}"
    And the response "data.attributes.mode" is equal to "custom"
