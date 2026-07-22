@endpoint(pup-bump-test) @endpoint(pup-bump-test-v2)
Feature: Pup Bump Test
  Temporary test-only tag used to exercise the pup dependency-bump
  generation and merge pipeline. Not a real product feature.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "PupBumpTest" API
    And operation "GetPupBumpTest" enabled
    And new "GetPupBumpTest" request

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get pup bump test resource returns "Not Found" response
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get pup bump test resource returns "OK" response
    When the request is sent
    Then the response status is 200 OK
