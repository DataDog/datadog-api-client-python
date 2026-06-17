@endpoint(intake-key) @endpoint(intake-key-v2)
Feature: Intake Key
  Exchange a cloud-provider identity proof for a Datadog API key via
  Workload Identity Federation intake mappings.

  @generated @skip @team:DataDog/credentials-management
  Scenario: Get an intake API key returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IntakeKey" API
    And new "GetIntakeKey" request
    When the request is sent
    Then the response status is 200 OK
