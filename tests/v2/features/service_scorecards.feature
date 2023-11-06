@endpoint(service-scorecards) @endpoint(service-scorecards-v2)
Feature: Service Scorecards
  API to create, update scorecard rules and outcomes.  This feature is
  currently in BETA. If you have any feedback, contact [Datadog
  support](https://docs.datadoghq.com/help/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceScorecards" API

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create a new rule returns "Bad Request" response
    Given operation "CreateScorecardRule" enabled
    And new "CreateScorecardRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Team Defined", "scorecard_name": "Deployments automated via Deployment Trains"}, "type": "rule"}}
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
