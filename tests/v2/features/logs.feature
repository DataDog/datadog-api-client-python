@endpoint(logs)
Feature: Logs
  Search your logs in the Datadog platform over HTTP.  [See API version
  1](/api/v1/logs/) for sending logs.

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
    Given operation "AggregateLogs" enabled
    And new "AggregateLogs" request
    And body {"compute": [{"aggregation": "count", "interval": "300", "metric": "test.aggregation.{{ unique }}", "type": "timeseries"}], "filter": {"from": "1600348573", "indexes": ["main"], "query": "datadog-agent", "to": "1600348600"}}
    When the request is sent
    Then the response status is 200 OK
