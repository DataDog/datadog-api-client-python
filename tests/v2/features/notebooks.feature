@endpoint(notebooks) @endpoint(notebooks-v2)
Feature: Notebooks
  Interact with your notebooks through the API to search and retrieve
  notebooks.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Notebooks" API
    And operation "SearchNotebooks" enabled
    And new "SearchNotebooks" request

  @generated @skip @team:DataDog/notebooks-backend
  Scenario: Search notebooks returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/notebooks-backend
  Scenario: Search notebooks returns "OK" response
    When the request is sent
    Then the response status is 200 OK
