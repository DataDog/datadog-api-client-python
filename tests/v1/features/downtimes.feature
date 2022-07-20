@endpoint(downtimes) @endpoint(downtimes-v1)
Feature: Downtimes
  [Downtiming](https://docs.datadoghq.com/monitors/notify/downtimes) gives
  you greater control over monitor notifications by allowing you to globally
  exclude scopes from alerting. Downtime settings, which can be scheduled
  with start and end times, prevent all alerting related to specified
  Datadog tags.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Downtimes" API

  @team:DataDog/monitor-app
  Scenario: Cancel a downtime returns "Downtime not found" response
    Given new "CancelDowntime" request
    And request contains "downtime_id" parameter with value 0
    When the request is sent
    Then the response status is 404 Downtime not found

  @team:DataDog/monitor-app
  Scenario: Cancel a downtime returns "OK" response
    Given there is a valid "downtime" in the system
    And new "CancelDowntime" request
    And request contains "downtime_id" parameter from "downtime.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/monitor-app
  Scenario: Cancel downtimes by scope returns "Bad Request" response
    Given new "CancelDowntimesByScope" request
    And body with value {"scope": "host:myserver"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Cancel downtimes by scope returns "Downtimes not found" response
    Given new "CancelDowntimesByScope" request
    And body with value {"scope": "test:{{ unique_lower_alnum }}_invalid"}
    When the request is sent
    Then the response status is 404 Downtimes not found

  @team:DataDog/monitor-app
  Scenario: Cancel downtimes by scope returns "OK" response
    Given there is a valid "downtime" in the system
    And new "CancelDowntimesByScope" request
    And body with value {"scope": "{{ downtime.scope[0] }}"}
    When the request is sent
    Then the response status is 200 OK
    And the response "cancelled_ids[0]" has the same value as "downtime.id"

  @team:DataDog/monitor-app
  Scenario: Get a downtime returns "Downtime not found" response
    Given new "GetDowntime" request
    And request contains "downtime_id" parameter with value 0
    When the request is sent
    Then the response status is 404 Downtime not found

  @team:DataDog/monitor-app
  Scenario: Get a downtime returns "OK" response
    Given there is a valid "downtime" in the system
    And new "GetDowntime" request
    And request contains "downtime_id" parameter from "downtime.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "id" has the same value as "downtime.id"
    And the response "message" has the same value as "downtime.message"

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get all downtimes for a monitor returns "Bad Request" response
    Given new "ListMonitorDowntimes" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get all downtimes for a monitor returns "Monitor Not Found error" response
    Given new "ListMonitorDowntimes" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Monitor Not Found error

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get all downtimes for a monitor returns "OK" response
    Given new "ListMonitorDowntimes" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get all downtimes returns "OK" response
    Given new "ListDowntimes" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime once a year
    Given new "CreateDowntime" request
    And body from file "downtime_recurrence_payload_once_a_year.json"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime returns "Bad Request" response
    Given new "CreateDowntime" request
    And body from file "downtime_with_many_tags_payload.json"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime returns "OK" response
    Given new "CreateDowntime" request
    And body with value {"message": "{{ unique }}", "start": {{ timestamp("now") }}, "timezone": "Etc/UTC", "scope": ["test:{{ unique_lower_alnum }}"], "recurrence": {"type": "weeks", "period": 1, "week_days": ["Mon", "Tue", "Wed", "Thu", "Fri"], "until_date": {{ timestamp("now + 21d")}} }}
    When the request is sent
    Then the response status is 200 OK
    And the response "message" is equal to "{{ unique }}"
    And the response "active" is equal to true

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime until date
    Given new "CreateDowntime" request
    And body from file "downtime_recurrence_payload_until_date.json"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime with invalid type hours
    Given new "CreateDowntime" request
    And body from file "downtime_recurrence_payload_invalid_type_hours.json"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime with invalid weekdays
    Given new "CreateDowntime" request
    And body from file "downtime_recurrence_payload_invalid_weekdays.json"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime with mutually exclusive until occurrences and until date properties
    Given new "CreateDowntime" request
    And body from file "downtime_recurrence_payload_until_occurrences_and_until_date_are_mutually_exclusive.json"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Schedule a downtime with until occurrences
    Given new "CreateDowntime" request
    And body from file "downtime_recurrence_payload_until_occurrences.json"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/monitor-app
  Scenario: Schedule a monitor downtime returns "OK" response
    Given there is a valid "monitor" in the system
    And new "CreateDowntime" request
    And body with value {"message": "{{ unique }}", "start": {{ timestamp("now") }}, "timezone": "Etc/UTC", "scope": ["test:{{ unique_lower_alnum }}"], "monitor_id": {{ monitor.id }}}
    When the request is sent
    Then the response status is 200 OK
    And the response "monitor_id" has the same value as "monitor.id"

  @generated @skip @team:DataDog/monitor-app
  Scenario: Update a downtime returns "Bad Request" response
    Given new "UpdateDowntime" request
    And request contains "downtime_id" parameter from "REPLACE.ME"
    And body with value {"disabled": false, "end": 1412793983, "message": "Message on the downtime", "monitor_id": 123456, "monitor_tags": ["*"], "mute_first_recovery_notification": false, "parent_id": 123, "recurrence": {"period": 1, "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1", "type": "weeks", "until_date": 1447786293, "until_occurrences": 2, "week_days": ["Mon", "Tue"]}, "scope": ["env:staging"], "start": 1412792983, "timezone": "America/New_York"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/monitor-app
  Scenario: Update a downtime returns "Downtime not found" response
    Given new "UpdateDowntime" request
    And request contains "downtime_id" parameter from "REPLACE.ME"
    And body with value {"disabled": false, "end": 1412793983, "message": "Message on the downtime", "monitor_id": 123456, "monitor_tags": ["*"], "mute_first_recovery_notification": false, "parent_id": 123, "recurrence": {"period": 1, "rrule": "FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1", "type": "weeks", "until_date": 1447786293, "until_occurrences": 2, "week_days": ["Mon", "Tue"]}, "scope": ["env:staging"], "start": 1412792983, "timezone": "America/New_York"}
    When the request is sent
    Then the response status is 404 Downtime not found

  @team:DataDog/monitor-app
  Scenario: Update a downtime returns "OK" response
    Given there is a valid "downtime" in the system
    And new "UpdateDowntime" request
    And request contains "downtime_id" parameter from "downtime.id"
    And body with value {"message": "{{ unique}}-updated", "mute_first_recovery_notification": true}
    When the request is sent
    Then the response status is 200 OK
    And the response "message" is equal to "{{ unique }}-updated"
