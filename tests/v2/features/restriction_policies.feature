@endpoint(restriction-policies) @endpoint(restriction-policies-v2)
Feature: Restriction Policies
  A restriction policy defines the access control rules for a resource,
  mapping a set of relations (such as editor and viewer) to a set of allowed
  principals (such as roles, teams, or users). The restriction policy
  determines who is authorized to perform what actions on the resource.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RestrictionPolicies" API

  @team:DataDog/aaa-granular-access
  Scenario: Delete a restriction policy returns "Bad Request" response
    Given new "DeleteRestrictionPolicy" request
    And request contains "resource_id" parameter with value "malformed"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-granular-access
  Scenario: Delete a restriction policy returns "No Content" response
    Given new "DeleteRestrictionPolicy" request
    And request contains "resource_id" parameter with value "dashboard:test-delete"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/aaa-granular-access
  Scenario: Get a restriction policy returns "Bad Request" response
    Given new "GetRestrictionPolicy" request
    And request contains "resource_id" parameter with value "malformed"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-granular-access
  Scenario: Get a restriction policy returns "OK" response
    Given new "GetRestrictionPolicy" request
    And request contains "resource_id" parameter with value "dashboard:test-get"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "restriction_policy"
    And the response "data.id" is equal to "dashboard:test-get"
    And the response "data.attributes.bindings" has length 0

  @team:DataDog/aaa-granular-access
  Scenario: Update a restriction policy returns "Bad Request" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And the "user" has the "role"
    And new "UpdateRestrictionPolicy" request
    And request contains "resource_id" parameter with value "malformed"
    And body with value {"data": {"id": "dashboard:abc-def-ghi", "type": "restriction_policy", "attributes": {"bindings": [{"relation": "editor", "principals": ["org:{{ user.data.relationships.org.data.id }}"]}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-granular-access
  Scenario: Update a restriction policy returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And the "user" has the "role"
    And new "UpdateRestrictionPolicy" request
    And request contains "resource_id" parameter with value "dashboard:test-update"
    And body with value {"data": {"id": "dashboard:test-update", "type": "restriction_policy", "attributes": {"bindings": [{"relation": "editor", "principals": ["org:{{ user.data.relationships.org.data.id }}"]}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "restriction_policy"
    And the response "data.id" is equal to "dashboard:test-update"
    And the response "data.attributes.bindings[0]" is equal to {"relation": "editor", "principals": ["org:{{ user.data.relationships.org.data.id }}"]}
