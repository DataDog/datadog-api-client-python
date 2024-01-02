@endpoint(downtimes) @endpoint(downtimes-v2)
Feature: Downtimes
  **Note**: Downtime V2 is currently in private beta. To request access,
  contact [Datadog support](https://docs.datadoghq.com/help/).
  [Downtiming](https://docs.datadoghq.com/monitors/notify/downtimes) gives
  you greater control over monitor notifications by allowing you to globally
  exclude scopes from alerting. Downtime settings, which can be scheduled
  with start and end times, prevent all alerting related to specified
  Datadog tags.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Downtimes" API

  @skip-validation @team:DataDog/monitor-app
  Scenario: Cancel a downtime returns "Downtime not found" response
    Given new "CancelDowntime" request
    And request contains "downtime_id" parameter with value "00000000-0000-1234-0000-000000000000"
    When the request is sent
    Then the response status is 404 Downtime not found

  @team:DataDog/monitor-app
  Scenario: Cancel a downtime returns "OK" response
    Given there is a valid "downtime_v2" in the system
    And new "CancelDowntime" request
    And request contains "downtime_id" parameter from "downtime_v2.data.id"
    When the request is sent
    Then the response status is 204 OK

  @skip-validation @team:DataDog/monitor-app
  Scenario: Get a downtime returns "Bad Request" response
    Given new "GetDowntime" request
    And request contains "downtime_id" parameter with value "INVALID_UUID_LENGTH"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/monitor-app
  Scenario: Get a downtime returns "Not Found" response
    Given new "GetDowntime" request
    And request contains "downtime_id" parameter with value "00000000-0000-1234-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/monitor-app
  Scenario: Get a downtime returns "OK" response
    Given there is a valid "downtime_v2" in the system
    And new "GetDowntime" request
    And request contains "downtime_id" parameter from "downtime_v2.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.message" is equal to "test message"

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get active downtimes for a monitor returns "Monitor Not Found error" response
    Given new "ListMonitorDowntimes" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Monitor Not Found error

  @replay-only @team:DataDog/monitor-app
  Scenario: Get active downtimes for a monitor returns "OK" response
    Given new "ListMonitorDowntimes" request
    And request contains "monitor_id" parameter with value 35534610
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data" has item with field "id" with value "aeefc6a8-15d8-11ee-a8ef-da7ad0900002"

  @generated @skip @team:DataDog/monitor-app @with-pagination
  Scenario: Get active downtimes for a monitor returns "OK" response with pagination
    Given new "ListMonitorDowntimes" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request with pagination is sent
    Then the response status is 200 OK

  @team:DataDog/monitor-app
  Scenario: Get all downtimes for a monitor returns "Monitor Not Found error" response
    Given new "ListMonitorDowntimes" request
    And request contains "monitor_id" parameter with value 0
    When the request is sent
    Then the response status is 404 Monitor Not Found error

  @replay-only @team:DataDog/monitor-app
  Scenario: Get all downtimes returns "OK" response
    Given new "ListDowntimes" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "1dcb33f8-b23a-11ed-ae77-da7ad0900002"

  @replay-only @skip-validation @team:DataDog/monitor-app @with-pagination
  Scenario: Get all downtimes returns "OK" response with pagination
    Given new "ListDowntimes" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @skip-validation @team:DataDog/monitor-app
  Scenario: Schedule a downtime returns "Bad Request" response
    Given new "CreateDowntime" request
    And body with value { "data": { "attributes": { "monitor_identifier": { "monitor_tags": ["cat:hat"] }, "scope": "BAD_SCOPE_MISSING_KEY_VALUE_FORMAT", "schedule": {"start": null } }, "type": "downtime" } }
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime returns "OK" response
    Given new "CreateDowntime" request
    And body with value { "data": { "attributes": { "message": "dark forest", "monitor_identifier": { "monitor_tags": ["cat:hat"] }, "scope": "test:{{ unique_lower_alnum }}", "schedule": {"start": null } }, "type": "downtime" } }
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.message" is equal to "dark forest"

  @skip-java @skip-python @skip-ruby @skip-typescript @skip-validation @team:DataDog/monitor-app
  Scenario: Update a downtime returns "Bad Request" response
    Given there is a valid "downtime_v2" in the system
    And new "UpdateDowntime" request
    And request contains "downtime_id" parameter from "downtime_v2.data.id"
    And body with value {"data": {"attributes": {"invalid_field": "sophon"}, "id": "{{ downtime_v2.data.id }}", "type": "downtime"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/monitor-app
  Scenario: Update a downtime returns "Downtime not found" response
    Given new "UpdateDowntime" request
    And request contains "downtime_id" parameter with value "00000000-0000-1234-0000-000000000000"
    And body with value {"data": {"attributes": {"message": "test msg"}, "id": "00000000-0000-1234-0000-000000000000", "type": "downtime"}}
    When the request is sent
    Then the response status is 404 Downtime not found

  @team:DataDog/monitor-app
  Scenario: Update a downtime returns "OK" response
    Given there is a valid "downtime_v2" in the system
    And new "UpdateDowntime" request
    And request contains "downtime_id" parameter from "downtime_v2.data.id"
    And body with value {"data": {"attributes": {"message": "light speed"}, "id": "{{ downtime_v2.data.id }}", "type": "downtime"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.message" is equal to "light speed"
