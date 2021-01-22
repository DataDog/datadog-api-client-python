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

  Scenario: Get a quick list of logs returns "OK" response
    Given operation "ListLogsGet" enabled
    And new "ListLogsGet" request
    And request contains "filter[query]" parameter with value "datadog-agent"
    And request contains "filter[index]" parameter with value "main"
    And request contains "filter[from]" parameter with value "2020-09-17T11:48:36+01:00"
    And request contains "filter[to]" parameter with value "2020-09-17T12:48:36+01:00"
    And request contains "page[limit]" parameter with value 5
    When the request is sent
    Then the response status is 200 OK

  Scenario: Get a list of logs returns "OK" response
    Given operation "ListLogs" enabled
    And new "ListLogs" request
    And body {"filter": {"query": "datadog-agent", "indexes": ["main"], "from": "2020-09-17T11:48:36+01:00", "to": "2020-09-17T12:48:36+01:00"}, "sort": "timestamp", "page": {"limit": 5}}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Aggregate events returns "OK" response
    Given new "AggregateLogs" request
    And body {"compute": [{"aggregation": "count", "interval": "300", "metric": "test.aggregation.{{ unique }}", "type": "timeseries"}], "filter": {"from": "1600348573", "indexes": ["main"], "query": "datadog-agent", "to": "1600348600"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a list of logs returns "Bad Request" response
    Given operation "ListLogs" enabled
    And new "ListLogs" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Aggregate events returns "Bad Request" response
    Given new "AggregateLogs" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get a quick list of logs returns "Bad Request" response
    Given operation "ListLogsGet" enabled
    And new "ListLogsGet" request
    When the request is sent
    Then the response status is 400 Bad Request
