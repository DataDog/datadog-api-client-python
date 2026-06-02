@endpoint(stegadography) @endpoint(stegadography-v2)
Feature: Stegadography
  Recover dashboard widget data from watermarks embedded in images.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Stegadography" API
    And operation "GetWidgetsFromImage" enabled
    And new "GetWidgetsFromImage" request

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Get widgets from an image returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Get widgets from an image returns "OK" response
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Get widgets from an image returns "Unsupported Media Type" response
    When the request is sent
    Then the response status is 415 Unsupported Media Type
