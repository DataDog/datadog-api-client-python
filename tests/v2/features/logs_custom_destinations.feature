@endpoint(logs-custom-destinations) @endpoint(logs-custom-destinations-v2)
Feature: Logs Custom Destinations
  Custom Destinations forward all the logs ingested to an external
  destination.  **Note**: Log forwarding is not available for the Government
  (US1-FED) site. Contact your account representative for more information.
  See the [Custom Destinations
  Page](https://app.datadoghq.com/logs/pipelines/log-forwarding/custom-
  destinations) for a list of the custom destinations currently configured
  in web UI.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsCustomDestinations" API

  @team:DataDog/logs-backend
  Scenario: Create a Basic HTTP custom destination returns "OK" response
    Given new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"enabled": false, "forward_tags": false, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"auth": {"password": "datadog-custom-destination-password", "type": "basic", "username": "datadog-custom-destination-username"}, "endpoint": "https://example.com", "type": "http"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_destination"
    And the response "data" has field "id"
    And the response "data.attributes.name" is equal to "Nginx logs"
    And the response "data.attributes.query" is equal to "source:nginx"
    And the response "data.attributes.forwarder_destination.type" is equal to "http"
    And the response "data.attributes.forwarder_destination.endpoint" is equal to "https://example.com"
    And the response "data.attributes.forwarder_destination.auth.type" is equal to "basic"
    And the response "data.attributes.forwarder_destination.auth" does not have field "username"
    And the response "data.attributes.forwarder_destination.auth" does not have field "password"
    And the response "data.attributes.enabled" is false
    And the response "data.attributes.forward_tags" is false
    And the response "data.attributes.forward_tags_restriction_list" has length 2
    And the response "data.attributes.forward_tags_restriction_list" array contains value "datacenter"
    And the response "data.attributes.forward_tags_restriction_list" array contains value "host"
    And the response "data.attributes.forward_tags_restriction_list_type" is equal to "ALLOW_LIST"

  @team:DataDog/logs-backend
  Scenario: Create a Custom Header HTTP custom destination returns "OK" response
    Given new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"enabled": false, "forward_tags": false, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"auth": {"header_value": "my-secret", "type": "custom_header", "header_name": "MY-AUTHENTICATION-HEADER"}, "endpoint": "https://example.com", "type": "http"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_destination"
    And the response "data" has field "id"
    And the response "data.attributes.name" is equal to "Nginx logs"
    And the response "data.attributes.query" is equal to "source:nginx"
    And the response "data.attributes.forwarder_destination.type" is equal to "http"
    And the response "data.attributes.forwarder_destination.endpoint" is equal to "https://example.com"
    And the response "data.attributes.forwarder_destination.auth.type" is equal to "custom_header"
    And the response "data.attributes.forwarder_destination.auth.header_name" is equal to "MY-AUTHENTICATION-HEADER"
    And the response "data.attributes.forwarder_destination.auth" does not have field "header_value"
    And the response "data.attributes.enabled" is false
    And the response "data.attributes.forward_tags" is false
    And the response "data.attributes.forward_tags_restriction_list" has length 2
    And the response "data.attributes.forward_tags_restriction_list" array contains value "datacenter"
    And the response "data.attributes.forward_tags_restriction_list" array contains value "host"
    And the response "data.attributes.forward_tags_restriction_list_type" is equal to "ALLOW_LIST"

  @team:DataDog/logs-backend
  Scenario: Create a Splunk custom destination returns "OK" response
    Given new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"enabled": false, "forward_tags": false, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"access_token": "my-access-token", "endpoint": "https://example.com", "type": "splunk_hec"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_destination"
    And the response "data" has field "id"
    And the response "data.attributes.name" is equal to "Nginx logs"
    And the response "data.attributes.query" is equal to "source:nginx"
    And the response "data.attributes.forwarder_destination.type" is equal to "splunk_hec"
    And the response "data.attributes.forwarder_destination.endpoint" is equal to "https://example.com"
    And the response "data.attributes.forwarder_destination" does not have field "access_token"
    And the response "data.attributes.enabled" is false
    And the response "data.attributes.forward_tags" is false
    And the response "data.attributes.forward_tags_restriction_list" has length 2
    And the response "data.attributes.forward_tags_restriction_list" array contains value "datacenter"
    And the response "data.attributes.forward_tags_restriction_list" array contains value "host"
    And the response "data.attributes.forward_tags_restriction_list_type" is equal to "ALLOW_LIST"

  @skip-java @skip-python @skip-rust @skip-typescript @team:DataDog/logs-backend
  Scenario: Create a custom destination returns "Bad Request" response
    Given new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"name": "Nginx logs"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Create a custom destination returns "Conflict" response
    Given new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"enabled": true, "forward_tags": true, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"auth": {"password": "datadog-custom-destination-password", "type": "basic", "username": "datadog-custom-destination-username"}, "endpoint": "https://example.com", "type": "http"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/logs-backend
  Scenario: Create a custom destination returns "OK" response
    Given new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"enabled": true, "forward_tags": true, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"auth": {"password": "datadog-custom-destination-password", "type": "basic", "username": "datadog-custom-destination-username"}, "endpoint": "https://example.com", "type": "http"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/logs-backend
  Scenario: Create an Elasticsearch custom destination returns "OK" response
    Given new "CreateLogsCustomDestination" request
    And body with value {"data": {"attributes": {"enabled": false, "forward_tags": false, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"auth": {"username": "my-username", "password": "my-password"}, "index_name": "nginx-logs", "index_rotation": "yyyy-MM-dd", "endpoint": "https://example.com", "type": "elasticsearch"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_destination"
    And the response "data" has field "id"
    And the response "data.attributes.name" is equal to "Nginx logs"
    And the response "data.attributes.query" is equal to "source:nginx"
    And the response "data.attributes.forwarder_destination.type" is equal to "elasticsearch"
    And the response "data.attributes.forwarder_destination.endpoint" is equal to "https://example.com"
    And the response "data.attributes.forwarder_destination.index_name" is equal to "nginx-logs"
    And the response "data.attributes.forwarder_destination.index_rotation" is equal to "yyyy-MM-dd"
    And the response "data.attributes.forwarder_destination.auth" does not have field "username"
    And the response "data.attributes.forwarder_destination.auth" does not have field "password"
    And the response "data.attributes.enabled" is false
    And the response "data.attributes.forward_tags" is false
    And the response "data.attributes.forward_tags_restriction_list" has length 2
    And the response "data.attributes.forward_tags_restriction_list" array contains value "datacenter"
    And the response "data.attributes.forward_tags_restriction_list" array contains value "host"
    And the response "data.attributes.forward_tags_restriction_list_type" is equal to "ALLOW_LIST"

  @generated @skip @team:DataDog/logs-backend
  Scenario: Delete a custom destination returns "Bad Request" response
    Given new "DeleteLogsCustomDestination" request
    And request contains "custom_destination_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-backend
  Scenario: Delete a custom destination returns "Not Found" response
    Given new "DeleteLogsCustomDestination" request
    And request contains "custom_destination_id" parameter with value "does-not-exist"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-backend
  Scenario: Delete a custom destination returns "OK" response
    Given new "DeleteLogsCustomDestination" request
    And there is a valid "custom_destination" in the system
    And request contains "custom_destination_id" parameter from "custom_destination.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Get a custom destination returns "Bad Request" response
    Given new "GetLogsCustomDestination" request
    And request contains "custom_destination_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/logs-backend
  Scenario: Get a custom destination returns "Not Found" response
    Given new "GetLogsCustomDestination" request
    And request contains "custom_destination_id" parameter with value "does-not-exist"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/logs-backend
  Scenario: Get a custom destination returns "OK" response
    Given new "GetLogsCustomDestination" request
    And there is a valid "custom_destination" in the system
    And request contains "custom_destination_id" parameter from "custom_destination.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_destination"
    And the response "data.id" is equal to "{{ custom_destination.data.id }}"
    And the response "data.attributes.name" is equal to "{{ custom_destination.data.attributes.name }}"
    And the response "data.attributes.query" is equal to "{{ custom_destination.data.attributes.query }}"
    And the response "data.attributes.forwarder_destination.type" is equal to "{{ custom_destination.data.attributes.forwarder_destination.type }}"
    And the response "data.attributes.forwarder_destination.endpoint" is equal to "{{ custom_destination.data.attributes.forwarder_destination.endpoint }}"
    And the response "data.attributes.forwarder_destination.auth.type" is equal to "{{ custom_destination.data.attributes.forwarder_destination.auth.type }}"
    And the response "data.attributes.forwarder_destination.auth" does not have field "username"
    And the response "data.attributes.forwarder_destination.auth" does not have field "password"
    And the response "data.attributes.enabled" is false
    And the response "data.attributes.forward_tags" is false
    And the response "data.attributes.forward_tags_restriction_list" has length 1
    And the response "data.attributes.forward_tags_restriction_list" array contains value "host"
    And the response "data.attributes.forward_tags_restriction_list_type" is equal to "{{ custom_destination.data.attributes.forward_tags_restriction_list_type }}"

  @team:DataDog/logs-backend
  Scenario: Get all custom destinations returns "OK" response
    Given new "ListLogsCustomDestinations" request
    And there is a valid "custom_destination" in the system
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "type" with value "custom_destination"
    And the response "data" has item with field "id" with value "{{ custom_destination.data.id }}"
    And the response "data" has item with field "attributes.name" with value "{{ custom_destination.data.attributes.name }}"
    And the response "data" has item with field "attributes.query" with value "{{ custom_destination.data.attributes.query }}"
    And the response "data" has item with field "attributes.forwarder_destination.type" with value "{{ custom_destination.data.attributes.forwarder_destination.type }}"
    And the response "data" has item with field "attributes.forwarder_destination.endpoint" with value "{{ custom_destination.data.attributes.forwarder_destination.endpoint }}"
    And the response "data" has item with field "attributes.forwarder_destination.auth.type" with value "{{ custom_destination.data.attributes.forwarder_destination.auth.type }}"
    And the response "data" has item with field "attributes.enabled" with value false
    And the response "data" has item with field "attributes.forward_tags" with value false
    And the response "data" has item with field "attributes.forward_tags_restriction_list_type" with value "{{ custom_destination.data.attributes.forward_tags_restriction_list_type }}"

  @team:DataDog/logs-backend
  Scenario: Update a custom destination returns "Bad Request" response
    Given new "UpdateLogsCustomDestination" request
    And there is a valid "custom_destination" in the system
    And request contains "custom_destination_id" parameter from "custom_destination.data.id"
    And body with value {"data": {"attributes": {"forward_tags_restriction_list_type": "this_list_type_does_not_exist"}, "type": "custom_destination", "id": "{{ custom_destination.data.id }}" }}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/logs-backend
  Scenario: Update a custom destination returns "Conflict" response
    Given new "UpdateLogsCustomDestination" request
    And request contains "custom_destination_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": false, "forward_tags": false, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"auth": {"password": "datadog-custom-destination-password", "type": "basic", "username": "datadog-custom-destination-username"}, "endpoint": "https://example.com", "type": "http"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/logs-backend
  Scenario: Update a custom destination returns "Not Found" response
    Given new "UpdateLogsCustomDestination" request
    And request contains "custom_destination_id" parameter with value "id-from-non-existing-custom-destination"
    And body with value {"data": {"attributes": {"enabled": false, "forward_tags": false, "forward_tags_restriction_list": ["datacenter", "host"], "forward_tags_restriction_list_type": "ALLOW_LIST", "forwarder_destination": {"auth": {"type": "basic", "username": "datadog-custom-destination-username", "password": "datadog-custom-destination-password"}, "endpoint": "https://example.com", "type": "http"}, "name": "Nginx logs", "query": "source:nginx"}, "type": "custom_destination", "id": "id-from-non-existing-custom-destination" }}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/logs-backend
  Scenario: Update a custom destination returns "OK" response
    Given new "UpdateLogsCustomDestination" request
    And there is a valid "custom_destination" in the system
    And request contains "custom_destination_id" parameter from "custom_destination.data.id"
    And body with value {"data": {"attributes": {"name": "Nginx logs (Updated)", "query": "source:nginx", "enabled":false, "forward_tags":false, "forward_tags_restriction_list_type":"BLOCK_LIST"}, "type": "custom_destination", "id": "{{ custom_destination.data.id }}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_destination"
    And the response "data.id" is equal to "{{ custom_destination.data.id }}"
    And the response "data.attributes.name" is equal to "Nginx logs (Updated)"
    And the response "data.attributes.query" is equal to "{{ custom_destination.data.attributes.query }}"
    And the response "data.attributes.forwarder_destination.type" is equal to "{{ custom_destination.data.attributes.forwarder_destination.type }}"
    And the response "data.attributes.forwarder_destination.endpoint" is equal to "{{ custom_destination.data.attributes.forwarder_destination.endpoint }}"
    And the response "data.attributes.forwarder_destination.auth.type" is equal to "{{ custom_destination.data.attributes.forwarder_destination.auth.type }}"
    And the response "data.attributes.forwarder_destination.auth" does not have field "username"
    And the response "data.attributes.forwarder_destination.auth" does not have field "password"
    And the response "data.attributes.enabled" is false
    And the response "data.attributes.forward_tags" is false
    And the response "data.attributes.forward_tags_restriction_list" has length 1
    And the response "data.attributes.forward_tags_restriction_list" array contains value "host"
    And the response "data.attributes.forward_tags_restriction_list_type" is equal to "{{ custom_destination.data.attributes.forward_tags_restriction_list_type }}"
