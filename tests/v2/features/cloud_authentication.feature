@endpoint(cloud-authentication) @endpoint(cloud-authentication-v2)
Feature: Cloud Authentication
  Configure AWS cloud authentication mappings for persona and intake
  authentication through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudAuthentication" API
    And operation "ListAWSCloudAuthPersonaMappings" enabled
    And new "ListAWSCloudAuthPersonaMappings" request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List AWS cloud authentication persona mappings returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List AWS cloud authentication persona mappings returns "OK" response
    When the request is sent
    Then the response status is 200 OK
