@endpoint(delegated-token) @endpoint(delegated-token-v2)
Feature: Delegated Token
  Exchange a cloud-provider identity proof or Datadog credential for a
  short-lived delegated-user JWT via Workload Identity Federation.

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get a delegated token returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DelegatedToken" API
    And new "GetDelegatedToken" request
    When the request is sent
    Then the response status is 200 OK
