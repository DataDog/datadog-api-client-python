@endpoint(service-level-objective-corrections) @endpoint(service-level-objective-corrections-v1)
Feature: Service Level Objective Corrections
  SLO Status Corrections allow you to prevent specific time periods from
  negatively impacting your SLO’s status and error budget. You can use
  Status Corrections for various purposes, such as removing planned
  maintenance windows, non-business hours, or other time periods that do not
  correspond to genuine issues.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceLevelObjectiveCorrections" API

  @skip @team:DataDog/slo-app
  Scenario: Create an SLO correction returns "Bad Request" response
    Given there is a valid "slo" in the system
    And new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description":  "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/slo-app
  Scenario: Create an SLO correction returns "OK" response
    Given there is a valid "slo" in the system
    And new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description": "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "slo_id": "{{ slo.data[0].id }}", "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/slo-app
  Scenario: Create an SLO correction returns "SLO Not Found" response
    Given new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description": "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "slo_id": "sloId", "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 404 SLO Not Found

  @team:DataDog/slo-app
  Scenario: Create an SLO correction with rrule returns "OK" response
    Given there is a valid "slo" in the system
    And new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description": "{{ unique }}", "slo_id": "{{ slo.data[0].id }}", "start": {{ timestamp("now") }}, "duration": 3600, "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5", "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/slo-app
  Scenario: Delete an SLO correction returns "Not found" response
    Given new "DeleteSLOCorrection" request
    And request contains "slo_correction_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/slo-app
  Scenario: Delete an SLO correction returns "OK" response
    Given new "DeleteSLOCorrection" request
    And request contains "slo_correction_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/slo-app
  Scenario: Get all SLO corrections returns "OK" response
    Given there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "ListSLOCorrection" request
    And request contains "offset" parameter with value 1
    And request contains "limit" parameter with value 1
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1

  @generated @skip @team:DataDog/slo-app
  Scenario: Get an SLO correction for an SLO returns "Bad Request" response
    Given new "GetSLOCorrection" request
    And request contains "slo_correction_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/slo-app
  Scenario: Get an SLO correction for an SLO returns "OK" response
    Given there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "GetSLOCorrection" request
    And request contains "slo_correction_id" parameter from "correction.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/slo-app
  Scenario: Update an SLO correction returns "Bad Request" response
    Given there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "UpdateSLOCorrection" request
    And request contains "slo_correction_id" parameter from "correction.data.id"
    And body with value {"data": {"attributes": {"category": "Invalid Test"}, "type": "correction"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Update an SLO correction returns "Not Found" response
    Given new "UpdateSLOCorrection" request
    And request contains "slo_correction_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "duration": 3600, "end": 1600000000, "rrule": "FREQ=DAILY;INTERVAL=10;COUNT=5", "start": 1600000000, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/slo-app
  Scenario: Update an SLO correction returns "OK" response
    Given there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "UpdateSLOCorrection" request
    And request contains "slo_correction_id" parameter from "correction.data.id"
    And body with value {"data": {"attributes": {"category": "Deployment", "description": "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "correction.data.id"
    And the response "data.attributes.slo_id" has the same value as "correction.data.attributes.slo_id"
    And the response "data.attributes.category" is equal to "Deployment"
