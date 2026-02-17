@endpoint(team) @endpoint(team-v2) @endpoint(teams) @endpoint(teams-v2)
Feature: Teams
  View and manage teams within Datadog. See the [Teams
  page](https://docs.datadoghq.com/account_management/teams/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Teams" API

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Add a member team returns "API error response." response
    Given operation "AddMemberTeam" enabled
    And new "AddMemberTeam" request
    And request contains "super_team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "member_teams"}}
    When the request is sent
    Then the response status is 409 API error response.

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Add a member team returns "Added" response
    Given operation "AddMemberTeam" enabled
    And new "AddMemberTeam" request
    And request contains "super_team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "member_teams"}}
    When the request is sent
    Then the response status is 204 Added

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Add a user to a team returns "API error response." response
    Given new "CreateTeamMembership" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"role": "admin"}, "relationships": {"team": {"data": {"id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9", "type": "team"}}, "user": {"data": {"id": "b8626d7e-cedd-11eb-abf5-da7ad0900001", "type": "users"}}}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 409 API error response.

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Add a user to a team returns "Represents a user's association to a team" response
    Given new "CreateTeamMembership" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"role": "admin"}, "relationships": {"team": {"data": {"id": "d7e15d9d-d346-43da-81d8-3d9e71d9a5e9", "type": "team"}}, "user": {"data": {"id": "b8626d7e-cedd-11eb-abf5-da7ad0900001", "type": "users"}}}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 200 Represents a user's association to a team

  @team:DataDog/aaa-omg
  Scenario: Create a team hierarchy link returns "Conflict" response
    Given new "AddTeamHierarchyLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "dd_team_2" in the system
    And there is a valid "team_hierarchy_link" in the system
    And body with value {"data": {"relationships": {"parent_team": {"data": {"id": "{{team_hierarchy_link.data.relationships.parent_team.data.id}}", "type": "team"}}, "sub_team": {"data": {"id": "{{team_hierarchy_link.data.relationships.sub_team.data.id}}", "type": "team"}}}, "type": "team_hierarchy_links"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/aaa-omg
  Scenario: Create a team hierarchy link returns "OK" response
    Given new "AddTeamHierarchyLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "dd_team_2" in the system
    And body with value {"data": {"relationships": {"parent_team": {"data": {"id": "{{dd_team.data.id}}", "type": "team"}}, "sub_team": {"data": {"id": "{{dd_team_2.data.id}}", "type": "team"}}}, "type": "team_hierarchy_links"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Create a team link returns "API error response." response
    Given new "CreateTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And body with value {"data": {"attributes": {"label": "", "url": "https://example.com", "position": 0}, "type": "team_links"}}
    When the request is sent
    Then the response status is 422 API error response.

  @team:DataDog/aaa-omg
  Scenario: Create a team link returns "OK" response
    Given new "CreateTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And body with value {"data": {"attributes": {"label": "Link label", "url": "https://example.com", "position": 0}, "type": "team_links"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.label" is equal to "Link label"
    And the response "data.attributes.url" is equal to "https://example.com"
    And the response "data.attributes.position" is equal to 0

  @team:DataDog/aaa-omg
  Scenario: Create a team returns "API error response." response
    Given new "CreateTeam" request
    And there is a valid "dd_team" in the system
    And body with value {"data": {"attributes": {"handle": "{{dd_team.data.attributes.handle}}", "name": "Example Team"}, "relationships": {"users": {"data": []}}, "type": "team"}}
    When the request is sent
    Then the response status is 409 API error response.

  @team:DataDog/aaa-omg
  Scenario: Create a team returns "CREATED" response
    Given new "CreateTeam" request
    And body with value {"data": {"attributes": {"handle": "test-handle-{{ unique_hash }}", "name": "test-name-{{ unique_hash }}"}, "relationships": {"users": {"data": []}}, "type": "team"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data" has field "id"
    And the response "data.attributes.handle" is equal to "test-handle-{{ unique_hash }}"
    And the response "data.attributes.name" is equal to "test-name-{{ unique_hash }}"

  @team:DataDog/aaa-omg
  Scenario: Create a team with V2 fields returns "CREATED" response
    Given new "CreateTeam" request
    And body with value {"data": {"attributes": {"handle": "test-handle-{{ unique_hash }}","name": "test-name-{{ unique_hash }}", "avatar": "🥑", "banner": 7, "visible_modules": ["m1","m2"], "hidden_modules": ["m3"]}, "type": "team"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data" has field "id"
    And the response "data.attributes.handle" is equal to "test-handle-{{ unique_hash }}"
    And the response "data.attributes.name" is equal to "test-name-{{ unique_hash }}"
    And the response "data.attributes.avatar" is equal to "🥑"
    And the response "data.attributes.banner" is equal to 7
    And the response "data.attributes.visible_modules" has length 2
    And the response "data.attributes.visible_modules" array contains value "m1"
    And the response "data.attributes.visible_modules" array contains value "m2"
    And the response "data.attributes.hidden_modules" has length 1
    And the response "data.attributes.hidden_modules" array contains value "m3"

  @skip @team:DataDog/aaa-omg
  Scenario: Create team connections returns "Bad Request" response
    Given operation "CreateTeamConnections" enabled
    And new "CreateTeamConnections" request
    And body with value {"data": [{"attributes": {"source": "github"}, "relationships": {"connected_team": {"data": {"id": "@MyGitHubAccount/my-team-name", "type": "github_team"}}, "team": {"data": {"type": "team"}}}, "type": "team_connection"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Create team connections returns "Conflict" response
    Given new "CreateTeamConnections" request
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

  @team:DataDog/aaa-omg
  Scenario: Create team notification rule returns "API error response." response
    Given new "CreateTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And there is a valid "team_notification_rule" in the system
    And body with value {"data": {"type": "team_notification_rules", "attributes": {"email": {"enabled": true}, "slack": {"workspace": "Datadog", "channel": "aaa-omg-ops"}}}}
    When the request is sent
    Then the response status is 409 API error response.

  @team:DataDog/aaa-omg
  Scenario: Create team notification rule returns "OK" response
    Given new "CreateTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And body with value {"data": {"type": "team_notification_rules", "attributes": {"email": {"enabled": true}, "slack": {"workspace": "Datadog", "channel": "aaa-omg-ops"}}}}
    When the request is sent
    Then the response status is 201 Created

  @skip @team:DataDog/aaa-omg
  Scenario: Delete team connections returns "Bad Request" response
    Given operation "DeleteTeamConnections" enabled
    And new "DeleteTeamConnections" request
    And body with value {"data": [{"type": "team_connection"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete team connections returns "No Content" response
    Given new "DeleteTeamConnections" request
    And body with value {"data": [{"id": "12345678-1234-5678-9abc-123456789012", "type": "team_connection"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Delete team connections returns "Not Found" response
    Given new "DeleteTeamConnections" request
    And body with value {"data": [{"id": "12345678-1234-5678-9abc-123456789012", "type": "team_connection"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aaa-omg
  Scenario: Delete team notification rule returns "API error response." response
    Given new "DeleteTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_notification_rule" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "rule_id" parameter with value "3d031bb2-e1da-4d34-a670-1b5557b032c9"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Delete team notification rule returns "No Content" response
    Given new "DeleteTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_notification_rule" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "rule_id" parameter from "team_notification_rule.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/aaa-omg
  Scenario: Get a team hierarchy link returns "API error response." response
    Given new "GetTeamHierarchyLink" request
    And request contains "link_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get a team hierarchy link returns "OK" response
    Given new "GetTeamHierarchyLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "dd_team_2" in the system
    And there is a valid "team_hierarchy_link" in the system
    And request contains "link_id" parameter from "team_hierarchy_link.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ team_hierarchy_link.data.id }}"
    And the response "data.relationships.parent_team.data.id" is equal to "{{ dd_team.data.id }}"
    And the response "data.relationships.sub_team.data.id" is equal to "{{ dd_team_2.data.id }}"
    And the response "included" has item with field "id" with value "{{ dd_team.data.id }}"
    And the response "included" has item with field "id" with value "{{ dd_team_2.data.id }}"

  @team:DataDog/aaa-omg
  Scenario: Get a team link returns "API error response." response
    Given new "GetTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get a team link returns "OK" response
    Given new "GetTeamLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_link" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter from "team_link.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Get a team returns "API error response." response
    Given new "GetTeam" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get a team returns "OK" response
    Given new "GetTeam" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get all member teams returns "API error response." response
    Given operation "ListMemberTeams" enabled
    And new "ListMemberTeams" request
    And request contains "super_team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get all member teams returns "OK" response
    Given operation "ListMemberTeams" enabled
    And new "ListMemberTeams" request
    And request contains "super_team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg @with-pagination
  Scenario: Get all member teams returns "OK" response with pagination
    Given operation "ListMemberTeams" enabled
    And new "ListMemberTeams" request
    And request contains "super_team_id" parameter from "REPLACE.ME"
    When the request with pagination is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Get all teams returns "OK" response
    Given new "ListTeams" request
    And there is a valid "dd_team" in the system
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ dd_team.data.id }}"

  @replay-only @skip-validation @team:DataDog/aaa-omg @with-pagination
  Scenario: Get all teams returns "OK" response with pagination
    Given new "ListTeams" request
    And request contains "page[size]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/aaa-omg
  Scenario: Get all teams with fields_team parameter returns "OK" response
    Given new "ListTeams" request
    And there is a valid "dd_team" in the system
    And request contains "fields[team]" parameter with value ["id", "name", "handle"]
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0]" has field "id"
    And the response "data[0].attributes" has field "name"
    And the response "data[0].attributes" has field "handle"

  @team:DataDog/aaa-omg
  Scenario: Get links for a team returns "API error response." response
    Given new "GetTeamLinks" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get links for a team returns "OK" response
    Given new "GetTeamLinks" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Get permission settings for a team returns "API error response." response
    Given new "GetTeamPermissionSettings" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get permission settings for a team returns "OK" response
    Given new "GetTeamPermissionSettings" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Get team hierarchy links returns "OK" response
    Given new "ListTeamHierarchyLinks" request
    And there is a valid "dd_team" in the system
    And there is a valid "dd_team_2" in the system
    And there is a valid "team_hierarchy_link" in the system
    And request contains "filter[parent_team]" parameter from "team_hierarchy_link.data.relationships.parent_team.data.id"
    And request contains "filter[sub_team]" parameter from "team_hierarchy_link.data.relationships.sub_team.data.id"
    And request contains "page[number]" parameter with value 0
    And request contains "page[size]" parameter with value 100
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].id" is equal to "{{ team_hierarchy_link.data.id }}"
    And the response "data[0].relationships.parent_team.data.id" is equal to "{{ dd_team.data.id }}"
    And the response "data[0].relationships.sub_team.data.id" is equal to "{{ dd_team_2.data.id }}"
    And the response "included" has item with field "id" with value "{{ dd_team.data.id }}"
    And the response "included" has item with field "id" with value "{{ dd_team_2.data.id }}"

  @generated @skip @team:DataDog/aaa-omg @with-pagination
  Scenario: Get team hierarchy links returns "OK" response with pagination
    Given new "ListTeamHierarchyLinks" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Get team memberships returns "API error response." response
    Given new "GetTeamMemberships" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get team memberships returns "Represents a user's association to a team" response
    Given new "GetTeamMemberships" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 200 Represents a user's association to a team

  @replay-only @skip-validation @team:DataDog/aaa-omg @with-pagination
  Scenario: Get team memberships returns "Represents a user's association to a team" response with pagination
    Given new "GetTeamMemberships" request
    And request contains "team_id" parameter with value "2e06bf2c-193b-41d4-b3c2-afccc080458f"
    And request contains "page[size]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/aaa-omg
  Scenario: Get team notification rule returns "API error response." response
    Given new "GetTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_notification_rule" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "rule_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get team notification rule returns "OK" response
    Given new "GetTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_notification_rule" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "rule_id" parameter from "team_notification_rule.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get team notification rules returns "API error response." response
    Given new "GetTeamNotificationRules" request
    And request contains "team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get team notification rules returns "OK" response
    Given new "GetTeamNotificationRules" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And there is a valid "team_notification_rule" in the system
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get team sync configurations returns "OK" response
    Given new "GetTeamSync" request
    And request contains "filter[source]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get team sync configurations returns "Team sync configurations not found" response
    Given new "GetTeamSync" request
    And request contains "filter[source]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Team sync configurations not found

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Get user memberships returns "API error response." response
    Given new "GetUserMemberships" request
    And request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Get user memberships returns "Represents a user's association to a team" response
    Given new "GetUserMemberships" request
    And there is a valid "user" in the system
    And request contains "user_uuid" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 Represents a user's association to a team
    And the response "data" has length 0

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Link Teams with GitHub Teams returns "OK" response
    Given new "SyncTeams" request
    And body with value {"data": {"attributes": {"source": "github", "type": "link"}, "type": "team_sync_bulk"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg
  Scenario: List team connections returns "Bad Request" response
    Given new "ListTeamConnections" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-omg
  Scenario: List team connections returns "OK" response
    Given new "ListTeamConnections" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-omg @with-pagination
  Scenario: List team connections returns "OK" response with pagination
    Given new "ListTeamConnections" request
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

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Remove a member team returns "API error response." response
    Given operation "RemoveMemberTeam" enabled
    And new "RemoveMemberTeam" request
    And request contains "super_team_id" parameter from "REPLACE.ME"
    And request contains "member_team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Remove a member team returns "No Content" response
    Given operation "RemoveMemberTeam" enabled
    And new "RemoveMemberTeam" request
    And request contains "super_team_id" parameter from "REPLACE.ME"
    And request contains "member_team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/aaa-omg
  Scenario: Remove a team hierarchy link returns "API error response." response
    Given new "RemoveTeamHierarchyLink" request
    And request contains "link_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Remove a team hierarchy link returns "No Content" response
    Given new "RemoveTeamHierarchyLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "dd_team_2" in the system
    And there is a valid "team_hierarchy_link" in the system
    And request contains "link_id" parameter from "team_hierarchy_link.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/aaa-omg
  Scenario: Remove a team link returns "API error response." response
    Given new "DeleteTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Remove a team link returns "No Content" response
    Given new "DeleteTeamLink" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_link" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter from "team_link.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/aaa-omg
  Scenario: Remove a team returns "API error response." response
    Given new "DeleteTeam" request
    And request contains "team_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Remove a team returns "No Content" response
    Given new "DeleteTeam" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/aaa-omg
  Scenario: Remove a user from a team returns "API error response." response
    Given new "DeleteTeamMembership" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @skip @team:DataDog/aaa-omg
  Scenario: Remove a user from a team returns "No Content" response
    Given new "DeleteTeamMembership" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @replay-only @team:DataDog/aaa-omg
  Scenario: Sync teams returns "OK" response
    Given new "SyncTeams" request
    And body with value {"data": {"attributes": {"source": "github", "type": "link"}, "type": "team_sync_bulk"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Update a team link returns "API error response." response
    Given new "UpdateTeamLink" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "link_id" parameter with value "REPLACE.ME"
    And body with value {"data": {"attributes": {"label": "Link label", "url": "https://example.com"}, "type": "team_links"}}
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
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
    And the response "data.attributes.label" is equal to "New Label"
    And the response "data.attributes.url" is equal to "https://example.com"

  @generated @skip @team:DataDog/aaa-omg
  Scenario: Update a team returns "API error response." response
    Given new "UpdateTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"avatar": "\ud83e\udd51", "banner": null, "handle": "example-team", "hidden_modules": [], "name": "Example Team", "visible_modules": []}, "relationships": {"team_links": {"data": [{"id": "f9bb8444-af7f-11ec-ac2c-da7ad0900001", "type": "team_links"}], "links": {"related": "/api/v2/team/c75a4a8e-20c7-11ee-a3a5-da7ad0900002/links"}}}, "type": "team"}}
    When the request is sent
    Then the response status is 409 API error response.

  @team:DataDog/aaa-omg
  Scenario: Update a team returns "OK" response
    Given new "UpdateTeam" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And body with value {"data": {"attributes": {"handle": "{{dd_team.data.attributes.handle}}", "name": "{{dd_team.data.attributes.name}} updated", "avatar": "🥑", "banner": 7, "hidden_modules": ["m3"], "visible_modules": ["m1", "m2"]}, "type": "team"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ dd_team.data.id }}"
    And the response "data.attributes.handle" is equal to "{{dd_team.data.attributes.handle}}"
    And the response "data.attributes.name" is equal to "{{dd_team.data.attributes.name}} updated"
    And the response "data.attributes.avatar" is equal to "🥑"
    And the response "data.attributes.banner" is equal to 7
    And the response "data.attributes.hidden_modules" is equal to ["m3"]
    And the response "data.attributes.visible_modules" is equal to ["m1", "m2"]

  @team:DataDog/aaa-omg
  Scenario: Update a user's membership attributes on a team returns "API error response." response
    Given new "UpdateTeamMembership" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter with value "00000000-0000-dead-beef-000000000000"
    And body with value {"data": {"attributes": {"role": "admin"}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Update a user's membership attributes on a team returns "OK" response
    Given new "UpdateTeamMembership" request
    And there is a valid "dd_team" in the system
    And there is a valid "user" in the system
    And there is a valid "team_membership" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter from "user.data.id"
    And body with value {"data": {"attributes": {"role": "admin"}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.role" is equal to "admin"
    And the response "data.relationships.user.data.id" is equal to "{{ user.data.id }}"

  @team:DataDog/aaa-omg
  Scenario: Update a user's membership attributes on a team with invalid role returns "API error response." response
    Given new "UpdateTeamMembership" request
    And there is a valid "dd_team" in the system
    And there is a valid "user" in the system
    And there is a valid "team_membership" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "user_id" parameter from "user.data.id"
    And body with value {"data": {"attributes": {"role": "member"}, "type": "team_memberships"}}
    When the request is sent
    Then the response status is 400 API error response.

  @team:DataDog/aaa-omg
  Scenario: Update permission setting for team returns "API error response." response
    Given new "UpdateTeamPermissionSetting" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "action" parameter with value "REPLACE.ME"
    And body with value {"data": {"attributes": {"value": "admins"}, "type": "team_permission_settings"}}
    When the request is sent
    Then the response status is 404 API error response.

  @team:DataDog/aaa-omg
  Scenario: Update permission setting for team returns "OK" response
    Given new "UpdateTeamPermissionSetting" request
    And there is a valid "dd_team" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "action" parameter with value "manage_membership"
    And body with value {"data": {"attributes": {"value": "admins"}, "type": "team_permission_settings"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-omg
  Scenario: Update team notification rule returns "API error response." response
    Given new "UpdateTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_notification_rule" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "rule_id" parameter with value "3d031bb2-e1da-4d34-a670-1b5557b032c9"
    And body with value {"data": {"type": "team_notification_rules", "id": "{{dd_team.data.id}}", "attributes": {"pagerduty": {"service_name": "Datadog-prod"}, "slack": {"workspace": "Datadog", "channel": "aaa-governance-ops"}}}}
    When the request is sent
    Then the response status is 409 API error response.

  @team:DataDog/aaa-omg
  Scenario: Update team notification rule returns "OK" response
    Given new "UpdateTeamNotificationRule" request
    And there is a valid "dd_team" in the system
    And there is a valid "team_notification_rule" in the system
    And request contains "team_id" parameter from "dd_team.data.id"
    And request contains "rule_id" parameter from "team_notification_rule.data.id"
    And body with value {"data": {"type": "team_notification_rules", "id": "{{team_notification_rule.data.id}}", "attributes": {"pagerduty": {"service_name": "Datadog-prod"}, "slack": {"workspace": "Datadog", "channel": "aaa-governance-ops"}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.slack.channel" is equal to "aaa-governance-ops"
    And the response "data.attributes.pagerduty.service_name" is equal to "Datadog-prod"
