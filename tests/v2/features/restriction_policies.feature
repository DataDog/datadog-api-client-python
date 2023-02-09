@endpoint(restriction-policies) @endpoint(restriction-policies-v2)
Feature: Restriction Policies
  A restriction policy defines the access control rules for a resource,
  mapping a set of relations (such as editor and viewer) to a set of allowed
  principals (such as roles). The restriction policy determines who is
  authorized to perform what actions on the resource.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RestrictionPolicies" API
    And new "GetRestrictionPolicy" request

  @team:DataDog/aaa-granular-access
  Scenario: Get a restriction policy returns "Bad Request" response
    Given request contains "resource_id" parameter with value "malformed"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-granular-access
  Scenario: Get a restriction policy returns "OK" response
    Given request contains "resource_id" parameter with value "dashboard:abc-def-ghi"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "restriction_policy"
    And the response "data.id" is equal to "dashboard:abc-def-ghi"
    And the response "data.attributes.bindings" has length 0
