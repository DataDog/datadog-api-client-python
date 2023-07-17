@endpoint(spans) @endpoint(spans-v2)
Feature: Spans
  Search and aggregate your spans from your Datadog platform over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Spans" API

  @skip @team:DataDog/apm
  Scenario: Aggregate spans returns "Bad Request" response
    Given new "AggregateSpans" request
    And body with value {"compute": [{"aggregation": "pc90", "interval": "5m", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "service:web* AND @http.status_code:[200 TO 299]", "to": "now"}, "group_by": [{"facet": "host", "histogram": {"interval": 10, "max": 100, "min": 50}, "limit": 10, "sort": {"aggregation": "count", "order": "asc"}, "total": false}], "options": {"timezone": "GMT"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/apm
  Scenario: Aggregate spans returns "OK" response
    Given new "AggregateSpans" request
    And body with value {"data":{"attributes": {"compute": [{"aggregation": "count", "interval": "5m", "type": "timeseries"}],"filter": {"from": "now-15m", "query": "*", "to": "now"}},"type":"aggregate_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.status" is equal to "done"

  @generated @skip @team:DataDog/apm
  Scenario: Get a list of spans returns "Bad Request." response
    Given new "ListSpansGet" request
    When the request is sent
    Then the response status is 400 Bad Request.

  @replay-only @team:DataDog/apm
  Scenario: Get a list of spans returns "OK" response
    Given new "ListSpansGet" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "spans"

  @replay-only @skip-validation @team:DataDog/apm @with-pagination
  Scenario: Get a list of spans returns "OK" response with pagination
    Given new "ListSpansGet" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/apm
  Scenario: Get a list of spans returns "Unprocessable Entity." response
    Given new "ListSpansGet" request
    And request contains "filter[from]" parameter with value "now"
    And request contains "filter[to]" parameter with value "now-1m"
    When the request is sent
    Then the response status is 422 Unprocessable Entity.

  @skip @team:DataDog/apm
  Scenario: Search spans returns "Bad Request." response
    Given new "ListSpans" request
    And body with value {"filter": {"from": "now-15m", "query": "service:web*", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/apm
  Scenario: Search spans returns "OK" response
    Given new "ListSpans" request
    And body with value {"data": {"attributes": {"filter": {"from": "now-15m", "query": "*", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 25}, "sort": "timestamp"}, "type": "search_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "spans"

  @replay-only @skip-validation @team:DataDog/apm @with-pagination
  Scenario: Search spans returns "OK" response with pagination
    Given new "ListSpans" request
    And body with value {"data": {"attributes": {"filter": {"from": "now-15m", "query": "service:python*", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 2}, "sort": "timestamp"}, "type": "search_request"}}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/apm
  Scenario: Search spans returns "Unprocessable Entity." response
    Given new "ListSpans" request
    And body with value {"data": {"attributes": {"filter": {"from": "now", "query": "service:web* AND @http.status_code:[200 TO 299]", "to": "now-15m"}, "options": {"timezone": "GMT"}, "page": {"limit": 10}, "sort": "timestamp"}, "type": "search_request"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity.
