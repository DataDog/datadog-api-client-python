@endpoint(bits-ai-sre) @endpoint(bits-ai-sre-v2)
Feature: Bits AI SRE
  Use the Bits AI SRE endpoints to retrieve AI-powered investigations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "BitsAISRE" API

  @generated @skip @team:DataDog/bits-ai
  Scenario: Get a Bits AI SRE investigation returns "Bad Request" response
    Given operation "GetInvestigation" enabled
    And new "GetInvestigation" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/bits-ai
  Scenario: Get a Bits AI SRE investigation returns "Not Found" response
    Given operation "GetInvestigation" enabled
    And new "GetInvestigation" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/bits-ai
  Scenario: Get a Bits AI SRE investigation returns "OK" response
    Given operation "GetInvestigation" enabled
    And new "GetInvestigation" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/bits-ai
  Scenario: List Bits AI SRE investigations returns "Bad Request" response
    Given operation "ListInvestigations" enabled
    And new "ListInvestigations" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/bits-ai
  Scenario: List Bits AI SRE investigations returns "OK" response
    Given operation "ListInvestigations" enabled
    And new "ListInvestigations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/bits-ai @with-pagination
  Scenario: List Bits AI SRE investigations returns "OK" response with pagination
    Given operation "ListInvestigations" enabled
    And new "ListInvestigations" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/bits-ai
  Scenario: Trigger a Bits AI SRE investigation returns "Bad Request" response
    Given operation "TriggerInvestigation" enabled
    And new "TriggerInvestigation" request
    And body with value {"data": {"attributes": {"trigger": {"monitor_alert_trigger": {"event_id": "1234567890123456789", "event_ts": 1700000000000, "monitor_id": 12345678}, "type": "monitor_alert_trigger"}}, "type": "trigger_investigation_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/bits-ai
  Scenario: Trigger a Bits AI SRE investigation returns "OK" response
    Given operation "TriggerInvestigation" enabled
    And new "TriggerInvestigation" request
    And body with value {"data": {"attributes": {"trigger": {"monitor_alert_trigger": {"event_id": "1234567890123456789", "event_ts": 1700000000000, "monitor_id": 12345678}, "type": "monitor_alert_trigger"}}, "type": "trigger_investigation_request"}}
    When the request is sent
    Then the response status is 200 OK
