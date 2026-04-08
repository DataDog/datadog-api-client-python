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

  @team:DataDog/service-catalog
  Scenario: Create a new rule returns "Bad Request" response
    Given new "CreateScorecardRule" request
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scorecard_id": "NOT.FOUND"}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Create a new rule returns "Created" response
    Given new "CreateScorecardRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "{{unique}}", "scorecard_name": "Observability Best Practices"}, "type": "rule"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.scorecard_name" is equal to "Observability Best Practices"
    And the response "data.relationships.scorecard.data" has field "id"

  @team:DataDog/service-catalog
  Scenario: Create outcomes batch returns "Bad Request" response
    Given there is a valid "create_scorecard_rule" in the system
    And operation "CreateScorecardOutcomesBatch" enabled
    And new "CreateScorecardOutcomesBatch" request
    And body with value {"data": {"attributes": {"results": [{"remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "rule_id": "{{ create_scorecard_rule.data.id }}", "state": "pass", "service_name": ""}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Create outcomes batch returns "OK" response
    Given there is a valid "create_scorecard_rule" in the system
    And operation "CreateScorecardOutcomesBatch" enabled
    And new "CreateScorecardOutcomesBatch" request
    And body with value {"data": {"attributes": {"results": [{"remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "rule_id": "{{ create_scorecard_rule.data.id }}", "service_name": "my-service", "state": "pass"}]}, "type": "batched-outcome"}}
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

  @team:DataDog/service-catalog
  Scenario: Delete a rule returns "Not Found" response
    Given new "DeleteScorecardRule" request
    And request contains "rule_id" parameter with value "2a4f524e-168a-429d-bb75-7b1ffeab0cbb"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/service-catalog
  Scenario: Delete a rule returns "OK" response
    Given there is a valid "create_scorecard_rule" in the system
    And new "DeleteScorecardRule" request
    And request contains "rule_id" parameter from "create_scorecard_rule.data.id"
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

  @team:DataDog/service-catalog
  Scenario: List all rule outcomes returns "OK" response
    Given new "ListScorecardOutcomes" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/service-catalog @with-pagination
  Scenario: List all rule outcomes returns "OK" response with pagination
    Given new "ListScorecardOutcomes" request
    And request contains "page[size]" parameter with value 2
    And request contains "fields[outcome]" parameter with value "state"
    And request contains "filter[outcome][service_name]" parameter with value "my-service"
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all rules returns "Bad Request" response
    Given new "ListScorecardRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: List all rules returns "OK" response
    Given new "ListScorecardRules" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/service-catalog @with-pagination
  Scenario: List all rules returns "OK" response with pagination
    Given new "ListScorecardRules" request
    And request contains "page[size]" parameter with value 2
    And request contains "fields[rule]" parameter with value "name"
    And request contains "filter[rule][custom]" parameter with value true
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 4 items

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all scorecards returns "OK" response
    Given new "ListScorecards" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes asynchronously returns "Accepted" response
    Given there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardOutcomes" request
    And body with value {"data": {"attributes": {"results": [{"rule_id": "{{create_scorecard_rule.data.id}}", "entity_reference": "service:my-service", "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 202 Accepted

  @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes asynchronously returns "Bad Request" response
    Given there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardOutcomes" request
    And body with value {"data": {"attributes": {"results": [{"rule_id": "{{create_scorecard_rule.data.id}}", "entity_reference": "service:my-service", "state": "INVALID"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0]" has field "detail"

  @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes asynchronously returns "Conflict" response
    Given new "UpdateScorecardOutcomes" request
    And body with value {"data": {"attributes": {"results": [{"rule_id": "INVALID.RULE_ID", "entity_reference": "service:my-service", "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 409 Conflict
    And the response "errors" has length 1

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

  @team:DataDog/service-catalog
  Scenario: Update an existing rule returns "Rule updated successfully" response
    Given there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "create_scorecard_rule.data.id"
    And body with value {"data": {"type": "rule", "attributes": {"enabled": true, "name": "{{create_scorecard_rule.data.attributes.name}}", "scorecard_name": "{{create_scorecard_rule.data.attributes.scorecard_name}}", "description": "Updated description via test"}}}
    When the request is sent
    Then the response status is 200 Rule updated successfully

  @team:DataDog/service-catalog
  Scenario: Update an existing scorecard rule returns "Bad Request" response
    Given there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "create_scorecard_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scorecard_id": "NOT.FOUND"}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Update an existing scorecard rule returns "Not Found" response
    Given new "UpdateScorecardRule" request
    And request contains "rule_id" parameter with value "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update an existing scorecard rule returns "Rule updated successfully" response
    Given new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scope_query": "kind:service", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 200 Rule updated successfully
