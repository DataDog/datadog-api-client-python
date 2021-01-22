@endpoint(logs)
Feature: Logs
  Search your logs and send them to your Datadog platform over HTTP. Limits
  per HTTP request are:  - Maximum content size per payload (uncompressed):
  5MB - Maximum size for a single log: 1MB - Maximum array size if sending
  multiple logs in an array: 1000 entries  Any log exceeding 1MB is accepted
  and truncated by Datadog: - For a single log request, the API truncates
  the log at 1MB and returns a 2xx. - For a multi-logs request, the API
  processes all logs, truncates only logs larger than 1MB, and returns a
  2xx.  Datadog recommends sending your logs compressed. Add the `Content-
  Encoding: gzip` header to the request when sending compressed logs.  The
  status codes answered by the HTTP API are: - 200: OK - 400: Bad request
  (likely an issue in the payload formatting) - 403: Permission issue
  (likely using an invalid API Key) - 413: Payload too large (batch is above
  5MB uncompressed) - 5xx: Internal error, request should be retried after
  some time

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Logs" API
    And new "ListLogs" request
    And body {}

  @generated @skip
  Scenario: Get a list of logs returns "OK" response
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a list of logs returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request
