@endpoint(service-level-objectives)
Feature: Service Level Objectives
  [Service Level Objectives](https://docs.datadoghq.com/monitors/service_lev
  el_objectives/#configuration) (or SLOs) are a key part of the site
  reliability engineering toolkit. SLOs provide a framework for defining
  clear targets around application performance, which ultimately help teams
  provide a consistent customer experience, balance feature development with
  platform stability, and improve communication with internal and external
  users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceLevelObjectives" API

  @generated @skip
  Scenario: Bulk Delete SLO Timeframes returns "Bad Request" response
    Given new "DeleteSLOTimeframeInBulk" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Bulk Delete SLO Timeframes returns "OK" response
    Given new "DeleteSLOTimeframeInBulk" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Check if SLOs can be safely deleted returns "Bad Request" response
    Given new "CheckCanDeleteSLO" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Check if SLOs can be safely deleted returns "Conflict" response
    Given new "CheckCanDeleteSLO" request
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip
  Scenario: Check if SLOs can be safely deleted returns "OK" response
    Given new "CheckCanDeleteSLO" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a SLO object returns "Bad Request" response
    Given new "CreateSLO" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a SLO object returns "OK" response
    Given new "CreateSLO" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a SLO returns "Conflict" response
    Given new "DeleteSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip
  Scenario: Delete a SLO returns "Not found" response
    Given new "DeleteSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Delete a SLO returns "OK" response
    Given new "DeleteSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a SLO's details returns "Not found" response
    Given new "GetSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Get a SLO's details returns "OK" response
    Given new "GetSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an SLO's history returns "Bad Request" response
    Given operation "GetSLOHistory" enabled
    And new "GetSLOHistory" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get an SLO's history returns "Not Found" response
    Given operation "GetSLOHistory" enabled
    And new "GetSLOHistory" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get an SLO's history returns "OK" response
    Given operation "GetSLOHistory" enabled
    And new "GetSLOHistory" request
    And request contains "slo_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Search SLOs returns "Bad Request" response
    Given new "ListSLOs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Search SLOs returns "Not Found" response
    Given new "ListSLOs" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Search SLOs returns "OK" response
    Given new "ListSLOs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a SLO returns "Bad Request" response
    Given new "UpdateSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a SLO returns "Not Found" response
    Given new "UpdateSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Update a SLO returns "OK" response
    Given new "UpdateSLO" request
    And request contains "slo_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK
