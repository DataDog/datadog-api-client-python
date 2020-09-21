@endpoint(teams) @v2
Feature: Teams
  Create, update, delete and retrieve your organizations Teams.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Teams" API

  Scenario: Get a list of all teams returns "OK" response
    Given there is a valid "team" in the system
    And operation "GetTeams" enabled
    And new "GetTeams" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new team returns "CREATED" response
    Given operation "CreateTeam" enabled
    And new "CreateTeam" request
    And body {"data": {"type": "teams", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{ unique }}"

  Scenario: Delete an existing team returns "OK" response
    Given there is a valid "team" in the system
    And operation "DeleteTeam" enabled
    And new "DeleteTeam" request
    And request contains "team_id" parameter from "team.data.id"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get details of a team returns "OK" response
    Given there is a valid "team" in the system
    And operation "GetTeam" enabled
    And new "GetTeam" request
    And request contains "team_id" parameter from "team.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "team.data.attributes.name"

  Scenario: Update an existing team returns "OK" response
    Given there is a valid "team" in the system
    And operation "UpdateTeam" enabled
    And new "UpdateTeam" request
    And request contains "team_id" parameter from "team.data.id"
    And body {"data": {"type": "teams", "attributes": {"name": "{{ team.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ team.data.attributes.name }}-updated"
