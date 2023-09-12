@endpoint(logs-custom-destinations) @endpoint(logs-custom-destinations-v2)
Feature: Logs Custom Destinations
  **Note: This endpoint is in public beta. If you have any feedback, contact
  [Datadog support](https://docs.datadoghq.com/help/).**  Manage
  configuration of [log-based custom
  destinations](https://app.datadoghq.com/logs/pipelines/log-
  forwarding/custom-destinations) for your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsCustomDestinations" API

  @skip-validation @team:DataDog/logs-app
  Scenario: Create a custom destination returns "Bad Request" response
    Given operation "CreateLogsCustomDestination" enabled
    And new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"name": "", "forwarderDestination": {"auth": {"password": "password", "type": "basic", "username": "username"}, "endpoint": "https://example.org/my-intake", "type": "http"}, "version": 0}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app
  Scenario: Create a custom destination returns "OK" response
    Given operation "CreateLogsCustomDestination" enabled
    And new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"bufferMaxBytes": 10000000, "bufferTimeoutSeconds": 100, "compression": "GZIP", "enabled": true, "fallbackDestination": {"container": "container-name", "integration": {"clientId": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa", "tenantId": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"}, "storageAccount": "account-name", "type": "azure"}, "forwarderDestination": {"auth": {"password": "password", "type": "basic", "username": "username"}, "endpoint": "https://example.org/my-intake", "type": "http"}, "maxRetryDurationSeconds": 100, "name": "my-destination", "query": "source:dummy", "version": 0}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "my-destination"

  @team:DataDog/logs-app
  Scenario: Create a custom destination with Elasticsearch forwarding returns "OK" response
    Given operation "CreateLogsCustomDestination" enabled
    And new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"name": "my-destination", "version": 0, "forwarderDestination": {"type": "elasticsearch", "endpoint": "https://example.org/my-intake", "indexName": "name", "indexRotation": "yyyy-MM-dd", "auth": {"type": "basic", "username": "username", "password": "password"}}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "my-destination"

  @team:DataDog/logs-app
  Scenario: Create a custom destination with HTTP basic auth forwarding returns "OK" response
    Given operation "CreateLogsCustomDestination" enabled
    And new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"name": "my-destination", "version": 0, "forwarderDestination": {"type": "http", "endpoint": "https://example.org/my-intake", "auth": {"type": "basic", "username": "username", "password": "password"}}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "my-destination"

  @team:DataDog/logs-app
  Scenario: Create a custom destination with HTTP request header forwarding returns "OK" response
    Given operation "CreateLogsCustomDestination" enabled
    And new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"name": "my-destination", "version": 0, "forwarderDestination": {"type": "http", "endpoint": "https://example.org/my-intake", "auth": {"type": "custom_header", "headerName": "header", "headerValue": "value"}}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "my-destination"

  @team:DataDog/logs-app
  Scenario: Create a custom destination with Splunk forwarding returns "OK" response
    Given operation "CreateLogsCustomDestination" enabled
    And new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"name": "my-destination", "version": 0, "forwarderDestination": {"type": "splunk_hec", "endpoint": "https://example.org/my-intake", "accessToken": "secret"}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-app
  Scenario: Delete a custom destination returns "Not Found" response
    Given operation "DeleteLogsCustomDestination" enabled
    And new "DeleteLogsCustomDestination" request
    And request contains "custom_destination_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/logs-app
  Scenario: Delete a custom destination returns "Not found" response
    Given operation "DeleteLogsCustomDestination" enabled
    And new "DeleteLogsCustomDestination" request
    And request contains "custom_destination_id" parameter with value "some-non-existent-id"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-app
  Scenario: Delete a custom destination returns "OK" response
    Given operation "DeleteLogsCustomDestination" enabled
    And new "DeleteLogsCustomDestination" request
    And there is a valid "logs_custom_destination" in the system
    And request contains "custom_destination_id" parameter from "logs_custom_destination.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-app
  Scenario: Get a custom destination returns "Not Found" response
    Given operation "GetLogsCustomDestination" enabled
    And new "GetLogsCustomDestination" request
    And request contains "custom_destination_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/logs-app
  Scenario: Get a custom destination returns "Not found" response
    Given operation "GetLogsCustomDestination" enabled
    And new "GetLogsCustomDestination" request
    And request contains "custom_destination_id" parameter with value "some-non-existent-id"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-app
  Scenario: Get a custom destination returns "OK" response
    Given operation "GetLogsCustomDestination" enabled
    And new "GetLogsCustomDestination" request
    And there is a valid "logs_custom_destination" in the system
    And request contains "custom_destination_id" parameter from "logs_custom_destination.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ logs_custom_destination.data.attributes.name }}"

  @team:DataDog/logs-app
  Scenario: List custom destinations returns "OK" response
    Given operation "ListLogsCustomDestinations" enabled
    And new "ListLogsCustomDestinations" request
    And there is a valid "logs_custom_destination" in the system
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "{{ logs_custom_destination.data.attributes.name }}"

  @skip-validation @team:DataDog/logs-app
  Scenario: Update a custom destination returns "Bad Request" response
    Given operation "UpdateLogsCustomDestination" enabled
    And new "UpdateLogsCustomDestination" request
    And there is a valid "logs_custom_destination" in the system
    And request contains "custom_destination_id" parameter from "logs_custom_destination.data.id"
    And body with value {"data": {"id": "{{ logs_custom_destination.data.id }}", "attributes": {"name": "", "version": 0, "forwarderDestination": {"type": "http", "endpoint": "https://example.org/my-intake", "auth": {"type": "basic", "username": "username", "password": "password"}}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-app
  Scenario: Update a custom destination returns "Conflict" response
    Given operation "UpdateLogsCustomDestination" enabled
    And new "UpdateLogsCustomDestination" request
    And there is a valid "logs_custom_destination" in the system
    And request contains "custom_destination_id" parameter from "logs_custom_destination.data.id"
    And body with value {"data": {"id": "{{ logs_custom_destination.data.id }}", "attributes": {"name": "{{ logs_custom_destination.data.attributes.name }}--updated-name", "version": -1, "forwarderDestination": {"type": "http", "endpoint": "https://example.org/my-intake", "auth": {"type": "basic", "username": "username", "password": "password"}}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/logs-app
  Scenario: Update a custom destination returns "Not Found" response
    Given operation "UpdateLogsCustomDestination" enabled
    And new "UpdateLogsCustomDestination" request
    And request contains "custom_destination_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bufferMaxBytes": 10000000, "bufferTimeoutSeconds": 100, "compression": "GZIP", "enabled": true, "fallbackDestination": {"container": "container-name", "integration": {"clientId": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa", "tenantId": "aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa"}, "storageAccount": "account-name", "type": "azure"}, "forwarderDestination": {"auth": {"password": "password", "type": "basic", "username": "username"}, "endpoint": "https://example.org/my-intake", "type": "http"}, "maxRetryDurationSeconds": 100, "name": "my-destination", "query": "source:dummy", "version": 0}, "id": "a8700823-acb7-4379-831d-9ae3d14bc855", "type": "custom_destination"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/logs-app
  Scenario: Update a custom destination returns "Not found" response
    Given operation "UpdateLogsCustomDestination" enabled
    And new "UpdateLogsCustomDestination" request
    And request contains "custom_destination_id" parameter with value "some-non-existent-id"
    And body with value {"data": {"id": "some-non-existent-id", "attributes": {"name": "so--updated-name", "version": 0, "forwarderDestination": {"type": "http", "endpoint": "https://example.org/my-intake", "auth": {"type": "basic", "username": "username", "password": "password"}}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-app
  Scenario: Update a custom destination returns "OK" response
    Given operation "UpdateLogsCustomDestination" enabled
    And new "UpdateLogsCustomDestination" request
    And there is a valid "logs_custom_destination" in the system
    And request contains "custom_destination_id" parameter from "logs_custom_destination.data.id"
    And body with value {"data": {"id": "{{ logs_custom_destination.data.id }}", "attributes": {"name": "{{ logs_custom_destination.data.attributes.name }}--updated-name", "version": 0, "forwarderDestination": {"type": "http", "endpoint": "https://example.org/my-intake", "auth": {"type": "basic", "username": "username", "password": "password"}}}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ logs_custom_destination.data.id }}"
    And the response "data.attributes.name" is equal to "{{ logs_custom_destination.data.attributes.name }}--updated-name"
