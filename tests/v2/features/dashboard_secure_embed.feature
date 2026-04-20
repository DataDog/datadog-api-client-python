@endpoint(dashboard-secure-embed) @endpoint(dashboard-secure-embed-v2) @endpoint(https://api.datadoghq.com) @endpoint(https://api.datadoghq.eu) @endpoint(https://api.ddog-gov.com) @endpoint(https://api.us5.datadoghq.com)
Feature: Dashboard Secure Embed
  Manage securely embedded Datadog dashboards. Secure embeds use HMAC-SHA256
  signed sessions for authentication, enabling customers to embed dashboards
  in their own applications with server-side auth control. Unlike public
  dashboards (open URL) or invite dashboards (email-based access), secure
  embeds provide programmatic access control.  **Requirements:** - **Embed**
  sharing must be enabled under **Organization Settings** > **Public
  Sharing** > **Shared Dashboards**. - You need [an API key and an
  application key](https://docs.datadoghq.com/account_management/api-app-
  keys/) to interact with these endpoints.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardSecureEmbed" API

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Create a secure embed for a dashboard returns "Conflict — max 1000 share URLs per dashboard exceeded" response
    Given operation "CreateDashboardSecureEmbed" enabled
    And new "CreateDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"global_time": {"live_span": "1h"}, "global_time_selectable": true, "selectable_template_vars": [{"default_values": ["1"], "name": "org_id", "prefix": "org_id", "visible_tags": ["1"]}], "status": "active", "title": "Q1 Metrics Dashboard", "viewing_preferences": {"high_density": false, "theme": "system"}}, "type": "secure_embed_request"}}
    When the request is sent
    Then the response status is 409 Conflict — max 1000 share URLs per dashboard exceeded

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Create a secure embed for a dashboard returns "Dashboard Not Found" response
    Given operation "CreateDashboardSecureEmbed" enabled
    And new "CreateDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"global_time": {"live_span": "1h"}, "global_time_selectable": true, "selectable_template_vars": [{"default_values": ["1"], "name": "org_id", "prefix": "org_id", "visible_tags": ["1"]}], "status": "active", "title": "Q1 Metrics Dashboard", "viewing_preferences": {"high_density": false, "theme": "system"}}, "type": "secure_embed_request"}}
    When the request is sent
    Then the response status is 404 Dashboard Not Found

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Create a secure embed for a dashboard returns "OK" response
    Given operation "CreateDashboardSecureEmbed" enabled
    And new "CreateDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"global_time": {"live_span": "1h"}, "global_time_selectable": true, "selectable_template_vars": [{"default_values": ["1"], "name": "org_id", "prefix": "org_id", "visible_tags": ["1"]}], "status": "active", "title": "Q1 Metrics Dashboard", "viewing_preferences": {"high_density": false, "theme": "system"}}, "type": "secure_embed_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Delete a secure embed for a dashboard returns "No Content" response
    Given operation "DeleteDashboardSecureEmbed" enabled
    And new "DeleteDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Delete a secure embed for a dashboard returns "Not Found" response
    Given operation "DeleteDashboardSecureEmbed" enabled
    And new "DeleteDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Get a secure embed for a dashboard returns "Not Found" response
    Given operation "GetDashboardSecureEmbed" enabled
    And new "GetDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Get a secure embed for a dashboard returns "OK" response
    Given operation "GetDashboardSecureEmbed" enabled
    And new "GetDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Update a secure embed for a dashboard returns "Not Found" response
    Given operation "UpdateDashboardSecureEmbed" enabled
    And new "UpdateDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"global_time": {"live_span": "1h"}, "global_time_selectable": true, "selectable_template_vars": [{"default_values": ["1"], "name": "org_id", "prefix": "org_id", "visible_tags": ["1"]}], "status": "active", "title": "Q1 Metrics Dashboard (Updated)", "viewing_preferences": {"high_density": false, "theme": "system"}}, "type": "secure_embed_update_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dashboardsnotebooks-backend
  Scenario: Update a secure embed for a dashboard returns "OK" response
    Given operation "UpdateDashboardSecureEmbed" enabled
    And new "UpdateDashboardSecureEmbed" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"global_time": {"live_span": "1h"}, "global_time_selectable": true, "selectable_template_vars": [{"default_values": ["1"], "name": "org_id", "prefix": "org_id", "visible_tags": ["1"]}], "status": "active", "title": "Q1 Metrics Dashboard (Updated)", "viewing_preferences": {"high_density": false, "theme": "system"}}, "type": "secure_embed_update_request"}}
    When the request is sent
    Then the response status is 200 OK
