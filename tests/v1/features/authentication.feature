@endpoint(authentication) @endpoint(authentication-v1)
Feature: Authentication
  All requests to Datadog’s API must be authenticated. Requests that write
  data require reporting access and require an `API key`. Requests that read
  data require full access and also require an `application key`.  **Note:**
  All Datadog API clients are configured by default to consume Datadog US
  site APIs. If you are on the Datadog EU site, set the environment variable
  `DATADOG_HOST` to `https://api.datadoghq.eu` or override this value
  directly when creating your client.  [Manage your account’s API and
  application keys](https://app.datadoghq.com/account/settings#api).

  Background:
    Given an instance of "Authentication" API
    And new "Validate" request

  @skip-validation @team:DataDog/team-aaa
  Scenario: Validate API key returns "Forbidden" response
    When the request is sent
    Then the response status is 403 OK

  @team:DataDog/team-aaa
  Scenario: Validate API key returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    When the request is sent
    Then the response status is 200 OK
