@endpoint(domain-allowlist) @endpoint(domain-allowlist-v2)
Feature: Domain Allowlist
  Configure your Datadog Email Domain Allowlist directly through the Datadog
  API. The Email Domain Allowlist controls the domains that certain datadog
  emails can be sent to. For more information, see the [Domain Allowlist
  docs page](https://docs.datadoghq.com/account_management/org_settings/doma
  in_allowlist)

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DomainAllowlist" API

  @team:Datadog/team-aaa-dogmail
  Scenario: Get Domain Allowlist returns "OK" response
    Given new "GetDomainAllowlist" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "domain_allowlist"
    And the response "data.attributes.domains" array contains value "@static-test-domain.test"
    And the response "data.attributes.enabled" is equal to false

  @team:Datadog/team-aaa-dogmail
  Scenario: Sets Domain Allowlist returns "OK" response
    Given new "PatchDomainAllowlist" request
    And body with value {"data": {"attributes": {"domains": ["@static-test-domain.test"], "enabled": false}, "type": "domain_allowlist"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "domain_allowlist"
    And the response "data.attributes.domains" has length 1
    And the response "data.attributes.domains" array contains value "@static-test-domain.test"
    And the response "data.attributes.enabled" is equal to false
