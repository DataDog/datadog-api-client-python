@endpoint(incident-services) @endpoint(incident-services-v2)
Feature: Incident Services
  Create, update, delete, and retrieve services which can be associated with
  incidents.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IncidentServices" API

  @generated @skip @team:Datadog/incident-app
  Scenario: Create a new incident service returns "Bad Request" response
    Given operation "CreateIncidentService" enabled
    And new "CreateIncidentService" request
    And body with value {"data": {"attributes": {"name": "an example service name"}, "type": "services"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/incident-app
  Scenario: Create a new incident service returns "CREATED" response
    Given operation "CreateIncidentService" enabled
    And new "CreateIncidentService" request
    And body with value {"data": {"type": "services", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:Datadog/incident-app
  Scenario: Create a new incident service returns "Not Found" response
    Given operation "CreateIncidentService" enabled
    And new "CreateIncidentService" request
    And body with value {"data": {"attributes": {"name": "an example service name"}, "type": "services"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an existing incident service returns "Bad Request" response
    Given operation "DeleteIncidentService" enabled
    And new "DeleteIncidentService" request
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an existing incident service returns "Not Found" response
    Given operation "DeleteIncidentService" enabled
    And new "DeleteIncidentService" request
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Delete an existing incident service returns "OK" response
    Given there is a valid "service" in the system
    And operation "DeleteIncidentService" enabled
    And new "DeleteIncidentService" request
    And request contains "service_id" parameter from "service.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of all incident services returns "Bad Request" response
    Given operation "ListIncidentServices" enabled
    And new "ListIncidentServices" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of all incident services returns "Not Found" response
    Given operation "ListIncidentServices" enabled
    And new "ListIncidentServices" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Get a list of all incident services returns "OK" response
    Given there is a valid "service" in the system
    And operation "ListIncidentServices" enabled
    And new "ListIncidentServices" request
    And request contains "filter" parameter from "service.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.name" has the same value as "service.data.attributes.name"

  @generated @skip @team:Datadog/incident-app
  Scenario: Get details of an incident service returns "Bad Request" response
    Given operation "GetIncidentService" enabled
    And new "GetIncidentService" request
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get details of an incident service returns "Not Found" response
    Given operation "GetIncidentService" enabled
    And new "GetIncidentService" request
    And request contains "service_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Get details of an incident service returns "OK" response
    Given there is a valid "service" in the system
    And operation "GetIncidentService" enabled
    And new "GetIncidentService" request
    And request contains "service_id" parameter from "service.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "service.data.attributes.name"

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an existing incident service returns "Bad Request" response
    Given operation "UpdateIncidentService" enabled
    And new "UpdateIncidentService" request
    And request contains "service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "an example service name"}, "id": "00000000-0000-0000-0000-000000000000", "type": "services"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an existing incident service returns "Not Found" response
    Given operation "UpdateIncidentService" enabled
    And new "UpdateIncidentService" request
    And request contains "service_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "an example service name"}, "id": "00000000-0000-0000-0000-000000000000", "type": "services"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Update an existing incident service returns "OK" response
    Given there is a valid "service" in the system
    And operation "UpdateIncidentService" enabled
    And new "UpdateIncidentService" request
    And request contains "service_id" parameter from "service.data.id"
    And body with value {"data": {"type": "services", "attributes": {"name": "{{ service.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ service.data.attributes.name }}-updated"
