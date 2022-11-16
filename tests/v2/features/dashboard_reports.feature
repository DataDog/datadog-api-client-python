@endpoint(dashboard-reports) @endpoint(dashboard-reports-v2)
Feature: Dashboard Reports
  Dashboard reports allow for sending scheduled emails with snapshots of
  your dashboard's widgets, using a given timeframe and frequency, to
  multiple email recipients.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardReports" API

  @generated @skip @team:DataDog/dashboards
  Scenario: Create a new Dashboard Report returns "Bad Request" response
    Given new "CreateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of\nour Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": "1st", "repeat_on_day_of_week": "Monday", "timezone": "America/New_York"}, "template_variables": {"bar": "*", "foo": "*"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards
  Scenario: Create a new Dashboard Report returns "Conflict" response
    Given new "CreateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of\nour Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": "1st", "repeat_on_day_of_week": "Monday", "timezone": "America/New_York"}, "template_variables": {"bar": "*", "foo": "*"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/dashboards
  Scenario: Create a new Dashboard Report returns "Created" response
    Given there is a valid "dashboard" in the system
    And new "CreateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of our Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": null, "repeat_on_day_of_week": null, "timezone": "America/New_York"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.description" is equal to "This report summarizes the recent errors, latency, and uptime of our Web Application Backend."
    And the response "data.attributes.destinations.email.recipient_addresses" has length 1
    And the response "data.attributes.destinations.email.recipient_addresses[0]" is equal to "jane.doe@example.com"
    And the response "data.attributes.schedule.active" is equal to true
    And the response "data.attributes.schedule.frequency" is equal to "1d"
    And the response "data.attributes.schedule.repeat_at" is equal to "13:30"
    And the response "data.attributes.schedule.repeat_on_day_of_month" is equal to null
    And the response "data.attributes.schedule.repeat_on_day_of_week" is equal to null
    And the response "data.attributes.schedule.timezone" is equal to "America/New_York"
    And the response "data.attributes.timeframe" is equal to "1w"
    And the response "data.attributes.title" is equal to "Summary of recent stability and performance for Web Application Backend"
    And the response "data.relationships.dashboard.data.id" is equal to "{{ dashboard.id }}"
    And the response "data.relationships.dashboard.data.type" is equal to "dashboards"
    And the response "data.type" is equal to "dashboard_reports"

  @generated @skip @team:DataDog/dashboards
  Scenario: Create a new Dashboard Report returns "Not Found" response
    Given new "CreateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of\nour Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": "1st", "repeat_on_day_of_week": "Monday", "timezone": "America/New_York"}, "template_variables": {"bar": "*", "foo": "*"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Create a new Dashboard Report returns "Unprocessable Entity" response
    Given there is a valid "screenboard_dashboard" in the system
    And new "CreateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "screenboard_dashboard.id"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of our Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": null, "repeat_on_day_of_week": null, "timezone": "America/New_York"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/dashboards
  Scenario: Delete a Dashboard Report returns "No Content" response
    Given there is a valid "dashboard" in the system
    And there is a valid "dashboard_report" in the system
    And new "DeleteDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    And request contains "report_uuid" parameter from "dashboard_report.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dashboards
  Scenario: Delete a Dashboard Report returns "Not Found" response
    Given new "DeleteDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "report_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dashboards
  Scenario: Delete a Dashboard Report returns "Unprocessable Entity" response
    Given new "DeleteDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "report_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/dashboards
  Scenario: Get Dashboard Reports for a Dashboard returns "Not Found" response
    Given new "GetDashboardReportConfigsList" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Get Dashboard Reports for a Dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And there is a valid "dashboard_report" in the system
    And new "GetDashboardReportConfigsList" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/dashboards
  Scenario: Get Dashboard Reports for a Dashboard returns "Unprocessable Entity" response
    Given there is a valid "screenboard_dashboard" in the system
    And new "GetDashboardReportConfigsList" request
    And request contains "dashboard_id" parameter from "screenboard_dashboard.id"
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/dashboards
  Scenario: Get a Dashboard Report returns "Not Found" response
    Given new "GetDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "report_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Get a Dashboard Report returns "OK" response
    Given there is a valid "dashboard" in the system
    And there is a valid "dashboard_report" in the system
    And new "GetDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    And request contains "report_uuid" parameter from "dashboard_report.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.description" is equal to "This report summarizes the recent errors, latency, and uptime of our Web Application Backend."
    And the response "data.attributes.destinations.email.recipient_addresses" has length 1
    And the response "data.attributes.destinations.email.recipient_addresses[0]" is equal to "jane.doe@example.com"
    And the response "data.attributes.schedule.active" is equal to true
    And the response "data.attributes.schedule.frequency" is equal to "1d"
    And the response "data.attributes.schedule.repeat_at" is equal to "13:30"
    And the response "data.attributes.schedule.repeat_on_day_of_month" is equal to null
    And the response "data.attributes.schedule.repeat_on_day_of_week" is equal to null
    And the response "data.attributes.schedule.timezone" is equal to "America/New_York"
    And the response "data.attributes.timeframe" is equal to "1w"
    And the response "data.attributes.title" is equal to "Summary of recent stability and performance for Web Application Backend"
    And the response "data.id" is equal to "{{ dashboard_report.data.id }}"
    And the response "data.relationships.dashboard.data.id" is equal to "{{ dashboard.id }}"
    And the response "data.relationships.dashboard.data.type" is equal to "dashboards"
    And the response "data.type" is equal to "dashboard_reports"

  @generated @skip @team:DataDog/dashboards
  Scenario: Get a Dashboard Report returns "Unprocessable Entity" response
    Given new "GetDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "report_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/dashboards
  Scenario: Update Dashboard Report returns "Bad Request" response
    Given there is a valid "dashboard" in the system
    And there is a valid "dashboard_report" in the system
    And new "UpdateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    And request contains "report_uuid" parameter from "dashboard_report.data.id"
    And body with value {"data": {"attributes": {"schedule": {"repeat_on_day_of_month": "1st", "repeat_on_day_of_week": "Monday"}}, "id": "{{ dashboard_report.data.id }}", "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards
  Scenario: Update Dashboard Report returns "Conflict" response
    Given new "UpdateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "report_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of\nour Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": "1st", "repeat_on_day_of_week": "Monday", "timezone": "America/New_York"}, "template_variables": {"bar": "*", "foo": "*"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "id": "d34db33f-1337-4a7a-d099-da7ad0900002", "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/dashboards
  Scenario: Update Dashboard Report returns "Not Found" response
    Given new "UpdateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "report_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of\nour Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": "1st", "repeat_on_day_of_week": "Monday", "timezone": "America/New_York"}, "template_variables": {"bar": "*", "foo": "*"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "id": "d34db33f-1337-4a7a-d099-da7ad0900002", "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Update Dashboard Report returns "OK" response
    Given there is a valid "dashboard" in the system
    And there is a valid "dashboard_report" in the system
    And new "UpdateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    And request contains "report_uuid" parameter from "dashboard_report.data.id"
    And body with value {"data": {"attributes": {"schedule": {"active": false}, "title": "Summary of performance for Web Application Backend"}, "id": "{{ dashboard_report.data.id }}", "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.description" is equal to "This report summarizes the recent errors, latency, and uptime of our Web Application Backend."
    And the response "data.attributes.destinations.email.recipient_addresses" has length 1
    And the response "data.attributes.destinations.email.recipient_addresses[0]" is equal to "jane.doe@example.com"
    And the response "data.attributes.schedule.active" is equal to false
    And the response "data.attributes.schedule.frequency" is equal to "1d"
    And the response "data.attributes.schedule.repeat_at" is equal to "13:30"
    And the response "data.attributes.schedule.repeat_on_day_of_month" is equal to null
    And the response "data.attributes.schedule.repeat_on_day_of_week" is equal to null
    And the response "data.attributes.schedule.timezone" is equal to "America/New_York"
    And the response "data.attributes.timeframe" is equal to "1w"
    And the response "data.attributes.title" is equal to "Summary of performance for Web Application Backend"
    And the response "data.id" is equal to "{{ dashboard_report.data.id }}"
    And the response "data.relationships.dashboard.data.id" is equal to "{{ dashboard.id }}"
    And the response "data.relationships.dashboard.data.type" is equal to "dashboards"
    And the response "data.type" is equal to "dashboard_reports"

  @generated @skip @team:DataDog/dashboards
  Scenario: Update Dashboard Report returns "Unprocessable Entity" response
    Given new "UpdateDashboardReportConfig" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And request contains "report_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "This report summarizes the recent errors, latency, and uptime of\nour Web Application Backend.", "destinations": {"email": {"recipient_addresses": ["jane.doe@example.com"]}}, "schedule": {"active": true, "frequency": "1d", "repeat_at": "13:30", "repeat_on_day_of_month": "1st", "repeat_on_day_of_week": "Monday", "timezone": "America/New_York"}, "template_variables": {"bar": "*", "foo": "*"}, "timeframe": "1w", "title": "Summary of recent stability and performance for Web Application Backend"}, "id": "d34db33f-1337-4a7a-d099-da7ad0900002", "type": "dashboard_reports"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
