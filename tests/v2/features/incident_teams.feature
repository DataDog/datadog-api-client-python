@endpoint(incident-teams)
Feature: Incident Teams
  Create, update, delete and retrieve teams which can be associated with
  incidents.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IncidentTeams" API

  Scenario: Get a list of all incident teams returns "OK" response
    Given there is a valid "team" in the system
    And operation "ListIncidentTeams" enabled
    And new "ListIncidentTeams" request
    And request contains "filter" parameter from "team.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.name" has the same value as "team.data.attributes.name"

  Scenario: Create a new incident team returns "CREATED" response
    Given operation "CreateIncidentTeam" enabled
    And new "CreateIncidentTeam" request
    And body {"data": {"type": "teams", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{ unique }}"

  Scenario: Delete an existing incident team returns "OK" response
    Given there is a valid "team" in the system
    And operation "DeleteIncidentTeam" enabled
    And new "DeleteIncidentTeam" request
    And request contains "team_id" parameter from "team.data.id"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get details of an incident team returns "OK" response
    Given there is a valid "team" in the system
    And operation "GetIncidentTeam" enabled
    And new "GetIncidentTeam" request
    And request contains "team_id" parameter from "team.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "team.data.attributes.name"

  Scenario: Update an existing incident team returns "OK" response
    Given there is a valid "team" in the system
    And operation "UpdateIncidentTeam" enabled
    And new "UpdateIncidentTeam" request
    And request contains "team_id" parameter from "team.data.id"
    And body {"data": {"type": "teams", "attributes": {"name": "{{ team.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ team.data.attributes.name }}-updated"
