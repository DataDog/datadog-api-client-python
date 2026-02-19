@endpoint(integrations) @endpoint(integrations-v2)
Feature: Integrations
  The Integrations API is used to list available integrations and retrieve
  information about their installation status.

  @skip-validation @team:DataDog/integrations-experience
  Scenario: List Integrations returns "Successful Response." response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Integrations" API
    And new "ListIntegrations" request
    When the request is sent
    Then the response status is 200 Successful Response.
