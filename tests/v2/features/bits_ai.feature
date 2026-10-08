@endpoint(bits-ai) @endpoint(bits-ai-v2)
Feature: Bits AI
  Use the Bits AI endpoints to retrieve AI-powered investigations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "BitsAI" API

  @skip @team:ddoghq/bits-ai
  Scenario: Disable automatic investigations for a monitor
    Given operation "UpdateMonitorAutomation" enabled
    And there is a valid "monitor" in the system
    And new "UpdateMonitorAutomation" request
    And request contains "monitor_id" parameter from "monitor.id"
    And body with value {"data":{"type":"monitor_automation","attributes":{"enabled":false}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.enabled" is false

  @skip @team:ddoghq/bits-ai
  Scenario: Enable automatic investigations for a monitor
    Given operation "UpdateMonitorAutomation" enabled
    And there is a valid "monitor" in the system
    And new "UpdateMonitorAutomation" request
    And request contains "monitor_id" parameter from "monitor.id"
    And body with value {"data":{"type":"monitor_automation","attributes":{"enabled":true}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.enabled" is true

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Get a Bits AI investigation returns "Bad Request" response
    Given operation "GetInvestigation" enabled
    And new "GetInvestigation" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Get a Bits AI investigation returns "Not Found" response
    Given operation "GetInvestigation" enabled
    And new "GetInvestigation" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Get a Bits AI investigation returns "OK" response
    Given operation "GetInvestigation" enabled
    And new "GetInvestigation" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Get automatic investigation settings for a monitor returns "Invalid request or unsupported monitor type." response
    Given operation "GetMonitorAutomation" enabled
    And new "GetMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Invalid request or unsupported monitor type.

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Get automatic investigation settings for a monitor returns "Monitor not found or not visible to the caller." response
    Given operation "GetMonitorAutomation" enabled
    And new "GetMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Monitor not found or not visible to the caller.

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Get automatic investigation settings for a monitor returns "OK" response
    Given operation "GetMonitorAutomation" enabled
    And new "GetMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Get automatic investigation settings for a monitor returns "The monitor setting could not be updated." response
    Given operation "GetMonitorAutomation" enabled
    And new "GetMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 The monitor setting could not be updated.

  @generated @skip @team:ddoghq/bits-ai
  Scenario: List Bits AI investigations returns "Bad Request" response
    Given operation "ListInvestigations" enabled
    And new "ListInvestigations" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/bits-ai
  Scenario: List Bits AI investigations returns "OK" response
    Given operation "ListInvestigations" enabled
    And new "ListInvestigations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/bits-ai @with-pagination
  Scenario: List Bits AI investigations returns "OK" response with pagination
    Given operation "ListInvestigations" enabled
    And new "ListInvestigations" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/bits-ai
  Scenario: Read automatic investigation settings for a new monitor
    Given operation "GetMonitorAutomation" enabled
    And there is a valid "monitor" in the system
    And new "GetMonitorAutomation" request
    And request contains "monitor_id" parameter from "monitor.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.enabled" is false

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Trigger a Bits AI investigation returns "Bad Request" response
    Given operation "TriggerInvestigation" enabled
    And new "TriggerInvestigation" request
    And body with value {"data": {"attributes": {"trigger": {"monitor_alert_trigger": {"event_id": "1234567890123456789", "event_ts": 1700000000000, "monitor_id": 12345678}, "type": "monitor_alert_trigger"}}, "type": "trigger_investigation_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Trigger a Bits AI investigation returns "OK" response
    Given operation "TriggerInvestigation" enabled
    And new "TriggerInvestigation" request
    And body with value {"data": {"attributes": {"trigger": {"monitor_alert_trigger": {"event_id": "1234567890123456789", "event_ts": 1700000000000, "monitor_id": 12345678}, "type": "monitor_alert_trigger"}}, "type": "trigger_investigation_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Update monitor automatic investigation settings returns "Invalid request or unsupported monitor type." response
    Given operation "UpdateMonitorAutomation" enabled
    And new "UpdateMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true}, "type": "monitor_automation"}}
    When the request is sent
    Then the response status is 400 Invalid request or unsupported monitor type.

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Update monitor automatic investigation settings returns "Monitor not found or not visible to the caller." response
    Given operation "UpdateMonitorAutomation" enabled
    And new "UpdateMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true}, "type": "monitor_automation"}}
    When the request is sent
    Then the response status is 404 Monitor not found or not visible to the caller.

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Update monitor automatic investigation settings returns "OK" response
    Given operation "UpdateMonitorAutomation" enabled
    And new "UpdateMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true}, "type": "monitor_automation"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/bits-ai
  Scenario: Update monitor automatic investigation settings returns "The monitor setting could not be updated." response
    Given operation "UpdateMonitorAutomation" enabled
    And new "UpdateMonitorAutomation" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true}, "type": "monitor_automation"}}
    When the request is sent
    Then the response status is 412 The monitor setting could not be updated.
