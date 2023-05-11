@endpoint(team) @endpoint(team-v2) @endpoint(teams) @endpoint(teams-v2)
Feature: Teams
  View and manage teams within Datadog.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Teams" API

  @generated @skip @team:DataDog/core-app
  Scenario: Add a user to a team returns "API error response." response
    Given new "CreateTeamMembership" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"role": "admin"}, "relationships": {"user": {"data": {"id": "b8626d7e-cedd-11eb-abf5-da7ad0900001", "type": "users"}}}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 409 API error response.

  @generated @skip @team:DataDog/core-app
  Scenario: Add a user to a team returns "Represents a user's association to a team" response
    Given new "CreateTeamMembership" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"role": "admin"}, "relationships": {"user": {"data": {"id": "b8626d7e-cedd-11eb-abf5-da7ad0900001", "type": "users"}}}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 200 Represents a user's association to a team

  @team:DataDog/core-app
  Scenario: Create a team link returns "API error response." response
    Given new "CreateTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And body with value {"data": {"attributes": {"label": "", "url": "https://example.com", "position": 0}, "type": "team_links"}}
    When the request is sent
    Then the response status is 422 API error response.

  @team:DataDog/core-app
  Scenario: Create a team link returns "OK" response
    Given new "CreateTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And body with value {"data": {"attributes": {"label": "Link label", "url": "https://example.com", "position": 0}, "type": "team_links"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/core-app
  Scenario: Create a team returns "API error response." response
    Given new "CreateTeam" request
    And there is a valid "dd_team" in the system
    And body with value {"data": {"attributes": {"handle": "{{dd_team.data.attributes.handle}}", "name": "Example Team"}, "relationships": {"users": {"data": []}}, "type": "team"}}
    When the request is sent
    Then the response status is 409 API error response.

  @team:DataDog/core-app
  Scenario: Create a team returns "CREATED" response
    Given new "CreateTeam" request
    And body with value {"data": {"attributes": {"handle": "handle-{{ unique_hash }}", "name": "name-{{ unique_hash }}"}, "relationships": {"users": {"data": []}}, "type": "team"}}
    When the request is sent
    Then the response status is 201 CREATED

  @team:DataDog/core-app
  Scenario: Get a team link returns "API error response." response
    Given new "GetTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Get a team link returns "OK" response
    Given new "GetTeamLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_link" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter from "team_link.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/core-app
  Scenario: Get a team returns "API error response." response
    Given new "GetTeam" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Get a team returns "OK" response
    Given new "GetTeam" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/core-app
  Scenario: Get all teams returns "OK" response
    Given new "ListTeams" request
    And there is a valid "dd_team" in the system
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ dd_team.data.id }}"

  @team:DataDog/core-app
  Scenario: Get links for a team returns "API error response." response
    Given new "GetTeamLinks" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Get links for a team returns "OK" response
    Given new "GetTeamLinks" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/core-app
  Scenario: Get permission settings for a team returns "API error response." response
    Given new "GetTeamPermissionSettings" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Get permission settings for a team returns "OK" response
    Given new "GetTeamPermissionSettings" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/core-app
  Scenario: Get team memberships returns "API error response." response
    Given new "GetTeamMemberships" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Get team memberships returns "Represents a user's association to a team" response
    Given new "GetTeamMemberships" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 Represents a user's association to a team

  @team:DataDog/core-app
  Scenario: Remove a team link returns "API error response." response
    Given new "DeleteTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Remove a team link returns "No Content" response
    Given new "DeleteTeamLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_link" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter from "team_link.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/core-app
  Scenario: Remove a team returns "API error response." response
    Given new "DeleteTeam" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Remove a team returns "No Content" response
    Given new "DeleteTeam" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/core-app
  Scenario: Remove a user from a team returns "API error response." response
    Given new "DeleteTeamMembership" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @skip @team:DataDog/core-app
  Scenario: Remove a user from a team returns "No Content" response
    Given new "DeleteTeamMembership" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/core-app
  Scenario: Update a team link returns "API error response." response
    Given new "UpdateTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter with value "REPLACE.ME"
    And body with value {"data": {"attributes": {"label": "Link label", "url": "https://example.com"}, "type": "team_links"}}
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Update a team link returns "OK" response
    Given new "UpdateTeamLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_link" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter from "team_link.data.id"
    And body with value {"data": {"attributes": {"label": "New Label", "url": "https://example.com"}, "type": "team_links"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ team_link.data.id }}"
    And the response "data.attributes.team_id" is equal to "{{ dd_team.data.id }}"

  @generated @skip @team:DataDog/core-app
  Scenario: Update a team returns "API error response." response
    Given new "UpdateTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"handle": "example-team", "name": "Example Team"}, "relationships": {"team_links": {"data": [{"id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001", "type": "team_links"}]}}, "type": "team"}}
    When the request is sent
    Then the response status is 409 API error response.

  @team:DataDog/core-app
  Scenario: Update a team returns "OK" response
    Given new "UpdateTeam" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And body with value {"data": {"attributes": {"handle": "{{dd_team.data.attributes.handle}}", "name": "{{dd_team.data.attributes.name}} updated"}, "type": "team"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ dd_team.data.id }}"

  @generated @skip @team:DataDog/core-app
  Scenario: Update a user's membership attributes on a team returns "API error response." response
    Given new "UpdateTeamMembership" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And request contains "user_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"role": "admin"}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 404 API error response.

  @generated @skip @team:DataDog/core-app
  Scenario: Update a user's membership attributes on a team returns "Represents a user's association to a team" response
    Given new "UpdateTeamMembership" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And request contains "user_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"role": "admin"}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 200 Represents a user's association to a team

  @team:DataDog/core-app
  Scenario: Update a user's role on a team returns "API error response." response
    Given new "UpdateTeamMembership" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter with value "REPLACE.ME"
    And body with value {"data": {"attributes": {"role": "admin"}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Update permission setting for team returns "API error response." response
    Given new "UpdateTeamPermissionSetting" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "action" parameter with value "REPLACE.ME"
    And body with value {"data": {"attributes": {"value": "admins"}, "type": "team_permission_settings"}}
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/core-app
  Scenario: Update permission setting for team returns "OK" response
    Given new "UpdateTeamPermissionSetting" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "action" parameter with value "manage_membership"
    And body with value {"data": {"attributes": {"value": "admins"}, "type": "team_permission_settings"}}
    When the request is sent
    Then the response status is 200 OK
