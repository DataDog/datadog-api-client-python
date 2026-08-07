@endpoint(tag-rules) @endpoint(tag-rules-v2)
Feature: Tag Rules
  Tag Rules define rules that govern which tag values are accepted for a
  given tag key, scoped to a particular telemetry source (such as logs,
  spans, or metrics). Rules can be `blocking` (data not matching the rule is
  rejected) or `surfacing` (matching data is highlighted but not blocked).
  Each rule reports a compliance `score` derived from how much recent
  telemetry adheres to the rule.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TagRules" API

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Create a tag rule returns "Bad Request" response
    Given operation "CreateTagRule" enabled
    And new "CreateTagRule" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "Service tag must be one of api or web", "policy_type": "surfacing", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Create a tag rule returns "Conflict" response
    Given operation "CreateTagRule" enabled
    And new "CreateTagRule" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "Service tag must be one of api or web", "policy_type": "surfacing", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Create a tag rule returns "Created" response
    Given operation "CreateTagRule" enabled
    And new "CreateTagRule" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "Service tag must be one of api or web", "policy_type": "surfacing", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Delete a tag rule returns "Bad Request" response
    Given operation "DeleteTagRule" enabled
    And new "DeleteTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Delete a tag rule returns "No Content" response
    Given operation "DeleteTagRule" enabled
    And new "DeleteTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Delete a tag rule returns "Not Found" response
    Given operation "DeleteTagRule" enabled
    And new "DeleteTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag rule compliance score returns "Bad Request" response
    Given operation "GetTagRuleScore" enabled
    And new "GetTagRuleScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag rule compliance score returns "Not Found" response
    Given operation "GetTagRuleScore" enabled
    And new "GetTagRuleScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag rule compliance score returns "OK" response
    Given operation "GetTagRuleScore" enabled
    And new "GetTagRuleScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag rule returns "Bad Request" response
    Given operation "GetTagRule" enabled
    And new "GetTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag rule returns "Not Found" response
    Given operation "GetTagRule" enabled
    And new "GetTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag rule returns "OK" response
    Given operation "GetTagRule" enabled
    And new "GetTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List tag rules returns "Bad Request" response
    Given operation "ListTagRules" enabled
    And new "ListTagRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List tag rules returns "OK" response
    Given operation "ListTagRules" enabled
    And new "ListTagRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a tag rule returns "Bad Request" response
    Given operation "UpdateTagRule" enabled
    And new "UpdateTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"policy_type": "surfacing", "tag_value_patterns": []}, "id": "123", "type": "tag_policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a tag rule returns "Not Found" response
    Given operation "UpdateTagRule" enabled
    And new "UpdateTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"policy_type": "surfacing", "tag_value_patterns": []}, "id": "123", "type": "tag_policy"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a tag rule returns "OK" response
    Given operation "UpdateTagRule" enabled
    And new "UpdateTagRule" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"policy_type": "surfacing", "tag_value_patterns": []}, "id": "123", "type": "tag_policy"}}
    When the request is sent
    Then the response status is 200 OK
