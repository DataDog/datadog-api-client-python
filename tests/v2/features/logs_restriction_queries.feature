@endpoint(logs-restriction-queries) @endpoint(logs-restriction-queries-v2)
Feature: Logs Restriction Queries
  **Note: This endpoint is in public beta. If you have any feedback, contact
  [Datadog support](https://docs.datadoghq.com/help/).**  A Restriction
  Query is a logs query that restricts which logs the `logs_read_data`
  permission grants read access to. For users whose roles have Restriction
  Queries, any log query they make only returns those log events that also
  match one of their Restriction Queries. This is true whether the user
  queries log events from any log-related feature, including the log
  explorer, Live Tail, re-hydration, or a dashboard widget.  Restriction
  Queries currently only support use of the following components of log
  events:  - Reserved attributes - The log message - Tags  To restrict read
  access on log data, add a team tag to log events to indicate which teams
  own them, and then scope Restriction Queries to the relevant values of the
  team tag. Tags can be applied to log events in many ways, and a log event
  can have multiple tags with the same key (like team) and different values.
  This means the same log event can be visible to roles whose restriction
  queries are scoped to different team values.  See [How to Set Up RBAC for
  Logs](https://docs.datadoghq.com/logs/guide/logs-rbac/?tab=api#restrict-
  access-to-logs) for details on how to add restriction queries.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsRestrictionQueries" API

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/aaa-granular-access
  Scenario: Create a restriction query returns "Bad Request" response
    Given new "CreateRestrictionQuery" request
    And operation "CreateRestrictionQuery" enabled
    And body with value {"test": "bad_request"}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Create a restriction query returns "OK" response
    Given new "CreateRestrictionQuery" request
    And operation "CreateRestrictionQuery" enabled
    And body with value {"data": {"type": "logs_restriction_queries", "attributes": {"restriction_query": "env:sandbox"}}}
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Delete a restriction query returns "Bad Request" response
    Given new "DeleteRestrictionQuery" request
    And operation "DeleteRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Delete a restriction query returns "No Content" response
    Given there is a valid "restriction_query" in the system
    And operation "DeleteRestrictionQuery" enabled
    And new "DeleteRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Delete a restriction query returns "Not Found" response
    Given new "DeleteRestrictionQuery" request
    And operation "DeleteRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a restriction query returns "Not found" response
    Given operation "DeleteRestrictionQuery" enabled
    And new "DeleteRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a restriction query returns "OK" response
    Given operation "DeleteRestrictionQuery" enabled
    And new "DeleteRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get a restriction query returns "Bad Request" response
    Given new "GetRestrictionQuery" request
    And operation "GetRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get a restriction query returns "Not Found" response
    Given new "GetRestrictionQuery" request
    And operation "GetRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get a restriction query returns "Not found" response
    Given operation "GetRestrictionQuery" enabled
    And new "GetRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get a restriction query returns "OK" response
    Given there is a valid "restriction_query" in the system
    And operation "GetRestrictionQuery" enabled
    And new "GetRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ restriction_query.data.id }}"
    And the response "data.type" is equal to "logs_restriction_queries"

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get all restriction queries for a given user returns "Bad Request" response
    Given new "ListUserRestrictionQueries" request
    And operation "ListUserRestrictionQueries" enabled
    And request contains "user_id" parameter with value "invalid-user-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get all restriction queries for a given user returns "OK" response
    Given there is a valid "user" in the system
    And operation "ListUserRestrictionQueries" enabled
    And new "ListUserRestrictionQueries" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get restriction query for a given role returns "Bad Request" response
    Given new "GetRoleRestrictionQuery" request
    And operation "GetRoleRestrictionQuery" enabled
    And request contains "role_id" parameter with value "invalid-role-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get restriction query for a given role returns "OK" response
    Given there is a valid "role" in the system
    And operation "GetRoleRestrictionQuery" enabled
    And new "GetRoleRestrictionQuery" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Grant role to a restriction query returns "Bad Request" response
    Given there is a valid "restriction_query" in the system
    And new "AddRoleToRestrictionQuery" request
    And operation "AddRoleToRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"type": "roles", "id": "invalid-role-id"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Grant role to a restriction query returns "No Content" response
    Given there is a valid "restriction_query" in the system
    And there is a valid "role" in the system
    And operation "AddRoleToRestrictionQuery" enabled
    And new "AddRoleToRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"type": "{{ role.data.type }}", "id": "{{ role.data.id }}"}}
    When the request is sent
    Then the response status is 204 No Content

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Grant role to a restriction query returns "Not Found" response
    Given new "AddRoleToRestrictionQuery" request
    And operation "AddRoleToRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "roles", "id": "00000000-0000-0000-0000-000000000001"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Grant role to a restriction query returns "Not found" response
    Given operation "AddRoleToRestrictionQuery" enabled
    And new "AddRoleToRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Grant role to a restriction query returns "OK" response
    Given operation "AddRoleToRestrictionQuery" enabled
    And new "AddRoleToRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 204 OK

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: List restriction queries returns "OK" response
    Given there is a valid "restriction_query" in the system
    And operation "ListRestrictionQueries" enabled
    And new "ListRestrictionQueries" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: List roles for a restriction query returns "Bad Request" response
    Given operation "ListRestrictionQueryRoles" enabled
    And new "ListRestrictionQueryRoles" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: List roles for a restriction query returns "Not Found" response
    Given new "ListRestrictionQueryRoles" request
    And operation "ListRestrictionQueryRoles" enabled
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: List roles for a restriction query returns "Not found" response
    Given operation "ListRestrictionQueryRoles" enabled
    And new "ListRestrictionQueryRoles" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: List roles for a restriction query returns "OK" response
    Given there is a valid "restriction_query" in the system
    And operation "ListRestrictionQueryRoles" enabled
    And new "ListRestrictionQueryRoles" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Revoke role from a restriction query returns "Bad Request" response
    Given operation "RemoveRoleFromRestrictionQuery" enabled
    And new "RemoveRoleFromRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Revoke role from a restriction query returns "No Content" response
    Given there is a valid "restriction_query" in the system
    And there is a valid "role" in the system
    And operation "AddRoleToRestrictionQuery" enabled
    And new "AddRoleToRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"type": "{{ role.data.type }}", "id": "{{ role.data.id }}"}}
    And operation "RemoveRoleFromRestrictionQuery" enabled
    And new "RemoveRoleFromRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"type": "{{ role.data.type }}", "id": "{{ role.data.id }}"}}
    When the request is sent
    And the request is sent
    Then the response status is 204 No Content
    And the response status is 204 No Content

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Revoke role from a restriction query returns "Not Found" response
    Given new "RemoveRoleFromRestrictionQuery" request
    And operation "RemoveRoleFromRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "roles", "id": "00000000-0000-0000-0000-000000000001"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Revoke role from a restriction query returns "Not found" response
    Given operation "RemoveRoleFromRestrictionQuery" enabled
    And new "RemoveRoleFromRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Revoke role from a restriction query returns "OK" response
    Given operation "RemoveRoleFromRestrictionQuery" enabled
    And new "RemoveRoleFromRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 204 OK

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Update a restriction query returns "Bad Request" response
    Given new "UpdateRestrictionQuery" request
    And operation "UpdateRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Update a restriction query returns "Not Found" response
    Given new "UpdateRestrictionQuery" request
    And operation "UpdateRestrictionQuery" enabled
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "logs_restriction_queries", "attributes": {"restriction_query": "env:production"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Update a restriction query returns "Not found" response
    Given operation "UpdateRestrictionQuery" enabled
    And new "UpdateRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"restriction_query": "env:sandbox"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 404 Not found

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Update a restriction query returns "OK" response
    Given there is a valid "restriction_query" in the system
    And operation "UpdateRestrictionQuery" enabled
    And new "UpdateRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"type": "logs_restriction_queries", "attributes": {"restriction_query": "env:production"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ restriction_query.data.id }}"
    And the response "data.attributes.restriction_query" is equal to "env:production"
