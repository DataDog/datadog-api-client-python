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

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/logs-app
  Scenario: Create a restriction query returns "Bad Request" response
    Given operation "CreateRestrictionQuery" enabled
    And new "CreateRestrictionQuery" request
    And body with value {"test": "bad_request"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app
  Scenario: Create a restriction query returns "OK" response
    Given operation "CreateRestrictionQuery" enabled
    And new "CreateRestrictionQuery" request
    And body with value {"data": {"attributes": {"restriction_query": "env:sandbox"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Delete a restriction query returns "Bad Request" response
    Given operation "DeleteRestrictionQuery" enabled
    And new "DeleteRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Delete a restriction query returns "Not found" response
    Given operation "DeleteRestrictionQuery" enabled
    And new "DeleteRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-app
  Scenario: Delete a restriction query returns "OK" response
    Given operation "DeleteRestrictionQuery" enabled
    And there is a valid "restriction_query" in the system
    And new "DeleteRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    When the request is sent
    Then the response status is 204 OK

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Get a restriction query returns "Bad Request" response
    Given operation "GetRestrictionQuery" enabled
    And new "GetRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Get a restriction query returns "Not found" response
    Given operation "GetRestrictionQuery" enabled
    And new "GetRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-app
  Scenario: Get a restriction query returns "OK" response
    Given operation "GetRestrictionQuery" enabled
    And there is a valid "restriction_query" in the system
    And new "GetRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Get all restriction queries for a given user returns "Bad Request" response
    Given operation "ListUserRestrictionQueries" enabled
    And new "ListUserRestrictionQueries" request
    And request contains "user_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app
  Scenario: Get all restriction queries for a given user returns "Not found" response
    Given operation "ListUserRestrictionQueries" enabled
    And new "ListUserRestrictionQueries" request
    And request contains "user_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/logs-app
  Scenario: Get all restriction queries for a given user returns "OK" response
    Given operation "ListUserRestrictionQueries" enabled
    And there is a valid "user" in the system
    And new "ListUserRestrictionQueries" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Get restriction query for a given role returns "Bad Request" response
    Given operation "GetRoleRestrictionQuery" enabled
    And new "GetRoleRestrictionQuery" request
    And request contains "role_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app
  Scenario: Get restriction query for a given role returns "Not found" response
    Given operation "GetRoleRestrictionQuery" enabled
    And new "GetRoleRestrictionQuery" request
    And request contains "role_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app
  Scenario: Get restriction query for a given role returns "OK" response
    Given operation "GetRoleRestrictionQuery" enabled
    And there is a valid "role" in the system
    And new "GetRoleRestrictionQuery" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Grant role to a restriction query returns "Bad Request" response
    Given operation "AddRoleToRestrictionQuery" enabled
    And new "AddRoleToRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "malformed_id"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: Grant role to a restriction query returns "Not found" response
    Given operation "AddRoleToRestrictionQuery" enabled
    And new "AddRoleToRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-app
  Scenario: Grant role to a restriction query returns "OK" response
    Given operation "AddRoleToRestrictionQuery" enabled
    And there is a valid "restriction_query" in the system
    And there is a valid "role" in the system
    And new "AddRoleToRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"id": "{{ role.data.id }}", "type": "roles"}}
    When the request is sent
    Then the response status is 204 OK

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: List restriction queries returns "OK" response
    Given operation "ListRestrictionQueries" enabled
    And new "ListRestrictionQueries" request
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: List roles for a restriction query returns "Bad Request" response
    Given operation "ListRestrictionQueryRoles" enabled
    And new "ListRestrictionQueryRoles" request
    And request contains "restriction_query_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/logs-app
  Scenario: List roles for a restriction query returns "Not found" response
    Given operation "ListRestrictionQueryRoles" enabled
    And new "ListRestrictionQueryRoles" request
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-app
  Scenario: List roles for a restriction query returns "OK" response
    Given operation "ListRestrictionQueryRoles" enabled
    And there is a valid "restriction_query" in the system
    And new "ListRestrictionQueryRoles" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/logs-app
  Scenario: Replace a restriction query returns "Bad Request" response
    Given operation "ReplaceRestrictionQuery" enabled
    And new "ReplaceRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "malformed_id"
    And body with value {"data": {"attributes": {"restriction_query": "env:sandbox"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/logs-app
  Scenario: Replace a restriction query returns "Not found" response
    Given operation "ReplaceRestrictionQuery" enabled
    And new "ReplaceRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"attributes": {"restriction_query": "env:sandbox"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 404 Not found

  @skip @team:DataDog/logs-app
  Scenario: Replace a restriction query returns "OK" response
    Given operation "ReplaceRestrictionQuery" enabled
    And there is a valid "restriction_query" in the system
    And new "ReplaceRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"attributes": {"restriction_query": "env:staging"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @skip-terraform-config @team:DataDog/logs-app
  Scenario: Revoke role from a restriction query returns "Bad Request" response
    Given operation "RemoveRoleFromRestrictionQuery" enabled
    And new "RemoveRoleFromRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "malformed_id"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/logs-app
  Scenario: Revoke role from a restriction query returns "Not found" response
    Given operation "RemoveRoleFromRestrictionQuery" enabled
    And new "RemoveRoleFromRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @skip @team:DataDog/logs-app
  Scenario: Revoke role from a restriction query returns "OK" response
    Given operation "RemoveRoleFromRestrictionQuery" enabled
    And there is a valid "restriction_query" in the system
    And there is a valid "role" in the system
    And new "RemoveRoleFromRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"id": "{{ role.data.id }}", "type": "roles"}}
    When the request is sent
    Then the response status is 204 OK

  @skip @skip-terraform-config @team:DataDog/logs-app
  Scenario: Update a restriction query returns "Bad Request" response
    Given operation "UpdateRestrictionQuery" enabled
    And new "UpdateRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "malformed_id"
    And body with value {"data": {"attributes": {"restriction_query": "env:sandbox"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/logs-app
  Scenario: Update a restriction query returns "Not found" response
    Given operation "UpdateRestrictionQuery" enabled
    And new "UpdateRestrictionQuery" request
    And request contains "restriction_query_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"attributes": {"restriction_query": "env:sandbox"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 404 Not found

  @skip @team:DataDog/logs-app
  Scenario: Update a restriction query returns "OK" response
    Given operation "UpdateRestrictionQuery" enabled
    And there is a valid "restriction_query" in the system
    And new "UpdateRestrictionQuery" request
    And request contains "restriction_query_id" parameter from "restriction_query.data.id"
    And body with value {"data": {"attributes": {"restriction_query": "env:production"}, "type": "logs_restriction_queries"}}
    When the request is sent
    Then the response status is 200 OK
