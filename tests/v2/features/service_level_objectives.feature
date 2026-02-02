@endpoint(service-level-objectives) @endpoint(service-level-objectives-v2)
Feature: Service Level Objectives
  [Service Level Objectives](https://docs.datadoghq.com/monitors/service_lev
  el_objectives/#configuration) (SLOs) are a key part of the site
  reliability engineering toolkit. SLOs provide a framework for defining
  clear targets around application performance, which ultimately help teams
  provide a consistent customer experience, balance feature development with
  platform stability, and improve communication with internal and external
  users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceLevelObjectives" API

  @team:DataDog/slo-app
  Scenario: Create a new SLO report returns "Bad Request" response
    Given operation "CreateSLOReportJob" enabled
    And new "CreateSLOReportJob" request
    And body with value {"data": {"attributes": {"from_ts": {{ timestamp('now - 40d') }},  "to_ts": {{ timestamp('now') }}, "query": "slo_type:metric \"SLO Reporting Test\"", "interval": "bad-interval"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/slo-app
  Scenario: Create a new SLO report returns "OK" response
    Given operation "CreateSLOReportJob" enabled
    And new "CreateSLOReportJob" request
    And body with value {"data": {"attributes": {"from_ts": {{ timestamp('now - 40d') }},  "to_ts": {{ timestamp('now') }}, "query": "slo_type:metric \"SLO Reporting Test\"", "interval": "monthly", "timezone": "America/New_York"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "report_id"

  @team:DataDog/slo-app
  Scenario: Get SLO report returns "Bad Request" response
    Given operation "GetSLOReport" enabled
    And new "GetSLOReport" request
    And request contains "report_id" parameter with value "invalid-report-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/slo-app
  Scenario: Get SLO report returns "Not Found" response
    Given operation "GetSLOReport" enabled
    And new "GetSLOReport" request
    And request contains "report_id" parameter with value "2b468c54-f2a7-11ee-b0b4-ffe56bb6ad43"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/slo-app
  Scenario: Get SLO report returns "OK" response
    Given operation "GetSLOReport" enabled
    And new "GetSLOReport" request
    And request contains "report_id" parameter with value "9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/slo-app
  Scenario: Get SLO report status returns "Bad Request" response
    Given operation "GetSLOReportJobStatus" enabled
    And new "GetSLOReportJobStatus" request
    And request contains "report_id" parameter with value "invalid-report-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/slo-app
  Scenario: Get SLO report status returns "Not Found" response
    Given operation "GetSLOReportJobStatus" enabled
    And new "GetSLOReportJobStatus" request
    And request contains "report_id" parameter with value "2b468c54-f2a7-11ee-b0b4-ffe56bb6ad43"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/slo-app
  Scenario: Get SLO report status returns "OK" response
    Given operation "GetSLOReportJobStatus" enabled
    And new "GetSLOReportJobStatus" request
    And there is a valid "report" in the system
    And request contains "report_id" parameter from "report.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "report_id"

  @generated @skip @team:DataDog/slo-app
  Scenario: Get SLO status returns "Bad Request" response
    Given operation "GetSloStatus" enabled
    And new "GetSloStatus" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    And request contains "from_ts" parameter from "REPLACE.ME"
    And request contains "to_ts" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Get SLO status returns "Not Found" response
    Given operation "GetSloStatus" enabled
    And new "GetSloStatus" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    And request contains "from_ts" parameter from "REPLACE.ME"
    And request contains "to_ts" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/slo-app
  Scenario: Get SLO status returns "OK" response
    Given operation "GetSloStatus" enabled
    And new "GetSloStatus" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    And request contains "from_ts" parameter from "REPLACE.ME"
    And request contains "to_ts" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
