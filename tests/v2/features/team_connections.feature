@endpoint(team-connections) @endpoint(team-connections-v2)
Feature: Team Connections
  View and manage relationships between Datadog teams and teams from
  external sources, such as GitHub.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TeamConnections" API

  @skip @team:DataDog/aaa-omg
  Scenario: Create team connections returns "Bad Request" response
    Given operation "CreateTeamConnections" enabled
    And new "CreateTeamConnections" request
    And body with value {"data": [{"attributes": {"source": "github"}, "relationships": {"connected_team": {"data": {"id": "@MyGitHubAccount/my-team-name", "type": "github_team"}}, "team": {"data": {"type": "team"}}}, "type": "team_connection"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Create team connections returns "Conflict" response
    Given operation "CreateTeamConnections" enabled
    And new "CreateTeamConnections" request
    And body with value {"data": [{"attributes": {"managed_by": "github_sync", "source": "github"}, "relationships": {"connected_team": {"data": {"id": "@GitHubOrg/team-handle", "type": "github_team"}}, "team": {"data": {"id": "87654321-4321-8765-dcba-210987654321", "type": "team"}}}, "type": "team_connection"}]}
    When the request is sent
    Then the response status is 409 Conflict

  @skip @team:DataDog/aaa-omg
  Scenario: Create team connections returns "Created" response
    Given operation "CreateTeamConnections" enabled
    And new "CreateTeamConnections" request
    And there is a valid "dd_team" in the system
    And body with value {"data": [{"type": "team_connection", "attributes": {"source": "github", "managed_by": "datadog"}, "relationships": {"team": {"data": {"id": "{{ dd_team.data.id }}", "type": "team"}}, "connected_team": {"data": {"id": "@MyGitHubAccount/my-team-name", "type": "github_team"}}}}]}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.data[0].attributes.source" is equal to "github"
    And the response "data.data[0].attributes.managed_by" is equal to "datadog"
    And the response "data.data[0].relationships.team.data.id" is equal to "{{ dd_team.data.id }}"
    And the response "data.data[0].relationships.connected_team.data.id" is equal to "@MyGitHubAccount/my-team-name"
    And the response "data.data[0].type" is equal to "team_connection"

  @skip @team:DataDog/aaa-omg
  Scenario: Delete team connections returns "Bad Request" response
    Given operation "DeleteTeamConnections" enabled
    And new "DeleteTeamConnections" request
    And body with value {"data": [{"type": "team_connection"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete team connections returns "No Content" response
    Given operation "DeleteTeamConnections" enabled
    And new "DeleteTeamConnections" request
    And body with value {"data": [{"id": "12345678-1234-5678-9abc-123456789012", "type": "team_connection"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete team connections returns "Not Found" response
    Given operation "DeleteTeamConnections" enabled
    And new "DeleteTeamConnections" request
    And body with value {"data": [{"id": "12345678-1234-5678-9abc-123456789012", "type": "team_connection"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: List team connections returns "Bad Request" response
    Given operation "ListTeamConnections" enabled
    And new "ListTeamConnections" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/aaa-omg
  Scenario: List team connections returns "OK" response
    Given operation "ListTeamConnections" enabled
    And new "ListTeamConnections" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg @with-pagination
  Scenario: List team connections returns "OK" response with pagination
    Given operation "ListTeamConnections" enabled
    And new "ListTeamConnections" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @skip @team:DataDog/aaa-omg
  Scenario: List team connections with filters returns "OK" response
    Given operation "ListTeamConnections" enabled
    And new "ListTeamConnections" request
    And request contains "filter[sources]" parameter with value ["github"]
    And request contains "page[size]" parameter with value 10
    When the request is sent
    Then the response status is 200 OK
