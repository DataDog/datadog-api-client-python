@endpoint(scorecards) @endpoint(scorecards-v2)
Feature: Scorecards
  API to create and update scorecard rules and outcomes. See
  [Scorecards](https://docs.datadoghq.com/service_catalog/scorecards) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Scorecards" API

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create a new campaign returns "Bad Request" response
    Given new "CreateScorecardCampaign" request
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create a new campaign returns "Created" response
    Given new "CreateScorecardCampaign" request
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create a new rule returns "Bad Request" response
    Given new "CreateScorecardRule" request
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scope_query": "kind:service", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create a new rule returns "Created" response
    Given new "CreateScorecardRule" request
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scope_query": "kind:service", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create outcomes batch returns "Bad Request" response
    Given operation "CreateScorecardOutcomesBatch" enabled
    And new "CreateScorecardOutcomesBatch" request
    And body with value {"data": {"attributes": {"results": [{"remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "rule_id": "q8MQxk8TCqrHnWkx", "service_name": "my-service", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create outcomes batch returns "OK" response
    Given operation "CreateScorecardOutcomesBatch" enabled
    And new "CreateScorecardOutcomesBatch" request
    And body with value {"data": {"attributes": {"results": [{"remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "rule_id": "q8MQxk8TCqrHnWkx", "service_name": "my-service", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a campaign returns "Bad Request" response
    Given new "DeleteScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a campaign returns "No Content" response
    Given new "DeleteScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a campaign returns "Not Found" response
    Given new "DeleteScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a rule returns "Bad Request" response
    Given new "DeleteScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a rule returns "Not Found" response
    Given new "DeleteScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a rule returns "OK" response
    Given new "DeleteScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a campaign returns "Bad Request" response
    Given new "GetScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a campaign returns "Not Found" response
    Given new "GetScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a campaign returns "OK" response
    Given new "GetScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all campaigns returns "Bad Request" response
    Given new "ListScorecardCampaigns" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all campaigns returns "OK" response
    Given new "ListScorecardCampaigns" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all rule outcomes returns "Bad Request" response
    Given new "ListScorecardOutcomes" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all rule outcomes returns "OK" response
    Given new "ListScorecardOutcomes" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog @with-pagination
  Scenario: List all rule outcomes returns "OK" response with pagination
    Given new "ListScorecardOutcomes" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all rules returns "Bad Request" response
    Given new "ListScorecardRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all rules returns "OK" response
    Given new "ListScorecardRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog @with-pagination
  Scenario: List all rules returns "OK" response with pagination
    Given new "ListScorecardRules" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all scorecards returns "OK" response
    Given new "ListScorecards" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes returns "Accepted" response
    Given new "UpdateScorecardOutcomes" request
    And body with value {"data": {"attributes": {"results": [{"entity_reference": "service:my-service", "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "rule_id": "q8MQxk8TCqrHnWkx", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes returns "Bad Request" response
    Given new "UpdateScorecardOutcomes" request
    And body with value {"data": {"attributes": {"results": [{"entity_reference": "service:my-service", "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "rule_id": "q8MQxk8TCqrHnWkx", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes returns "Conflict" response
    Given new "UpdateScorecardOutcomes" request
    And body with value {"data": {"attributes": {"results": [{"entity_reference": "service:my-service", "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "rule_id": "q8MQxk8TCqrHnWkx", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update a campaign returns "Bad Request" response
    Given new "UpdateScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update a campaign returns "Not Found" response
    Given new "UpdateScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update a campaign returns "OK" response
    Given new "UpdateScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update an existing scorecard rule returns "Bad Request" response
    Given new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scope_query": "kind:service", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update an existing scorecard rule returns "Rule updated successfully" response
    Given new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scope_query": "kind:service", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 200 Rule updated successfully
