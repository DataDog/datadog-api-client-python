@endpoint(logs)
Feature: Logs
  Send your logs to your Datadog platform over HTTP. Limits per HTTP request
  are:  - Maximum content size per payload: 5MB - Maximum size for a single
  log: 256kB - Maximum array size if sending multiple logs in an array: 500
  entries  Any log exceeding 256KB is accepted and truncated by Datadog: -
  For a single log request, the API truncates the log at 256KB and returns a
  2xx. - For a multi-logs request, the API processes all logs, truncates
  only logs larger than 256KB, and returns a 2xx.  We encourage you to send
  your logs compressed. Add the `Content-Encoding: gzip` header to the
  request when sending compressed logs.

  @generated @skip
  Scenario: Get a list of logs returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Logs" API
    And new "ListLogs" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
