@endpoint(services) @v2
Feature: Services
  Create, update, delete and retrieve your organizations services.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Services" API

  Scenario: Get a list of all services returns "OK" response
    Given there is a valid "service" in the system
    And operation "GetServices" enabled
    And new "GetServices" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new service returns "CREATED" response
    Given operation "CreateService" enabled
    And new "CreateService" request
    And body {"data": {"type": "services", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{ unique }}"

  Scenario: Delete an existing service returns "OK" response
    Given there is a valid "service" in the system
    And operation "DeleteService" enabled
    And new "DeleteService" request
    And request contains "service_id" parameter from "service.data.id"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get details of a service returns "OK" response
    Given there is a valid "service" in the system
    And operation "GetService" enabled
    And new "GetService" request
    And request contains "service_id" parameter from "service.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "service.data.attributes.name"

  Scenario: Update an existing service returns "OK" response
    Given there is a valid "service" in the system
    And operation "UpdateService" enabled
    And new "UpdateService" request
    And request contains "service_id" parameter from "service.data.id"
    And body {"data": {"type": "services", "attributes": {"name": "{{ service.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ service.data.attributes.name }}-updated"
