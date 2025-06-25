@endpoint(events) @endpoint(events-v2)
Feature: Events
  The Event Management API allows you to programmatically post events to the
  Events Explorer and fetch events from the Events Explorer. See the [Event
  Management page](https://docs.datadoghq.com/service_management/events/)
  for more information.  **Update to Datadog monitor events
  `aggregation_key` starting March 1, 2025:** The Datadog monitor events
  `aggregation_key` is unique to each Monitor ID. Starting March 1st, this
  key will also include Monitor Group, making it unique per *Monitor ID and
  Monitor Group*. If you're using monitor events `aggregation_key` in
  dashboard queries or the Event API, you must migrate to use `@monitor.id`.
  Reach out to [support](https://www.datadoghq.com/support/) if you have any
  question.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Events" API

  @generated @skip @team:DataDog/event-management
  Scenario: Get a list of events returns "Bad Request" response
    Given new "ListEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/event-management
  Scenario: Get a list of events returns "OK" response
    Given new "ListEvents" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/event-management @with-pagination
  Scenario: Get a list of events returns "OK" response with pagination
    Given new "ListEvents" request
    And request contains "filter[from]" parameter with value "now-15m"
    And request contains "filter[to]" parameter with value "now"
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/event-management
  Scenario: Get a quick list of events returns "OK" response
    Given new "ListEvents" request
    And request contains "filter[query]" parameter with value "datadog-agent"
    And request contains "filter[from]" parameter with value "2020-09-17T11:48:36+01:00"
    And request contains "filter[to]" parameter with value "2020-09-17T12:48:36+01:00"
    And request contains "page[limit]" parameter with value 5
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0

  @team:DataDog/event-management
  Scenario: Post an event returns "Bad request" response
    Given new "CreateEvent" request
    And body with value {"data": {"attributes": {"aggregation_key": "aggregation_key_123", "attributes": {"author": {"name": "example@datadog.com", "type": "user"}, "change_metadata": {"dd": {"team": "datadog_team", "user_email": "datadog@datadog.com", "user_id": "datadog_user_id", "user_name": "datadog_username"}, "resource_link": "datadog.com/feature/fallback_payments_test"}, "changed_resource": {"name": "fallback_payments_test", "type": "feature_flag"}, "impacted_resources": [{"name": "payments_api", "type": "service"}], "new_value": {"enabled": true, "percentage": "50%", "rule": {"datacenter": "devcycle.us1.prod"}}, "prev_value": {"enabled": true, "percentage": "10%", "rule": {"datacenter": "devcycle.us1.prod"}}}, "category": "invalid", "integration_id": "custom-events", "message": "payment_processed feature flag has been enabled", "tags": ["env:api_client_test"], "title": "payment_processed feature flag updated"}, "type": "event"}}
    When the request is sent
    Then the response status is 400 Bad request

  @skip-validation @team:DataDog/event-management
  Scenario: Post an event returns "OK" response
    Given new "CreateEvent" request
    And body with value {"data": {"attributes": {"aggregation_key": "aggregation_key_123", "attributes": {"author": {"name": "example@datadog.com", "type": "user"}, "change_metadata": {"dd": {"team": "datadog_team", "user_email": "datadog@datadog.com", "user_id": "datadog_user_id", "user_name": "datadog_username"}, "resource_link": "datadog.com/feature/fallback_payments_test"}, "changed_resource": {"name": "fallback_payments_test", "type": "feature_flag"}, "impacted_resources": [{"name": "payments_api", "type": "service"}], "new_value": {"enabled": true, "percentage": "50%", "rule": {"datacenter": "devcycle.us1.prod"}}, "prev_value": {"enabled": true, "percentage": "10%", "rule": {"datacenter": "devcycle.us1.prod"}}}, "category": "change", "integration_id": "custom-events", "message": "payment_processed feature flag has been enabled", "tags": ["env:api_client_test"], "title": "payment_processed feature flag updated"}, "type": "event"}}
    When the request is sent
    Then the response status is 202 OK
    And the response "data.type" is equal to "event"
    And the response "data.attributes.attributes.evt" has field "uid"

  @team:DataDog/event-management
  Scenario: Search events returns "Bad Request" response
    Given new "SearchEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "service:web* AND @http.status_code:[200 TO 299]", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/event-management
  Scenario: Search events returns "OK" response
    Given new "SearchEvents" request
    And body with value {"filter": {"query": "datadog-agent", "from": "2020-09-17T11:48:36+01:00", "to": "2020-09-17T12:48:36+01:00"}, "sort": "timestamp", "page": {"limit": 5}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0

  @replay-only @skip-validation @team:DataDog/event-management @with-pagination
  Scenario: Search events returns "OK" response with pagination
    Given new "SearchEvents" request
    And body with value {"filter": {"from": "now-15m", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items
