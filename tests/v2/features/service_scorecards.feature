@endpoint(service-scorecards) @endpoint(service-scorecards-v2)
Feature: Service Scorecards
  API to create and update scorecard rules and outcomes. See [Service
  Scorecards](https://docs.datadoghq.com/service_catalog/scorecards) for
  more information.  This feature is currently in BETA. If you have any
  feedback, contact [Datadog support](https://docs.datadoghq.com/help/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceScorecards" API

  @generated @skip @team:DataDog/service-catalog
  Scenario: Associate workflow with rule returns "Bad Request" response
    Given operation "UpdateScorecardRuleWorkflow" enabled
    And new "UpdateScorecardRuleWorkflow" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And request contains "workflow_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Associate workflow with rule returns "No Content" response
    Given operation "UpdateScorecardRuleWorkflow" enabled
    And new "UpdateScorecardRuleWorkflow" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And request contains "workflow_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/service-catalog
  Scenario: Associate workflow with rule returns "Not Found" response
    Given operation "UpdateScorecardRuleWorkflow" enabled
    And new "UpdateScorecardRuleWorkflow" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And request contains "workflow_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create a new campaign returns "Bad Request" response
    Given operation "CreateScorecardCampaign" enabled
    And new "CreateScorecardCampaign" request
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create a new campaign returns "Created" response
    Given operation "CreateScorecardCampaign" enabled
    And new "CreateScorecardCampaign" request
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/service-catalog
  Scenario: Create a new rule returns "Bad Request" response
    Given operation "CreateScorecardRule" enabled
    And new "CreateScorecardRule" request
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scorecard_id": "NOT.FOUND"}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Create a new rule returns "Created" response
    Given operation "CreateScorecardRule" enabled
    And new "CreateScorecardRule" request
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
    Given operation "DeleteScorecardCampaign" enabled
    And new "DeleteScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a campaign returns "No Content" response
    Given operation "DeleteScorecardCampaign" enabled
    And new "DeleteScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a campaign returns "Not Found" response
    Given operation "DeleteScorecardCampaign" enabled
    And new "DeleteScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a rule returns "Bad Request" response
    Given operation "DeleteScorecardRule" enabled
    And new "DeleteScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Delete a rule returns "Not Found" response
    Given operation "DeleteScorecardRule" enabled
    And new "DeleteScorecardRule" request
    And request contains "rule_id" parameter with value "2a4f524e-168a-429d-bb75-7b1ffeab0cbb"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/service-catalog
  Scenario: Delete a rule returns "OK" response
    Given operation "DeleteScorecardRule" enabled
    And there is a valid "create_scorecard_rule" in the system
    And new "DeleteScorecardRule" request
    And request contains "rule_id" parameter from "create_scorecard_rule.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete rule workflow returns "Bad Request" response
    Given operation "DeleteScorecardRuleWorkflow" enabled
    And new "DeleteScorecardRuleWorkflow" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete rule workflow returns "No Content" response
    Given operation "DeleteScorecardRuleWorkflow" enabled
    And new "DeleteScorecardRuleWorkflow" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete rule workflow returns "Not Found" response
    Given operation "DeleteScorecardRuleWorkflow" enabled
    And new "DeleteScorecardRuleWorkflow" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Generate campaign report returns "Accepted" response
    Given operation "GenerateScorecardCampaignReport" enabled
    And new "GenerateScorecardCampaignReport" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"slack": {"channel_id": "C024BDQ4N", "channel_name": "service-scorecards", "workspace_id": "T024BDQ4N", "workspace_name": "datadog-workspace"}}, "type": "campaign-report"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/service-catalog
  Scenario: Generate campaign report returns "Bad Request" response
    Given operation "GenerateScorecardCampaignReport" enabled
    And new "GenerateScorecardCampaignReport" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"slack": {"channel_id": "C024BDQ4N", "channel_name": "service-scorecards", "workspace_id": "T024BDQ4N", "workspace_name": "datadog-workspace"}}, "type": "campaign-report"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Generate campaign report returns "Not Found" response
    Given operation "GenerateScorecardCampaignReport" enabled
    And new "GenerateScorecardCampaignReport" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"slack": {"channel_id": "C024BDQ4N", "channel_name": "service-scorecards", "workspace_id": "T024BDQ4N", "workspace_name": "datadog-workspace"}}, "type": "campaign-report"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Generate team-specific campaign reports returns "Accepted" response
    Given operation "GenerateScorecardCampaignTeamReports" enabled
    And new "GenerateScorecardCampaignTeamReports" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"entity_owners": [{"slack": {"channel_id": "C024BDQ4N", "workspace_id": "T024BDQ4N"}, "team_id": "550e8400-e29b-41d4-a716-446655440000"}]}, "type": "campaign-team-report"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/service-catalog
  Scenario: Generate team-specific campaign reports returns "Bad Request" response
    Given operation "GenerateScorecardCampaignTeamReports" enabled
    And new "GenerateScorecardCampaignTeamReports" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"entity_owners": [{"slack": {"channel_id": "C024BDQ4N", "workspace_id": "T024BDQ4N"}, "team_id": "550e8400-e29b-41d4-a716-446655440000"}]}, "type": "campaign-team-report"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Generate team-specific campaign reports returns "Not Found" response
    Given operation "GenerateScorecardCampaignTeamReports" enabled
    And new "GenerateScorecardCampaignTeamReports" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"entity_owners": [{"slack": {"channel_id": "C024BDQ4N", "workspace_id": "T024BDQ4N"}, "team_id": "550e8400-e29b-41d4-a716-446655440000"}]}, "type": "campaign-team-report"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a campaign returns "Bad Request" response
    Given operation "GetScorecardCampaign" enabled
    And new "GetScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a campaign returns "Not Found" response
    Given operation "GetScorecardCampaign" enabled
    And new "GetScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a campaign returns "OK" response
    Given operation "GetScorecardCampaign" enabled
    And new "GetScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all campaigns returns "Bad Request" response
    Given operation "ListScorecardCampaigns" enabled
    And new "ListScorecardCampaigns" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all campaigns returns "OK" response
    Given operation "ListScorecardCampaigns" enabled
    And new "ListScorecardCampaigns" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all rule outcomes returns "Bad Request" response
    Given operation "ListScorecardOutcomes" enabled
    And new "ListScorecardOutcomes" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: List all rule outcomes returns "OK" response
    Given operation "ListScorecardOutcomes" enabled
    And new "ListScorecardOutcomes" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/service-catalog @with-pagination
  Scenario: List all rule outcomes returns "OK" response with pagination
    Given operation "ListScorecardOutcomes" enabled
    And new "ListScorecardOutcomes" request
    And request contains "page[size]" parameter with value 2
    And request contains "fields[outcome]" parameter with value "state"
    And request contains "filter[outcome][service_name]" parameter with value "my-service"
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all rules returns "Bad Request" response
    Given operation "ListScorecardRules" enabled
    And new "ListScorecardRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: List all rules returns "OK" response
    Given operation "ListScorecardRules" enabled
    And new "ListScorecardRules" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/service-catalog @with-pagination
  Scenario: List all rules returns "OK" response with pagination
    Given operation "ListScorecardRules" enabled
    And new "ListScorecardRules" request
    And request contains "page[size]" parameter with value 2
    And request contains "fields[rule]" parameter with value "name"
    And request contains "filter[rule][custom]" parameter with value true
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 4 items

  @generated @skip @team:DataDog/service-catalog
  Scenario: List all scorecards returns "OK" response
    Given operation "ListScorecards" enabled
    And new "ListScorecards" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List default rules returns "OK" response
    Given operation "ListScorecardDefaultRules" enabled
    And new "ListScorecardDefaultRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List entity facets returns "Bad Request" response
    Given operation "ListScorecardFacets" enabled
    And new "ListScorecardFacets" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: List entity facets returns "OK" response
    Given operation "ListScorecardFacets" enabled
    And new "ListScorecardFacets" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: List scores by aggregation returns "Bad Request" response
    Given operation "ListScorecardScores" enabled
    And new "ListScorecardScores" request
    And request contains "aggregation" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: List scores by aggregation returns "OK" response
    Given operation "ListScorecardScores" enabled
    And new "ListScorecardScores" request
    And request contains "aggregation" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Set up rules for organization returns "Bad Request" response
    Given operation "SetupScorecardRules" enabled
    And new "SetupScorecardRules" request
    And body with value {"data": {"attributes": {"disabled_default_rules": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"]}, "type": "setup"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Set up rules for organization returns "No Content" response
    Given operation "SetupScorecardRules" enabled
    And new "SetupScorecardRules" request
    And body with value {"data": {"attributes": {"disabled_default_rules": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"]}, "type": "setup"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/service-catalog
  Scenario: Set up rules for organization returns "Not Found" response
    Given operation "SetupScorecardRules" enabled
    And new "SetupScorecardRules" request
    And body with value {"data": {"attributes": {"disabled_default_rules": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"]}, "type": "setup"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes asynchronously returns "Accepted" response
    Given operation "UpdateScorecardOutcomesAsync" enabled
    And there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardOutcomesAsync" request
    And body with value {"data": {"attributes": {"results": [{"rule_id": "{{create_scorecard_rule.data.id}}", "entity_reference": "service:my-service", "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 202 Accepted

  @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes asynchronously returns "Bad Request" response
    Given operation "UpdateScorecardOutcomesAsync" enabled
    And there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardOutcomesAsync" request
    And body with value {"data": {"attributes": {"results": [{"rule_id": "{{create_scorecard_rule.data.id}}", "entity_reference": "service:my-service", "state": "INVALID"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0]" has field "detail"

  @team:DataDog/service-catalog
  Scenario: Update Scorecard outcomes asynchronously returns "Conflict" response
    Given operation "UpdateScorecardOutcomesAsync" enabled
    And new "UpdateScorecardOutcomesAsync" request
    And body with value {"data": {"attributes": {"results": [{"rule_id": "INVALID.RULE_ID", "entity_reference": "service:my-service", "remarks": "See: <a href=\"https://app.datadoghq.com/services\">Services</a>", "state": "pass"}]}, "type": "batched-outcome"}}
    When the request is sent
    Then the response status is 409 Conflict
    And the response "errors" has length 1

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update a campaign returns "Bad Request" response
    Given operation "UpdateScorecardCampaign" enabled
    And new "UpdateScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update a campaign returns "Not Found" response
    Given operation "UpdateScorecardCampaign" enabled
    And new "UpdateScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update a campaign returns "OK" response
    Given operation "UpdateScorecardCampaign" enabled
    And new "UpdateScorecardCampaign" request
    And request contains "campaign_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Campaign to improve security posture for Q1 2024.", "due_date": "2024-03-31T23:59:59Z", "entity_scope": "kind:service AND team:platform", "guidance": "Please ensure all services pass the security requirements.", "key": "q1-security-2024", "name": "Q1 Security Campaign", "owner_id": "550e8400-e29b-41d4-a716-446655440000", "rule_ids": ["q8MQxk8TCqrHnWkx", "r9NRyl9UDrsIoXly"], "start_date": "2024-01-01T00:00:00Z", "status": "in_progress"}, "type": "campaign"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Update an existing rule returns "Bad Request" response
    Given operation "UpdateScorecardRule" enabled
    And new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Update an existing rule returns "Rule updated successfully" response
    Given operation "UpdateScorecardRule" enabled
    And there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "create_scorecard_rule.data.id"
    And body with value {"data": { "attributes" : {"enabled": true, "name": "{{create_scorecard_rule.data.attributes.name}}", "scorecard_name": "{{create_scorecard_rule.data.attributes.scorecard_name}}", "description": "Updated description via test"}}}
    When the request is sent
    Then the response status is 200 Rule updated successfully

  @team:DataDog/service-catalog
  Scenario: Update an existing scorecard rule returns "Bad Request" response
    Given operation "UpdateScorecardRule" enabled
    And there is a valid "create_scorecard_rule" in the system
    And new "UpdateScorecardRule" request
    And request contains "rule_id" parameter from "create_scorecard_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scorecard_id": "NOT.FOUND"}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Update an existing scorecard rule returns "Not Found" response
    Given operation "UpdateScorecardRule" enabled
    And new "UpdateScorecardRule" request
    And request contains "rule_id" parameter with value "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "level": 2, "name": "Team Defined", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
    When the request is sent
    Then the response status is 404 Not Found
