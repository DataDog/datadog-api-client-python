@endpoint(entity-risk-scores) @endpoint(entity-risk-scores-v2)
Feature: Entity Risk Scores
  Retrieves security risk scores for entities in your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "EntityRiskScores" API

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get Entity Risk Score returns "Bad Request" response
    Given operation "GetEntityRiskScore" enabled
    And new "GetEntityRiskScore" request
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get Entity Risk Score returns "Not Found" response
    Given operation "GetEntityRiskScore" enabled
    And new "GetEntityRiskScore" request
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get Entity Risk Score returns "OK" response
    Given operation "GetEntityRiskScore" enabled
    And new "GetEntityRiskScore" request
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List Entity Risk Scores returns "Bad Request" response
    Given operation "ListEntityRiskScores" enabled
    And new "ListEntityRiskScores" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List Entity Risk Scores returns "OK" response
    Given operation "ListEntityRiskScores" enabled
    And new "ListEntityRiskScores" request
    When the request is sent
    Then the response status is 200 OK
