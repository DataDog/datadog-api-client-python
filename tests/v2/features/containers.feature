@endpoint(containers) @endpoint(containers-v2)
Feature: Containers
  The Containers API allows you to query container data for your
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Containers" API
    And new "ListContainers" request

  @replay-only @team:DataDog/processes
  Scenario: Get All Container groups returns "OK" response
    Given request contains "group_by" parameter with value "short_image"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.count" is equal to 123

  @generated @skip @team:DataDog/processes
  Scenario: Get All Containers returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/processes
  Scenario: Get All Containers returns "OK" response
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "test_name"

  @replay-only @skip-validation @team:DataDog/processes @with-pagination
  Scenario: Get All Containers returns "OK" response with pagination
    Given request contains "page[size]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items
