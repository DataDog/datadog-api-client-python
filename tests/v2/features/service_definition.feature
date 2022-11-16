@endpoint(service-definition) @endpoint(service-definition-v2)
Feature: Service Definition
  API to create, update, retrieve and delete service definitions.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceDefinition" API

  @generated @skip @team:DataDog/apm-insights
  Scenario: Create or update service definition returns "Bad Request" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"contacts": [{"contact": "contact@datadoghq.com", "name": "Team Email", "type": "email"}], "dd-service": "my-service", "dd-team": "my-team", "docs": [{"name": "Architecture", "provider": "google drive", "url": "https://gdrive/mydoc"}], "extensions": {"myorg/extension": "extensionValue"}, "integrations": {"opsgenie": {"region": "US", "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"}, "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"}, "links": [{"name": "Runbook", "type": "runbook", "url": "https://my-runbook"}], "repos": [{"name": "Source Code", "provider": "GitHub", "url": "https://github.com/DataDog/schema"}], "schema-version": "v2", "tags": ["my:tag", "service:tag"], "team": "my-team"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/apm-insights
  Scenario: Create or update service definition returns "CREATED" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"contacts": [{"contact": "contact@datadoghq.com", "name": "Team Email", "type": "email"}], "dd-service": "service-{{ unique }}", "dd-team": "my-team", "docs": [{"name": "Architecture", "provider": "google drive", "url": "https://gdrive/mydoc"}], "extensions": {"myorgextension": "extensionvalue"}, "integrations": {"opsgenie": {"region": "US", "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"}, "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"}, "links": [{"name": "Runbook", "type": "runbook", "url": "https://my-runbook"}], "repos": [{"name": "Source Code", "provider": "GitHub", "url": "https://github.com/DataDog/schema"}], "schema-version": "v2", "tags": ["my:tag", "service:tag"], "team": "my-team"}
    When the request is sent
    Then the response status is 200 CREATED
    And the response "data[0].attributes.meta.ingested-schema-version" is equal to "v2"

  @generated @skip @team:DataDog/apm-insights
  Scenario: Create or update service definition returns "Conflict" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"contacts": [{"contact": "contact@datadoghq.com", "name": "Team Email", "type": "email"}], "dd-service": "my-service", "dd-team": "my-team", "docs": [{"name": "Architecture", "provider": "google drive", "url": "https://gdrive/mydoc"}], "extensions": {"myorg/extension": "extensionValue"}, "integrations": {"opsgenie": {"region": "US", "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"}, "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"}, "links": [{"name": "Runbook", "type": "runbook", "url": "https://my-runbook"}], "repos": [{"name": "Source Code", "provider": "GitHub", "url": "https://github.com/DataDog/schema"}], "schema-version": "v2", "tags": ["my:tag", "service:tag"], "team": "my-team"}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/apm-insights
  Scenario: Delete a single service definition returns "Bad Request" response
    Given new "DeleteServiceDefinition" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/apm-insights
  Scenario: Delete a single service definition returns "Not Found" response
    Given new "DeleteServiceDefinition" request
    And request contains "service_name" parameter with value "not-a-service"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors[0]" is equal to "Not Found"

  @replay-only @team:DataDog/apm-insights
  Scenario: Delete a single service definition returns "OK" response
    Given new "DeleteServiceDefinition" request
    And request contains "service_name" parameter with value "service-definition-test"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/apm-insights
  Scenario: Get a single service definition returns "Bad Request" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/apm-insights
  Scenario: Get a single service definition returns "Conflict" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/apm-insights
  Scenario: Get a single service definition returns "Not Found" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter with value "not-a-service"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors[0]" is equal to "Not Found"

  @team:DataDog/apm-insights
  Scenario: Get a single service definition returns "OK" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter with value "service-definition-test"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.meta.ingested-schema-version" is equal to "v2"

  @team:DataDog/apm-insights
  Scenario: Get all service definitions returns "OK" response
    Given new "ListServiceDefinitions" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.meta.ingested-schema-version" is equal to "v2"
