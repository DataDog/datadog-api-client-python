@endpoint(incident-services)
Feature: Incident Services
  Create, update, delete, and retrieve services which can be associated with
  incidents.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IncidentServices" API

  Scenario: Get a list of all incident services returns "OK" response
    Given there is a valid "service" in the system
    And operation "GetIncidentServices" enabled
    And new "GetIncidentServices" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new incident service returns "CREATED" response
    Given operation "CreateIncidentService" enabled
    And new "CreateIncidentService" request
    And body {"data": {"type": "services", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{ unique }}"

  Scenario: Delete an existing incident service returns "OK" response
    Given there is a valid "service" in the system
    And operation "DeleteIncidentService" enabled
    And new "DeleteIncidentService" request
    And request contains "service_id" parameter from "service.data.id"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get details of an incident service returns "OK" response
    Given there is a valid "service" in the system
    And operation "GetIncidentService" enabled
    And new "GetIncidentService" request
    And request contains "service_id" parameter from "service.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "service.data.attributes.name"

  Scenario: Update an existing incident service returns "OK" response
    Given there is a valid "service" in the system
    And operation "UpdateIncidentService" enabled
    And new "UpdateIncidentService" request
    And request contains "service_id" parameter from "service.data.id"
    And body {"data": {"type": "services", "attributes": {"name": "{{ service.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ service.data.attributes.name }}-updated"
