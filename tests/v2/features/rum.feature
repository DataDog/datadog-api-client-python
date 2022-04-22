@endpoint(rum) @endpoint(rum-v2)
Feature: RUM
  Search or aggregate your RUM events over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUM" API

  @generated @skip @team:DataDog/rum-back
  Scenario: Aggregate RUM events returns "Bad Request" response
    Given new "AggregateRUMEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "interval": "5m", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "group_by": [{"facet": "@view.time_spent", "histogram": {"interval": 10, "max": 100, "min": 50}, "limit": 10, "sort": {"aggregation": "count", "order": "asc"}, "total": false}], "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-back
  Scenario: Aggregate RUM events returns "OK" response
    Given new "AggregateRUMEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "metric": "@view.time_spent", "type": "total"}], "filter": {"from": "now-15m", "query": "@type:view AND @session.type:user", "to": "now"}, "group_by": [{"facet": "@view.time_spent", "limit": 10, "total": false}], "options": {"timezone": "GMT"}, "page": { "limit": 25}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-back
  Scenario: Get a list of RUM events returns "Bad Request" response
    Given new "ListRUMEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-back
  Scenario: Get a list of RUM events returns "OK" response
    Given new "ListRUMEvents" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/rum-back @with-pagination
  Scenario: Get a list of RUM events returns "OK" response with pagination
    Given new "ListRUMEvents" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/rum-back
  Scenario: Search RUM events returns "Bad Request" response
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-back
  Scenario: Search RUM events returns "OK" response
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"time_offset": 0, "timezone": "GMT"}, "page": {"limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/rum-back @with-pagination
  Scenario: Search RUM events returns "OK" response with pagination
    Given new "SearchRUMEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@type:session AND @session.type:user", "to": "now"}, "options": {"time_offset": 0, "timezone": "GMT"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items
