@endpoint(logs)
Feature: Logs
  Search your logs and send them to your Datadog platform over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Logs" API

  @generated @skip
  Scenario: Aggregate events returns "Bad Request" response
    Given new "AggregateLogs" request
    And body {"compute": [{"aggregation": "pc90", "interval": "5m", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "indexes": ["main", "web"], "query": "service:web* AND @http.status_code:[200 TO 299]", "to": "now"}, "group_by": [{"facet": "host", "histogram": {"interval": 10, "max": 100, "min": 50}, "limit": 10, "missing": null, "sort": {"aggregation": "count", "order": "asc"}, "total": false}], "options": {"timeOffset": null, "timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="}}
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Aggregate events returns "OK" response
    Given new "AggregateLogs" request
    And body {"compute": [{"aggregation": "count", "interval": "300", "metric": "test.aggregation.{{ unique }}", "type": "timeseries"}], "filter": {"from": "1600348573", "indexes": ["main"], "query": "datadog-agent", "to": "1600348600"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a list of logs returns "Bad Request" response
    Given new "ListLogsGet" request
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Get a list of logs returns "OK" response
    Given operation "ListLogs" enabled
    And new "ListLogs" request
    And body {"filter": {"query": "datadog-agent", "indexes": ["main"], "from": "2020-09-17T11:48:36+01:00", "to": "2020-09-17T12:48:36+01:00"}, "sort": "timestamp", "page": {"limit": 5}}
    When the request is sent
    Then the response status is 200 OK

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

  @generated @skip
  Scenario: Search logs returns "Bad Request" response
    Given new "ListLogs" request
    And body {"filter": {"from": "now-15m", "indexes": ["main", "web"], "query": "service:web* AND @http.status_code:[200 TO 299]", "to": "now"}, "options": {"timeOffset": null, "timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": null}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Search logs returns "OK" response
    Given new "ListLogs" request
    And body {"filter": {"from": "now-15m", "indexes": ["main", "web"], "query": "service:web* AND @http.status_code:[200 TO 299]", "to": "now"}, "options": {"timeOffset": null, "timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": null}
    When the request is sent
    Then the response status is 200 OK
