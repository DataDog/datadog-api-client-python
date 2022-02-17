@endpoint(incident-teams) @endpoint(incident-teams-v2)
Feature: Incident Teams
  Create, update, delete and retrieve teams which can be associated with
  incidents.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IncidentTeams" API

  @generated @skip @team:Datadog/incident-app
  Scenario: Create a new incident team returns "Bad Request" response
    Given operation "CreateIncidentTeam" enabled
    And new "CreateIncidentTeam" request
    And body with value {"data": {"attributes": {"name": "team name"}, "type": "teams"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/incident-app
  Scenario: Create a new incident team returns "CREATED" response
    Given operation "CreateIncidentTeam" enabled
    And new "CreateIncidentTeam" request
    And body with value {"data": {"type": "teams", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:Datadog/incident-app
  Scenario: Create a new incident team returns "Not Found" response
    Given operation "CreateIncidentTeam" enabled
    And new "CreateIncidentTeam" request
    And body with value {"data": {"attributes": {"name": "team name"}, "type": "teams"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an existing incident team returns "Bad Request" response
    Given operation "DeleteIncidentTeam" enabled
    And new "DeleteIncidentTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an existing incident team returns "Not Found" response
    Given operation "DeleteIncidentTeam" enabled
    And new "DeleteIncidentTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Delete an existing incident team returns "OK" response
    Given there is a valid "team" in the system
    And operation "DeleteIncidentTeam" enabled
    And new "DeleteIncidentTeam" request
    And request contains "team_id" parameter from "team.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of all incident teams returns "Bad Request" response
    Given operation "ListIncidentTeams" enabled
    And new "ListIncidentTeams" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of all incident teams returns "Not Found" response
    Given operation "ListIncidentTeams" enabled
    And new "ListIncidentTeams" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Get a list of all incident teams returns "OK" response
    Given there is a valid "team" in the system
    And operation "ListIncidentTeams" enabled
    And new "ListIncidentTeams" request
    And request contains "filter" parameter from "team.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.name" has the same value as "team.data.attributes.name"

  @generated @skip @team:Datadog/incident-app
  Scenario: Get details of an incident team returns "Bad Request" response
    Given operation "GetIncidentTeam" enabled
    And new "GetIncidentTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get details of an incident team returns "Not Found" response
    Given operation "GetIncidentTeam" enabled
    And new "GetIncidentTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Get details of an incident team returns "OK" response
    Given there is a valid "team" in the system
    And operation "GetIncidentTeam" enabled
    And new "GetIncidentTeam" request
    And request contains "team_id" parameter from "team.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "team.data.attributes.name"

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an existing incident team returns "Bad Request" response
    Given operation "UpdateIncidentTeam" enabled
    And new "UpdateIncidentTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "team name"}, "id": "00000000-7ea3-0000-0001-000000000000", "type": "teams"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an existing incident team returns "Not Found" response
    Given operation "UpdateIncidentTeam" enabled
    And new "UpdateIncidentTeam" request
    And request contains "team_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "team name"}, "id": "00000000-7ea3-0000-0001-000000000000", "type": "teams"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Update an existing incident team returns "OK" response
    Given there is a valid "team" in the system
    And operation "UpdateIncidentTeam" enabled
    And new "UpdateIncidentTeam" request
    And request contains "team_id" parameter from "team.data.id"
    And body with value {"data": {"type": "teams", "attributes": {"name": "{{ team.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ team.data.attributes.name }}-updated"
