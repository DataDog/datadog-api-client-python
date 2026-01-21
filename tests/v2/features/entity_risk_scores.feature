@endpoint(entity-risk-scores) @endpoint(entity-risk-scores-v2)
Feature: Entity Risk Scores
  Retrieves security risk scores for entities in your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "EntityRiskScores" API
    And operation "ListEntityRiskScores" enabled
    And new "ListEntityRiskScores" request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List Entity Risk Scores returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List Entity Risk Scores returns "OK" response
    When the request is sent
    Then the response status is 200 OK
