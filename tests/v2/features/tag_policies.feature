@endpoint(tag-policies) @endpoint(tag-policies-v2)
Feature: Tag Policies
  Manage tag policies to enforce tagging standards across your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TagPolicies" API

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Create a tag policy returns "Bad Request" response
    Given operation "CreateTagPolicy" enabled
    And new "CreateTagPolicy" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "production-tags-policy", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Create a tag policy returns "Created" response
    Given operation "CreateTagPolicy" enabled
    And new "CreateTagPolicy" request
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "production-tags-policy", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete a tag policy returns "Bad Request" response
    Given operation "DeleteTagPolicy" enabled
    And new "DeleteTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete a tag policy returns "No Content" response
    Given operation "DeleteTagPolicy" enabled
    And new "DeleteTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete a tag policy returns "Not Found" response
    Given operation "DeleteTagPolicy" enabled
    And new "DeleteTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get a tag policy returns "Bad Request" response
    Given operation "GetTagPolicy" enabled
    And new "GetTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get a tag policy returns "Not Found" response
    Given operation "GetTagPolicy" enabled
    And new "GetTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get a tag policy returns "OK" response
    Given operation "GetTagPolicy" enabled
    And new "GetTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get tag policy score returns "Bad Request" response
    Given operation "GetTagPolicyScore" enabled
    And new "GetTagPolicyScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get tag policy score returns "Not Found" response
    Given operation "GetTagPolicyScore" enabled
    And new "GetTagPolicyScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get tag policy score returns "OK" response
    Given operation "GetTagPolicyScore" enabled
    And new "GetTagPolicyScore" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: List tag policies returns "Bad Request" response
    Given operation "ListTagPolicies" enabled
    And new "ListTagPolicies" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: List tag policies returns "OK" response
    Given operation "ListTagPolicies" enabled
    And new "ListTagPolicies" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update a tag policy returns "Bad Request" response
    Given operation "UpdateTagPolicy" enabled
    And new "UpdateTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "production-tags-policy", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update a tag policy returns "Not Found" response
    Given operation "UpdateTagPolicy" enabled
    And new "UpdateTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "production-tags-policy", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update a tag policy returns "OK" response
    Given operation "UpdateTagPolicy" enabled
    And new "UpdateTagPolicy" request
    And request contains "policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "negated": false, "policy_name": "production-tags-policy", "required": true, "scope": "env", "source": "logs", "tag_key": "service", "tag_value_patterns": ["api", "web"]}, "type": "tag_policy"}}
    When the request is sent
    Then the response status is 200 OK
