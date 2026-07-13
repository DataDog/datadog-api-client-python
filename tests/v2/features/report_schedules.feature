@endpoint(report-schedules) @endpoint(report-schedules-v2)
Feature: Report Schedules
  Create and manage scheduled reports. A scheduled report renders a
  dashboard or integration dashboard on a recurring cadence and delivers it
  to a set of recipients over email, Slack, or Microsoft Teams.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ReportSchedules" API

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a report schedule returns "Bad Request" response
    Given operation "CreateReportSchedule" enabled
    And new "CreateReportSchedule" request
    And body with value {"data": {"attributes": {"delivery_format": "pdf", "description": "Weekly summary of infrastructure health.", "recipients": ["user@example.com", "slack:T01234567.C01234567.alerts", "teams:11111111-1111-1111-1111-111111111111|22222222-2222-2222-2222-222222222222|19:exampleChannelId@thread.tacv2"], "resource_id": "abc-def-ghi", "resource_type": "dashboard", "rrule": "DTSTART;TZID=America/New_York:20260601T090000\nRRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0", "tab_id": "66666666-7777-8888-9999-000000000000", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "title": "Weekly Infrastructure Report"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a report schedule returns "CREATED" response
    Given operation "CreateReportSchedule" enabled
    And new "CreateReportSchedule" request
    And body with value {"data": {"attributes": {"delivery_format": "pdf", "description": "Weekly summary of infrastructure health.", "recipients": ["user@example.com", "slack:T01234567.C01234567.alerts", "teams:11111111-1111-1111-1111-111111111111|22222222-2222-2222-2222-222222222222|19:exampleChannelId@thread.tacv2"], "resource_id": "abc-def-ghi", "resource_type": "dashboard", "rrule": "DTSTART;TZID=America/New_York:20260601T090000\nRRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0", "tab_id": "66666666-7777-8888-9999-000000000000", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "title": "Weekly Infrastructure Report"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a report schedule returns "Not Found" response
    Given operation "CreateReportSchedule" enabled
    And new "CreateReportSchedule" request
    And body with value {"data": {"attributes": {"delivery_format": "pdf", "description": "Weekly summary of infrastructure health.", "recipients": ["user@example.com", "slack:T01234567.C01234567.alerts", "teams:11111111-1111-1111-1111-111111111111|22222222-2222-2222-2222-222222222222|19:exampleChannelId@thread.tacv2"], "resource_id": "abc-def-ghi", "resource_type": "dashboard", "rrule": "DTSTART;TZID=America/New_York:20260601T090000\nRRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0", "tab_id": "66666666-7777-8888-9999-000000000000", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "title": "Weekly Infrastructure Report"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Delete a report schedule returns "Bad Request" response
    Given new "DeleteReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Delete a report schedule returns "Not Found" response
    Given new "DeleteReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Delete a report schedule returns "OK" response
    Given new "DeleteReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get a report schedule returns "Bad Request" response
    Given new "GetReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get a report schedule returns "Not Found" response
    Given new "GetReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get a report schedule returns "OK" response
    Given new "GetReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get report schedules for a resource returns "Bad Request" response
    Given new "GetReportSchedulesForResource" request
    And request contains "resource_type" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get report schedules for a resource returns "Not Found" response
    Given new "GetReportSchedulesForResource" request
    And request contains "resource_type" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get report schedules for a resource returns "OK" response
    Given new "GetReportSchedulesForResource" request
    And request contains "resource_type" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List dataset report schedules returns "Bad Request" response
    Given new "ListDatasetReportSchedules" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List dataset report schedules returns "Not Found" response
    Given new "ListDatasetReportSchedules" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List dataset report schedules returns "OK" response
    Given new "ListDatasetReportSchedules" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List report schedules returns "Bad Request" response
    Given new "ListReportSchedules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List report schedules returns "Not Found" response
    Given new "ListReportSchedules" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List report schedules returns "OK" response
    Given new "ListReportSchedules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Print a report returns "Bad Request" response
    Given new "PrintReport" request
    And body with value {"data": {"attributes": {"from_ts": 1780318800000, "resource_id": "abc-def-ghi", "resource_type": "dashboard", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "to_ts": 1780923600000}, "type": "report"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Print a report returns "Not Found" response
    Given new "PrintReport" request
    And body with value {"data": {"attributes": {"from_ts": 1780318800000, "resource_id": "abc-def-ghi", "resource_type": "dashboard", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "to_ts": 1780923600000}, "type": "report"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Print a report returns "OK" response
    Given new "PrintReport" request
    And body with value {"data": {"attributes": {"from_ts": 1780318800000, "resource_id": "abc-def-ghi", "resource_type": "dashboard", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "to_ts": 1780923600000}, "type": "report"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Print a report returns "Unprocessable Entity" response
    Given new "PrintReport" request
    And body with value {"data": {"attributes": {"from_ts": 1780318800000, "resource_id": "abc-def-ghi", "resource_type": "dashboard", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "to_ts": 1780923600000}, "type": "report"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Toggle a report schedule returns "Bad Request" response
    Given new "ToggleReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "active"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Toggle a report schedule returns "Not Found" response
    Given new "ToggleReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "active"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Toggle a report schedule returns "OK" response
    Given new "ToggleReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "active"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Update a report schedule returns "Bad Request" response
    Given operation "PatchReportSchedule" enabled
    And new "PatchReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"delivery_format": "pdf", "description": "Updated weekly summary of infrastructure health.", "recipients": ["user@example.com", "slack:T01234567.C01234567.alerts", "teams:11111111-1111-1111-1111-111111111111|22222222-2222-2222-2222-222222222222|19:exampleChannelId@thread.tacv2"], "rrule": "DTSTART;TZID=America/New_York:20260601T090000\nRRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0", "tab_id": "66666666-7777-8888-9999-000000000000", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "title": "Weekly Infrastructure Report"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Update a report schedule returns "Not Found" response
    Given operation "PatchReportSchedule" enabled
    And new "PatchReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"delivery_format": "pdf", "description": "Updated weekly summary of infrastructure health.", "recipients": ["user@example.com", "slack:T01234567.C01234567.alerts", "teams:11111111-1111-1111-1111-111111111111|22222222-2222-2222-2222-222222222222|19:exampleChannelId@thread.tacv2"], "rrule": "DTSTART;TZID=America/New_York:20260601T090000\nRRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0", "tab_id": "66666666-7777-8888-9999-000000000000", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "title": "Weekly Infrastructure Report"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Update a report schedule returns "OK" response
    Given operation "PatchReportSchedule" enabled
    And new "PatchReportSchedule" request
    And request contains "schedule_uuid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"delivery_format": "pdf", "description": "Updated weekly summary of infrastructure health.", "recipients": ["user@example.com", "slack:T01234567.C01234567.alerts", "teams:11111111-1111-1111-1111-111111111111|22222222-2222-2222-2222-222222222222|19:exampleChannelId@thread.tacv2"], "rrule": "DTSTART;TZID=America/New_York:20260601T090000\nRRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0", "tab_id": "66666666-7777-8888-9999-000000000000", "template_variables": [{"name": "env", "values": ["prod"]}], "timeframe": "1w", "timezone": "America/New_York", "title": "Weekly Infrastructure Report"}, "type": "schedule"}}
    When the request is sent
    Then the response status is 200 OK
