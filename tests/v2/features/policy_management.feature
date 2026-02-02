@endpoint(policy-management) @endpoint(policy-management-v2)
Feature: Policy Management
  Manage and evaluate organizational policies.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "PolicyManagement" API
    And operation "EvaluatePolicyResult" enabled
    And new "EvaluatePolicyResult" request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Evaluate policy result returns "Bad Request" response
    Given request contains "policy_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Evaluate policy result returns "Not Found" response
    Given request contains "policy_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Evaluate policy result returns "OK" response
    Given request contains "policy_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
