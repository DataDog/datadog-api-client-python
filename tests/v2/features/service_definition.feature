@endpoint(service-definition) @endpoint(service-definition-v2)
Feature: Service Definition
  API to create, update, retrieve and delete service definitions.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceDefinition" API

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create or update service definition returns "Bad Request" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"application": "my-app", "contacts": [{"contact": "https://teams.microsoft.com/myteam", "name": "My team channel", "type": "slack"}], "dd-service": "my-service", "description": "My service description", "extensions": {"myorg/extension": "extensionValue"}, "integrations": {"opsgenie": {"region": "US", "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"}, "pagerduty": {"service-url": "https://my-org.pagerduty.com/service-directory/PMyService"}}, "languages": ["dotnet", "go", "java", "js", "php", "python", "ruby", "c++"], "lifecycle": "sandbox", "links": [{"name": "Runbook", "provider": "Github", "type": "runbook", "url": "https://my-runbook"}], "schema-version": "v2.2", "tags": ["my:tag", "service:tag"], "team": "my-team", "tier": "High", "type": "web"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create or update service definition returns "CREATED" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"application": "my-app", "contacts": [{"contact": "https://teams.microsoft.com/myteam", "name": "My team channel", "type": "slack"}], "dd-service": "my-service", "description": "My service description", "extensions": {"myorg/extension": "extensionValue"}, "integrations": {"opsgenie": {"region": "US", "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"}, "pagerduty": {"service-url": "https://my-org.pagerduty.com/service-directory/PMyService"}}, "languages": ["dotnet", "go", "java", "js", "php", "python", "ruby", "c++"], "lifecycle": "sandbox", "links": [{"name": "Runbook", "provider": "Github", "type": "runbook", "url": "https://my-runbook"}], "schema-version": "v2.2", "tags": ["my:tag", "service:tag"], "team": "my-team", "tier": "High", "type": "web"}
    When the request is sent
    Then the response status is 200 CREATED

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create or update service definition returns "Conflict" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"application": "my-app", "contacts": [{"contact": "https://teams.microsoft.com/myteam", "name": "My team channel", "type": "slack"}], "dd-service": "my-service", "description": "My service description", "extensions": {"myorg/extension": "extensionValue"}, "integrations": {"opsgenie": {"region": "US", "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"}, "pagerduty": {"service-url": "https://my-org.pagerduty.com/service-directory/PMyService"}}, "languages": ["dotnet", "go", "java", "js", "php", "python", "ruby", "c++"], "lifecycle": "sandbox", "links": [{"name": "Runbook", "provider": "Github", "type": "runbook", "url": "https://my-runbook"}], "schema-version": "v2.2", "tags": ["my:tag", "service:tag"], "team": "my-team", "tier": "High", "type": "web"}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/service-catalog
  Scenario: Create or update service definition using schema v2 returns "CREATED" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"contacts": [{"contact": "contact@datadoghq.com", "name": "Team Email", "type": "email"}], "dd-service": "service-{{ unique_lower_alnum }}", "dd-team": "my-team", "docs": [{"name": "Architecture", "provider": "google drive", "url": "https://gdrive/mydoc"}], "extensions": {"myorgextension": "extensionvalue"}, "integrations": {"opsgenie": {"region": "US", "service-url": "https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"}, "pagerduty": "https://my-org.pagerduty.com/service-directory/PMyService"}, "links": [{"name": "Runbook", "type": "runbook", "url": "https://my-runbook"}], "repos": [{"name": "Source Code", "provider": "GitHub", "url": "https://github.com/DataDog/schema"}], "schema-version": "v2", "tags": ["my:tag", "service:tag"], "team": "my-team"}
    When the request is sent
    Then the response status is 200 CREATED
    And the response "data[0].attributes.meta.ingested-schema-version" is equal to "v2"
    And the response "data[0].attributes.schema.dd-service" is equal to "service-{{ unique_lower_alnum }}"

  @team:DataDog/service-catalog
  Scenario: Create or update service definition using schema v2-1 returns "CREATED" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"contacts":[{"contact":"contact@datadoghq.com","name":"Team Email","type":"email"}],"dd-service":"service-{{ unique_lower_alnum }}","extensions":{"myorgextension":"extensionvalue"},"integrations":{"opsgenie":{"region":"US","service-url":"https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"},"pagerduty":{"service-url":"https://my-org.pagerduty.com/service-directory/PMyService"}},"links":[{"name":"Runbook","type":"runbook","url":"https://my-runbook"},{"name":"Source Code","type":"repo","provider":"GitHub","url":"https://github.com/DataDog/schema"},{"name":"Architecture","type":"doc","provider":"Gigoogle drivetHub","url":"https://my-runbook"}],"schema-version":"v2.1","tags":["my:tag","service:tag"],"team":"my-team"}
    When the request is sent
    Then the response status is 200 CREATED
    And the response "data[0].attributes.meta.ingested-schema-version" is equal to "v2.1"
    And the response "data[0].attributes.schema.dd-service" is equal to "service-{{ unique_lower_alnum }}"

  @team:DataDog/service-catalog
  Scenario: Create or update service definition using schema v2-2 returns "CREATED" response
    Given new "CreateOrUpdateServiceDefinitions" request
    And body with value {"contacts":[{"contact":"contact@datadoghq.com","name":"Team Email","type":"email"}],"dd-service":"service-{{ unique_lower_alnum }}","extensions":{"myorgextension":"extensionvalue"},"integrations":{"opsgenie":{"region":"US","service-url":"https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000"},"pagerduty":{"service-url":"https://my-org.pagerduty.com/service-directory/PMyService"}},"links":[{"name":"Runbook","type":"runbook","url":"https://my-runbook"},{"name":"Source Code","type":"repo","provider":"GitHub","url":"https://github.com/DataDog/schema"},{"name":"Architecture","type":"doc","provider":"Gigoogle drivetHub","url":"https://my-runbook"}],"schema-version":"v2.2","tags":["my:tag","service:tag"],"team":"my-team"}
    When the request is sent
    Then the response status is 200 CREATED
    And the response "data[0].attributes.meta.ingested-schema-version" is equal to "v2.2"
    And the response "data[0].attributes.schema.dd-service" is equal to "service-{{ unique_lower_alnum }}"

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a single service definition returns "Bad Request" response
    Given new "DeleteServiceDefinition" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/service-catalog
  Scenario: Delete a single service definition returns "Not Found" response
    Given new "DeleteServiceDefinition" request
    And request contains "service_name" parameter with value "not-a-service"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors[0]" is equal to "Not Found"

  @replay-only @team:DataDog/service-catalog
  Scenario: Delete a single service definition returns "OK" response
    Given new "DeleteServiceDefinition" request
    And request contains "service_name" parameter with value "service-definition-test"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a single service definition returns "Bad Request" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Get a single service definition returns "Conflict" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/service-catalog
  Scenario: Get a single service definition returns "Not Found" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter with value "not-a-service"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors[0]" is equal to "Not Found"

  @team:DataDog/service-catalog
  Scenario: Get a single service definition returns "OK" response
    Given new "GetServiceDefinition" request
    And request contains "service_name" parameter with value "service-definition-test"
    And request contains "schema_version" parameter with value "v2.1"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.meta.ingested-schema-version" is equal to "v2"
    And the response "data.attributes.schema.schema-version" is equal to "v2.1"
    And the response "data.attributes.schema.dd-service" is equal to "service-definition-test"

  @team:DataDog/service-catalog
  Scenario: Get all service definitions returns "OK" response
    Given new "ListServiceDefinitions" request
    And request contains "schema_version" parameter with value "v2.1"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.meta.ingestion-source" is equal to "api"
    And the response "data[0].attributes.schema.schema-version" is equal to "v2.1"

  @replay-only @skip-validation @team:DataDog/service-catalog @with-pagination
  Scenario: Get all service definitions returns "OK" response with pagination
    Given new "ListServiceDefinitions" request
    And request contains "page[size]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items
