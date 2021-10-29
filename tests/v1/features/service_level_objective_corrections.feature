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

  @skip
  Scenario: Create an SLO correction returns "Bad Request" response
    Given there is a valid "slo" in the system
    And operation "CreateSLOCorrection" enabled
    And new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description":  "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Create an SLO correction returns "OK" response
    Given there is a valid "slo" in the system
    And operation "CreateSLOCorrection" enabled
    And new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description": "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "slo_id": "{{ slo.data[0].id }}", "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 200 OK

  @skip
  Scenario: Create an SLO correction returns "SLO Not Found" response
    Given operation "CreateSLOCorrection" enabled
    And new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description": "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "slo_id": "sloId", "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 404 SLO Not Found

  Scenario: Create an SLO correction with rrule returns "OK" response
    Given there is a valid "slo" in the system
    And operation "CreateSLOCorrection" enabled
    And new "CreateSLOCorrection" request
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description": "{{ unique }}", "slo_id": "{{ slo.data[0].id }}", "start": {{ timestamp("now") }}, "duration": 3600, "rrule": "RRULE:FREQ=DAILY;INTERVAL=10;COUNT=5", "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete an SLO correction returns "Not found" response
    Given operation "DeleteSLOCorrection" enabled
    And new "DeleteSLOCorrection" request
    And request contains "slo_correction_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Delete an SLO correction returns "OK" response
    Given operation "DeleteSLOCorrection" enabled
    And new "DeleteSLOCorrection" request
    And request contains "slo_correction_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get all SLO corrections returns "OK" response
    Given operation "ListSLOCorrection" enabled
    And there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "ListSLOCorrection" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an SLO correction for an SLO returns "Bad Request" response
    Given operation "GetSLOCorrection" enabled
    And new "GetSLOCorrection" request
    And request contains "slo_correction_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Get an SLO correction for an SLO returns "OK" response
    Given operation "GetSLOCorrection" enabled
    And there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "GetSLOCorrection" request
    And request contains "slo_correction_id" parameter from "correction.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip
  Scenario: Update an SLO correction returns "Bad Request" response
    Given operation "UpdateSLOCorrection" enabled
    And there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "UpdateSLOCorrection" request
    And request contains "slo_correction_id" parameter from "correction.data.id"
    And body with value {"data": {"attributes": {"category": "Invalid Test"}, "type": "correction"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update an SLO correction returns "Not Found" response
    Given operation "UpdateSLOCorrection" enabled
    And new "UpdateSLOCorrection" request
    And request contains "slo_correction_id" parameter from "<PATH>"
    And body with value {"data": {"attributes": {"category": "Scheduled Maintenance", "description": null, "duration": 3600, "end": 1600000000, "rrule": "RRULE:FREQ=DAILY;INTERVAL=10;COUNT=5", "start": 1600000000, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 404 Not Found

  Scenario: Update an SLO correction returns "OK" response
    Given there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And operation "UpdateSLOCorrection" enabled
    And new "UpdateSLOCorrection" request
    And request contains "slo_correction_id" parameter from "correction.data.id"
    And body with value {"data": {"attributes": {"category": "Deployment", "description": "{{ unique }}", "end": {{ timestamp("now + 1h") }}, "start": {{ timestamp("now") }}, "timezone": "UTC"}, "type": "correction"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "correction.data.id"
    And the response "data.attributes.slo_id" has the same value as "correction.data.attributes.slo_id"
    And the response "data.attributes.category" is equal to "Deployment"
