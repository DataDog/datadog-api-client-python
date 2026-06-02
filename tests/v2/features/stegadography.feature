@endpoint(stegadography) @endpoint(stegadography-v2)
Feature: Stegadography
  Extract watermarks embedded in dashboard screenshots to retrieve cached
  widget state.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Stegadography" API
    And new "GetStegadographyWidgets" request

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Get widgets from an image returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/dataviz-backend-maintainers
  Scenario: Get widgets from an image returns "OK" response
    Given request contains "image" parameter with value "fixtures/stegadography/image.png"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Get widgets from an image returns "Unsupported Media Type" response
    When the request is sent
    Then the response status is 415 Unsupported Media Type
