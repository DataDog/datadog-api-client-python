@endpoint(events) @endpoint(events-v2)
Feature: Events
  The events service allows you to programmatically post events to the event
  stream and fetch events from the event stream. Events are limited to 4000
  characters. If an event is sent out with a message containing more than
  4000 characters, only the first 4000 characters are displayed.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Events" API

  @generated @skip @team:DataDog/event-management
  Scenario: Get a list of events returns "Bad Request" response
    Given operation "ListEvents" enabled
    And new "ListEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/event-management
  Scenario: Get a list of events returns "OK" response
    Given operation "ListEvents" enabled
    And new "ListEvents" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/event-management @with-pagination
  Scenario: Get a list of events returns "OK" response with pagination
    Given operation "ListEvents" enabled
    And new "ListEvents" request
    And request contains "filter[from]" parameter with value "now-15m"
    And request contains "filter[to]" parameter with value "now"
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/event-management
  Scenario: Get a quick list of events returns "OK" response
    Given operation "ListEvents" enabled
    And new "ListEvents" request
    And request contains "filter[query]" parameter with value "datadog-agent"
    And request contains "filter[from]" parameter with value "2020-09-17T11:48:36+01:00"
    And request contains "filter[to]" parameter with value "2020-09-17T12:48:36+01:00"
    And request contains "page[limit]" parameter with value 5
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-management
  Scenario: Search events returns "Bad Request" response
    Given operation "SearchEvents" enabled
    And new "SearchEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "service:web* AND @http.status_code:[200 TO 299]", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/event-management
  Scenario: Search events returns "OK" response
    Given operation "SearchEvents" enabled
    And new "SearchEvents" request
    And body with value {"filter": {"query": "datadog-agent", "from": "2020-09-17T11:48:36+01:00", "to": "2020-09-17T12:48:36+01:00"}, "sort": "timestamp", "page": {"limit": 5}}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/event-management @with-pagination
  Scenario: Search events returns "OK" response with pagination
    Given operation "SearchEvents" enabled
    And new "SearchEvents" request
    And body with value {"filter": {"from": "now-15m", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items
