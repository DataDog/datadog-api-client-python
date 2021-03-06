@endpoint(authentication)
Feature: Authentication
  All requests to Datadog’s API must be authenticated. Requests that write
  data require reporting access and require an `API key`. Requests that read
  data require full access and also require an `application key`.  **Note:**
  All Datadog API clients are configured by default to consume Datadog US
  site APIs. If you are on the Datadog EU site, set the environment variable
  `DATADOG_HOST` to `https://api.datadoghq.eu` or override this value
  directly when creating your client.  [Manage your account’s API and
  application keys](https://app.datadoghq.com/account/settings#api).

  @generated @skip
  Scenario: Validate API key returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And an instance of "Authentication" API
    And new "Validate" request
    When the request is sent
    Then the response status is 200 OK
