@endpoint(tag-policies) @endpoint(tag-policies-v2)
Feature: Tag Policies
  Tag Policies define rules that govern which tag values are accepted for a
  given tag key, scoped to a particular telemetry source (such as logs,
  spans, or metrics). Policies can be `blocking` (data not matching the
  policy is rejected) or `surfacing` (matching data is highlighted but not
  blocked). Each policy reports a compliance `score` derived from how much
  recent telemetry adheres to the policy.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TagPolicies" API

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Create a tag policy returns "Bad Request" response
    Given operation "CreateTagPolicy" enabled
    And new "CreateTagPolicy" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "Service tag must be one of api or web", "policy_type": "surfacing", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Create a tag policy returns "Conflict" response
    Given operation "CreateTagPolicy" enabled
    And new "CreateTagPolicy" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "Service tag must be one of api or web", "policy_type": "surfacing", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Create a tag policy returns "Created" response
    Given operation "CreateTagPolicy" enabled
    And new "CreateTagPolicy" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "Service tag must be one of api or web", "policy_type": "surfacing", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Delete a tag policy returns "Bad Request" response
    Given operation "DeleteTagPolicy" enabled
    And new "DeleteTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Delete a tag policy returns "No Content" response
    Given operation "DeleteTagPolicy" enabled
    And new "DeleteTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Delete a tag policy returns "Not Found" response
    Given operation "DeleteTagPolicy" enabled
    And new "DeleteTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag policy compliance score returns "Bad Request" response
    Given operation "GetTagPolicyScore" enabled
    And new "GetTagPolicyScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag policy compliance score returns "Not Found" response
    Given operation "GetTagPolicyScore" enabled
    And new "GetTagPolicyScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag policy compliance score returns "OK" response
    Given operation "GetTagPolicyScore" enabled
    And new "GetTagPolicyScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag policy returns "Bad Request" response
    Given operation "GetTagPolicy" enabled
    And new "GetTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag policy returns "Not Found" response
    Given operation "GetTagPolicy" enabled
    And new "GetTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Get a tag policy returns "OK" response
    Given operation "GetTagPolicy" enabled
    And new "GetTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List tag policies returns "Bad Request" response
    Given operation "ListTagPolicies" enabled
    And new "ListTagPolicies" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: List tag policies returns "OK" response
    Given operation "ListTagPolicies" enabled
    And new "ListTagPolicies" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a tag policy returns "Bad Request" response
    Given operation "UpdateTagPolicy" enabled
    And new "UpdateTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"policy_type": "surfacing", "tag_value_patterns": []}, "id": "123", "type": "tag_policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a tag policy returns "Not Found" response
    Given operation "UpdateTagPolicy" enabled
    And new "UpdateTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"policy_type": "surfacing", "tag_value_patterns": []}, "id": "123", "type": "tag_policy"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-governance-console
  Scenario: Update a tag policy returns "OK" response
    Given operation "UpdateTagPolicy" enabled
    And new "UpdateTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"policy_type": "surfacing", "tag_value_patterns": []}, "id": "123", "type": "tag_policy"}}
    When the request is sent
    Then the response status is 200 OK
