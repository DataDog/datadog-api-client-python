@endpoint(monitors) @endpoint(monitors-v1)
Feature: Monitors
  [Monitors](https://docs.datadoghq.com/monitors) allow you to watch a
  metric or check that you care about and notifies your team when a defined
  threshold has exceeded.  For more information, see [Creating
  Monitors](https://docs.datadoghq.com/monitors/create/types/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Monitors" API

  @generated @skip @team:DataDog/monitor-app
  Scenario: Check if a monitor can be deleted returns "Bad Request" response
    Given new "CheckCanDeleteMonitor" request
    And request contains "monitor_ids" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/monitor-app
  Scenario: Check if a monitor can be deleted returns "Deletion conflict error" response
    Given new "CheckCanDeleteMonitor" request
    And request contains "monitor_ids" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Deletion conflict error

  @team:DataDog/monitor-app
  Scenario: Check if a monitor can be deleted returns "OK" response
    Given there is a valid "monitor" in the system
    And new "CheckCanDeleteMonitor" request
    And request contains "monitor_ids" parameter with value [{{monitor.id}}]
    When the request is sent
    Then the response status is 200 OK
    And the response "data.ok[0]" has the same value as "monitor.id"

  @team:DataDog/monitor-app
  Scenario: Create a RUM formula and functions monitor returns "OK" response
    Given new "CreateMonitor" request
    And body with value {"name": "{{ unique }}","type": "rum alert","query": "formula(\"query2 / query1 * 100\").last(\"15m\") >= 0.8","message": "some message Notify: @hipchat-channel", "tags": ["test:{{ unique_lower_alnum }}", "env:ci"],"priority": 3,"options":{"thresholds":{"critical":0.8},"variables":[{"data_source": "rum","name": "query2","search": {"query": ""},"indexes": ["*"],"compute": {"aggregation": "count"},"group_by": []}, {"data_source": "rum","name": "query1","search": {"query": "status:error"},"indexes": ["*"],"compute": {"aggregation": "count"},"group_by": []}]}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "rum alert"

  @team:DataDog/monitor-app
  Scenario: Create a ci-pipelines formula and functions monitor returns "OK" response
    Given new "CreateMonitor" request
    And body with value {"name": "{{ unique }}","type": "ci-pipelines alert","query": "formula(\"query1 / query2 * 100\").last(\"15m\") >= 0.8","message": "some message Notify: @hipchat-channel","tags": ["test:{{ unique_lower_alnum }}", "env:ci"],"priority": 3,"options": {"thresholds": {"critical": 0.8},"variables": [{"data_source": "ci_pipelines","name": "query1","search": {"query": "@ci.status:error"},"indexes": ["*"],"compute": {"aggregation": "count"},"group_by": []},{"data_source": "ci_pipelines","name": "query2","search": {"query": ""},"indexes": ["*"],"compute": {"aggregation": "count"},"group_by": []}]}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "ci-pipelines alert"
    And the response "query" is equal to "formula(\"query1 / query2 * 100\").last(\"15m\") >= 0.8"

  @team:DataDog/monitor-app
  Scenario: Create a ci-pipelines monitor returns "OK" response
    Given new "CreateMonitor" request
    And body with value {"name": "{{ unique }}","type": "ci-pipelines alert","query": "ci-pipelines(\"ci_level:pipeline @git.branch:staging* @ci.status:error\").rollup(\"count\").by(\"@git.branch,@ci.pipeline.name\").last(\"5m\") >= 1","message": "some message Notify: @hipchat-channel",	"tags": ["test:{{ unique_lower_alnum }}", "env:ci"],"priority": 3,"options":{"thresholds":{"critical":1}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "ci-pipelines alert"
    And the response "query" is equal to "ci-pipelines(\"ci_level:pipeline @git.branch:staging* @ci.status:error\").rollup(\"count\").by(\"@git.branch,@ci.pipeline.name\").last(\"5m\") >= 1"

  @team:DataDog/monitor-app
  Scenario: Create a ci-tests formula and functions monitor returns "OK" response
    Given new "CreateMonitor" request
    And body with value {"name": "{{ unique }}","type": "ci-tests alert","query": "formula(\"query1 / query2 * 100\").last(\"15m\") >= 0.8","message": "some message Notify: @hipchat-channel","tags": ["test:{{ unique_lower_alnum }}", "env:ci"],"priority": 3,"options": {"thresholds": {"critical": 0.8},"variables": [{"data_source": "ci_tests","name": "query1","search": {"query": "@test.status:fail"},"indexes": ["*"],"compute": {"aggregation": "count"},"group_by": []},{"data_source": "ci_tests","name": "query2","search": {"query": ""},"indexes": ["*"],"compute": {"aggregation": "count"},"group_by": []}]}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "ci-tests alert"
    And the response "query" is equal to "formula(\"query1 / query2 * 100\").last(\"15m\") >= 0.8"

  @team:DataDog/monitor-app
  Scenario: Create a ci-tests monitor returns "OK" response
    Given new "CreateMonitor" request
    And body with value {"name": "{{ unique }}","type": "ci-tests alert","query": "ci-tests(\"type:test @git.branch:staging* @test.status:fail\").rollup(\"count\").by(\"@test.name\").last(\"5m\") >= 1","message": "some message Notify: @hipchat-channel", "tags": ["test:{{ unique_lower_alnum }}", "env:ci"],"priority": 3,"options":{"thresholds":{"critical":1}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "ci-tests alert"
    And the response "query" is equal to "ci-tests(\"type:test @git.branch:staging* @test.status:fail\").rollup(\"count\").by(\"@test.name\").last(\"5m\") >= 1"

  @team:DataDog/monitor-app
  Scenario: Create a metric monitor returns "OK" response
    Given new "CreateMonitor" request
    And body with value {"name": "{{ unique }}", "type": "metric alert", "query": "avg(current_1mo):avg:system.load.5{*} > 0.5", "message": "some message Notify: @hipchat-channel", "options":{"thresholds":{"critical":0.5}, "scheduling_options":{"evaluation_window":{"day_starts":"04:00", "month_starts":1}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "query" is equal to "avg(current_1mo):avg:system.load.5{*} > 0.5"

  @team:DataDog/monitor-app
  Scenario: Create a metric monitor with a custom schedule returns "OK" response
    Given new "CreateMonitor" request
    And body with value {"message":"some message Notify: @hipchat-channel","name":"{{ unique }}","query":"avg(current_1mo):avg:system.load.5{*} > 0.5","tags":[],"options":{"thresholds":{"critical":0.5},"notify_audit":false,"include_tags":false,"scheduling_options":{"evaluation_window":{"day_starts":"04:00", "month_starts":1},"custom_schedule":{"recurrences":[{"rrule":"FREQ=DAILY;INTERVAL=1","timezone":"America/Los_Angeles","start":"2024-10-26T09:13:00"}]}}},"type":"query alert"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "options.scheduling_options.custom_schedule.recurrences[0].rrule" is equal to "FREQ=DAILY;INTERVAL=1"
    And the response "options.scheduling_options.custom_schedule.recurrences[0].start" is equal to "2024-10-26T09:13:00"
    And the response "options.scheduling_options.custom_schedule.recurrences[0].timezone" is equal to "America/Los_Angeles"

  @team:DataDog/monitor-app
  Scenario: Create a monitor returns "Bad Request" response
    Given new "CreateMonitor" request
    And body with value {"type": "log alert", "query": "query"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Create a monitor returns "OK" response
    Given there is a valid "role" in the system
    And new "CreateMonitor" request
    And body with value {"name": "{{ unique }}", "type": "log alert", "query": "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source\").last(\"5m\") > 2", "message": "some message Notify: @hipchat-channel", "tags": ["test:{{ unique_lower_alnum }}", "env:ci"], "priority": 3, "restricted_roles": ["{{ role.data.id }}"]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log alert"
    And the response "query" is equal to "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source\").last(\"5m\") > 2"

  @team:DataDog/monitor-app
  Scenario: Create an Error Tracking monitor returns "OK" response
    Given new "CreateMonitor" request
    And body from file "monitor_error_tracking_alert_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "error-tracking alert"
    And the response "query" is equal to "error-tracking-rum(\"service:foo AND @error.source:source\").rollup(\"count\").by(\"@issue.id\").last(\"1h\") >= 1"

  @generated @skip @team:DataDog/monitor-app
  Scenario: Delete a monitor returns "Bad Request" response
    Given new "DeleteMonitor" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Delete a monitor returns "Item not found error" response
    Given new "DeleteMonitor" request
    And request contains "monitor_id" parameter with value 0
    When the request is sent
    Then the response status is 404 Item not found error

  @team:DataDog/monitor-app
  Scenario: Delete a monitor returns "OK" response
    Given there is a valid "monitor" in the system
    And new "DeleteMonitor" request
    And request contains "monitor_id" parameter from "monitor.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "deleted_monitor_id" has the same value as "monitor.id"

  @generated @skip @team:DataDog/monitor-app
  Scenario: Edit a monitor returns "Bad Request" response
    Given new "UpdateMonitor" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    And body with value {"options": {"evaluation_delay": null, "include_tags": true, "min_failure_duration": 0, "min_location_failed": 1, "new_group_delay": null, "new_host_delay": 300, "no_data_timeframe": null, "notification_preset_name": "show_all", "notify_audit": false, "notify_by": [], "on_missing_data": "default", "renotify_interval": null, "renotify_occurrences": null, "renotify_statuses": ["alert"], "scheduling_options": {"custom_schedule": {"recurrences": [{"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR", "start": "2023-08-31T16:30:00", "timezone": "Europe/Paris"}]}, "evaluation_window": {"day_starts": "04:00", "hour_starts": 0, "month_starts": 1}}, "synthetics_check_id": null, "threshold_windows": {"recovery_window": null, "trigger_window": null}, "thresholds": {"critical_recovery": null, "ok": null, "unknown": null, "warning": null, "warning_recovery": null}, "timeout_h": null, "variables": [{"compute": {"aggregation": "avg", "interval": 60000, "metric": "@duration"}, "data_source": "rum", "group_by": [{"facet": "status", "limit": 10, "sort": {"aggregation": "avg", "order": "desc"}}], "indexes": ["days-3", "days-7"], "name": "query_errors", "search": {"query": "service:query"}}]}, "restricted_roles": [], "tags": [], "type": "query alert"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Edit a monitor returns "Monitor Not Found error" response
    Given new "UpdateMonitor" request
    And request contains "monitor_id" parameter with value 0
    And body with value {"name": "updated", "options": {"evaluation_delay": null, "new_group_delay": 600, "new_host_delay":null, "renotify_interval":null, "thresholds": {"critical":2, "warning": null}, "timeout_h": null}}
    When the request is sent
    Then the response status is 404 Monitor Not Found error

  @team:DataDog/monitor-app
  Scenario: Edit a monitor returns "OK" response
    Given there is a valid "monitor" in the system
    And new "UpdateMonitor" request
    And request contains "monitor_id" parameter from "monitor.id"
    And body with value {"name": "{{ monitor.name }}-updated", "options": {"evaluation_delay": null, "new_group_delay": 600, "new_host_delay":null, "renotify_interval":null, "thresholds": {"critical":2, "warning": null}, "timeout_h": null}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ monitor.name }}-updated"

  @generated @skip @team:DataDog/monitor-app
  Scenario: Get a monitor's details returns "Bad Request" response
    Given new "GetMonitor" request
    And request contains "monitor_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Get a monitor's details returns "Monitor Not Found error" response
    Given new "GetMonitor" request
    And request contains "monitor_id" parameter with value 12345
    When the request is sent
    Then the response status is 404 Monitor Not Found error

  @team:DataDog/monitor-app
  Scenario: Get a monitor's details returns "OK" response
    Given there is a valid "monitor" in the system
    And new "GetMonitor" request
    And request contains "monitor_id" parameter from "monitor.id"
    And request contains "with_downtimes" parameter with value true
    When the request is sent
    Then the response status is 200 OK
    And the response "id" has the same value as "monitor.id"

  @replay-only @team:DataDog/monitor-app
  Scenario: Get a monitor's details with downtime returns "OK" response
    Given there is a valid "monitor" in the system
    And there is a valid "downtime" for a "monitor" in the system
    And new "GetMonitor" request
    And request contains "monitor_id" parameter from "monitor.id"
    And request contains "with_downtimes" parameter with value true
    When the request is sent
    Then the response status is 200 OK
    And the response "id" has the same value as "monitor.id"
    And the response "matching_downtimes" has length 1
    And the response "matching_downtimes[0].id" has the same value as "downtime_monitor.id"

  @team:DataDog/monitor-app
  Scenario: Get a synthetics monitor's details
    Given there is a valid "synthetics_api_test" in the system
    And new "GetMonitor" request
    And request contains "monitor_id" parameter from "synthetics_api_test.monitor_id"
    When the request is sent
    Then the response status is 200 OK
    And the response "options.synthetics_check_id" has the same value as "synthetics_api_test.public_id"

  @team:DataDog/monitor-app
  Scenario: Get all monitor details returns "Bad Request" response
    Given new "ListMonitors" request
    And request contains "group_states" parameter with value "notagroupstate"
    When the request is sent
    Then the response status is 400 Bad Request

  @integration-only @team:DataDog/monitor-app
  Scenario: Get all monitor details returns "OK" response
    Given new "ListMonitors" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/monitor-app @with-pagination
  Scenario: Get all monitor details returns "OK" response with pagination
    Given new "ListMonitors" request
    And request contains "page_size" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @skip @team:DataDog/monitor-app
  Scenario: Get all monitor details with tags
    Given there is a valid "monitor" in the system
    And new "ListMonitors" request
    And request contains "tags" parameter with value "test:{{ unique_lower_alnum }}"
    And request contains "page_size" parameter with value 1
    When the request is sent
    Then the response status is 200 OK
    And the response "[0].id" has the same value as "monitor.id"

  @team:DataDog/monitor-app
  Scenario: Monitors group search returns "Bad Request" response
    Given new "SearchMonitorGroups" request
    And request contains "query" parameter with value "status:notastatus"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Monitors group search returns "OK" response
    Given new "SearchMonitorGroups" request
    When the request is sent
    Then the response status is 200 OK
    And the response "metadata.page" is equal to 0

  @team:DataDog/monitor-app
  Scenario: Monitors search returns "Bad Request" response
    Given new "SearchMonitors" request
    And request contains "query" parameter with value "status:notastatus"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/monitor-app
  Scenario: Monitors search returns "OK" response
    Given new "SearchMonitors" request
    When the request is sent
    Then the response status is 200 OK
    And the response "metadata.page" is equal to 0

  @team:DataDog/monitor-app
  Scenario: Validate a monitor returns "Invalid JSON" response
    Given new "ValidateMonitor" request
    And body with value {"type": "log alert", "query": "query"}
    When the request is sent
    Then the response status is 400 Invalid JSON

  @team:DataDog/monitor-app
  Scenario: Validate a monitor returns "OK" response
    Given new "ValidateMonitor" request
    And body from file "monitor_payload.json"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/monitor-app
  Scenario: Validate a multi-alert monitor returns "OK" response
    Given new "ValidateMonitor" request
    And body from file "multi_alert_monitor_payload.json"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/monitor-app
  Scenario: Validate an existing monitor returns "Invalid JSON" response
    Given there is a valid "monitor" in the system
    And new "ValidateExistingMonitor" request
    And request contains "monitor_id" parameter from "monitor.id"
    And body with value {"type": "log alert", "query": "query"}
    When the request is sent
    Then the response status is 400 Invalid JSON

  @skip @team:DataDog/monitor-app
  Scenario: Validate an existing monitor returns "Item not found error" response
    Given new "ValidateExistingMonitor" request
    And request contains "monitor_id" parameter with value 0
    When the request is sent
    Then the response status is 404 Item not found error

  @team:DataDog/monitor-app
  Scenario: Validate an existing monitor returns "OK" response
    Given there is a valid "monitor" in the system
    And new "ValidateExistingMonitor" request
    And request contains "monitor_id" parameter from "monitor.id"
    And body from file "monitor_payload.json"
    When the request is sent
    Then the response status is 200 OK
