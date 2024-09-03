@endpoint(software-catalog) @endpoint(software-catalog-v2)
Feature: Software Catalog
  API to create, update, retrieve and delete Software Catalog entities.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SoftwareCatalog" API

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create or update entities returns "ACCEPTED" response
    Given new "UpsertCatalogEntity" request
    And body with value {"apiVersion": "v3", "datadog": {"codeLocations": [{"paths": []}], "events": [{}], "logs": [{}], "performanceData": {"tags": []}, "pipelines": {"fingerprints": []}}, "integrations": {"opsgenie": {"serviceURL": "https://www.opsgenie.com/service/shopping-cart"}, "pagerduty": {"serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"}}, "kind": "service", "metadata": {"additionalOwners": [], "contacts": [{"contact": "https://slack/", "type": "slack"}], "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb", "inheritFrom": "application:default/myapp", "links": [{"name": "mylink", "type": "link", "url": "https://mylink"}], "name": "myService", "namespace": "default", "tags": ["this:tag", "that:tag"]}, "spec": {"dependsOn": [], "languages": []}}
    When the request is sent
    Then the response status is 202 ACCEPTED

  @generated @skip @team:DataDog/service-catalog
  Scenario: Create or update entities returns "Bad Request" response
    Given new "UpsertCatalogEntity" request
    And body with value {"apiVersion": "v3", "datadog": {"codeLocations": [{"paths": []}], "events": [{}], "logs": [{}], "performanceData": {"tags": []}, "pipelines": {"fingerprints": []}}, "integrations": {"opsgenie": {"serviceURL": "https://www.opsgenie.com/service/shopping-cart"}, "pagerduty": {"serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"}}, "kind": "service", "metadata": {"additionalOwners": [], "contacts": [{"contact": "https://slack/", "type": "slack"}], "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb", "inheritFrom": "application:default/myapp", "links": [{"name": "mylink", "type": "link", "url": "https://mylink"}], "name": "myService", "namespace": "default", "tags": ["this:tag", "that:tag"]}, "spec": {"dependsOn": [], "languages": []}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/service-catalog
  Scenario: Create or update entities without metadata name returns "Internal Server Error" response
    Given new "UpsertCatalogEntity" request
    And body with value {"apiVersion": "v3", "datadog": {"codeLocations": [{"paths": []}], "events": [{}], "logs": [{}], "performanceData": {"tags": []}, "pipelines": {"fingerprints": []}}, "integrations": {"opsgenie": {"serviceURL": "https://www.opsgenie.com/service/shopping-cart"}, "pagerduty": {"serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"}}, "kind": "service", "metadata": {"additionalOwners": [], "contacts": [{"contact": "https://slack/", "type": "slack"}], "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb", "inheritFrom": "application:default/myapp", "links": [{"name": "mylink", "type": "link", "url": "https://mylink"}], "tags": ["this:tag", "that:tag"]}, "spec": {"dependsOn": [], "languages": []}}
    When the request is sent
    Then the response status is 500 Internal Server Error

  @team:DataDog/service-catalog
  Scenario: Create or update software catalog entity using schema v3 returns "ACCEPTED" response
    Given new "UpsertCatalogEntity" request
    And body with value {"apiVersion": "v3", "datadog": {"codeLocations": [{"paths": []}], "events": [{}], "logs": [{}], "performanceData": {"tags": []}, "pipelines": {"fingerprints": []}}, "integrations": {"opsgenie": {"serviceURL": "https://www.opsgenie.com/service/shopping-cart"}, "pagerduty": {"serviceURL": "https://www.pagerduty.com/service-directory/Pshopping-cart"}}, "kind": "service", "metadata": {"additionalOwners": [], "contacts": [{"contact": "https://slack/", "type": "slack"}], "id": "4b163705-23c0-4573-b2fb-f6cea2163fcb", "inheritFrom": "application:default/myapp", "links": [{"name": "mylink", "type": "link", "url": "https://mylink"}], "name": "service-{{ unique_lower_alnum }}", "tags": ["this:tag", "that:tag"]}, "spec": {"dependsOn": [], "languages": []}}
    When the request is sent
    Then the response status is 202 ACCEPTED
    And the response "data[0].attributes.apiVersion" is equal to "v3"
    And the response "data[0].attributes.kind" is equal to "service"
    And the response "data[0].attributes.name" is equal to "service-{{ unique_lower_alnum }}"

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a single entity returns "Bad Request" response
    Given new "DeleteCatalogEntity" request
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a single entity returns "Not Found" response
    Given new "DeleteCatalogEntity" request
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/service-catalog
  Scenario: Delete a single entity returns "OK" response
    Given new "DeleteCatalogEntity" request
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @skip @team:DataDog/service-catalog
  Scenario: Delete an entity returns "Not Found" response
    Given new "DeleteCatalogEntity" request
    And request contains "entity_id" parameter with value "service:not-a-service"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors[0]" is equal to "Not Found"

  @team:DataDog/service-catalog
  Scenario: Get a list of entities returns "OK" response
    Given new "ListCatalogEntity" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/service-catalog @with-pagination
  Scenario: Get a list of entities returns "OK" response with pagination
    Given new "ListCatalogEntity" request
    When the request with pagination is sent
    Then the response status is 200 OK
