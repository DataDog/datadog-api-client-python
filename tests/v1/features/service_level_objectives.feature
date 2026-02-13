@endpoint(service-level-objectives) @endpoint(service-level-objectives-v1)
Feature: Service Level Objectives
  [Service Level Objectives](https://docs.datadoghq.com/monitors/service_lev
  el_objectives/#configuration) (or SLOs) are a key part of the site
  reliability engineering toolkit. SLOs provide a framework for defining
  clear targets around application performance, which ultimately help teams
  provide a consistent customer experience, balance feature development with
  platform stability, and improve communication with internal and external
  users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ServiceLevelObjectives" API

  @generated @skip @team:DataDog/slo-app
  Scenario: Bulk Delete SLO Timeframes returns "Bad Request" response
    Given new "DeleteSLOTimeframeInBulk" request
    And body with value {"id1": ["7d", "30d"], "id2": ["7d", "30d"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Bulk Delete SLO Timeframes returns "OK" response
    Given new "DeleteSLOTimeframeInBulk" request
    And body with value {"id1": ["7d", "30d"], "id2": ["7d", "30d"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/slo-app
  Scenario: Check if SLOs can be safely deleted returns "Bad Request" response
    Given new "CheckCanDeleteSLO" request
    And request contains "ids" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Check if SLOs can be safely deleted returns "Conflict" response
    Given new "CheckCanDeleteSLO" request
    And request contains "ids" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/slo-app
  Scenario: Check if SLOs can be safely deleted returns "OK" response
    Given new "CheckCanDeleteSLO" request
    And request contains "ids" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/slo-app
  Scenario: Create a new metric SLO object using sli_specification returns "OK" response
    Given new "CreateSLO" request
    And body with value {"type":"metric","description":"Metric SLO using sli_specification","name":"{{ unique }}","sli_specification":{"count":{"good_events_formula":{"formula":"query1 - query2"},"total_events_formula":{"formula":"query1"},"queries":[{"data_source":"metrics","name":"query1","query":"sum:httpservice.hits{*}.as_count()"},{"data_source":"metrics","name":"query2","query":"sum:httpservice.errors{*}.as_count()"}]}},"tags":["env:prod","type:count"],"thresholds":[{"target":99.0,"target_display":"99.0","timeframe":"7d","warning":99.5,"warning_display":"99.5"}],"timeframe":"7d","target_threshold":99.0,"warning_threshold":99.5}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].timeframe" is equal to "7d"
    And the response "data[0].target_threshold" is equal to 99.0
    And the response "data[0].warning_threshold" is equal to 99.5
    And the response "data[0]" has field "sli_specification"
    And the response "data[0].sli_specification" has field "count"
    And the response "data[0].sli_specification.count" has field "good_events_formula"
    And the response "data[0].sli_specification.count" has field "total_events_formula"
    And the response "data[0].sli_specification.count" has field "queries"
    And the response "data[0].sli_specification.count.queries" has length 2
    And the response "data[0]" has field "query"

  @team:DataDog/slo-app
  Scenario: Create a time-slice SLO object returns "OK" response
    Given new "CreateSLO" request
    And body with value {"type":"time_slice","description":"string","name":"{{ unique }}","sli_specification":{"time_slice":{"query":{"formulas":[{"formula":"query1"}],"queries":[{"data_source":"metrics","name":"query1","query":"trace.servlet.request{env:prod}"}]},"comparator":">","threshold":5}},"tags":["env:prod"],"thresholds":[{"target":97.0,"target_display":"97.0","timeframe":"7d","warning":98,"warning_display":"98.0"}],"timeframe":"7d","target_threshold":97.0,"warning_threshold":98}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].timeframe" is equal to "7d"
    And the response "data[0].target_threshold" is equal to 97.0
    And the response "data[0].warning_threshold" is equal to 98.0

  @team:DataDog/slo-app
  Scenario: Create an SLO object returns "Bad Request" response
    Given new "CreateSLO" request
    And body with value {"type":"monitor","name":"{{ unique }}","thresholds":[{"target":95.0,"target_display":"95.0","timeframe":"7d","warning":98,"warning_display":"98.0"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/slo-app
  Scenario: Create an SLO object returns "OK" response
    Given new "CreateSLO" request
    And body with value {"type":"metric","description":"string","groups":["env:test","role:mysql"],"monitor_ids":[],"name":"{{ unique }}","query":{"denominator":"sum:httpservice.hits{!code:3xx}.as_count()","numerator":"sum:httpservice.hits{code:2xx}.as_count()"},"tags":["env:prod","app:core"],"thresholds":[{"target":97.0,"target_display":"97.0","timeframe":"7d","warning":98,"warning_display":"98.0"}],"timeframe":"7d","target_threshold":97.0,"warning_threshold":98}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].timeframe" is equal to "7d"
    And the response "data[0].target_threshold" is equal to 97.0
    And the response "data[0].warning_threshold" is equal to 98.0

  @generated @skip @team:DataDog/slo-app
  Scenario: Delete an SLO returns "Conflict" response
    Given new "DeleteSLO" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/slo-app
  Scenario: Delete an SLO returns "Not found" response
    Given new "DeleteSLO" request
    And request contains "slo_id" parameter with value "{{ unique_lower_alnum }}"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/slo-app
  Scenario: Delete an SLO returns "OK" response
    Given there is a valid "slo" in the system
    And new "DeleteSLO" request
    And request contains "slo_id" parameter from "slo.data[0].id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0]" has the same value as "slo.data[0].id"

  @generated @skip @team:DataDog/slo-app
  Scenario: Get Corrections For an SLO returns "Bad Request" response
    Given new "GetSLOCorrections" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Get Corrections For an SLO returns "Not Found" response
    Given new "GetSLOCorrections" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/slo-app
  Scenario: Get Corrections For an SLO returns "OK" response
    Given there is a valid "slo" in the system
    And there is a valid "correction" for "slo"
    And new "GetSLOCorrections" request
    And request contains "slo_id" parameter from "slo.data[0].id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1

  @generated @skip @team:DataDog/slo-app
  Scenario: Get all SLOs returns "Bad Request" response
    Given new "ListSLOs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Get all SLOs returns "Not Found" response
    Given new "ListSLOs" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/slo-app
  Scenario: Get all SLOs returns "OK" response
    Given there is a valid "slo" in the system
    And new "ListSLOs" request
    And request contains "ids" parameter from "slo.data[0].id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].id" has the same value as "slo.data[0].id"

  @replay-only @skip-validation @team:DataDog/slo-app @with-pagination
  Scenario: Get all SLOs returns "OK" response with pagination
    Given new "ListSLOs" request
    And request contains "limit" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/slo-app
  Scenario: Get an SLO's details returns "Not found" response
    Given new "GetSLO" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/slo-app
  Scenario: Get an SLO's details returns "OK" response
    Given there is a valid "slo" in the system
    And new "GetSLO" request
    And request contains "slo_id" parameter from "slo.data[0].id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "metric"

  @generated @skip @team:DataDog/slo-app
  Scenario: Get an SLO's history returns "Bad Request" response
    Given new "GetSLOHistory" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    And request contains "from_ts" parameter from "REPLACE.ME"
    And request contains "to_ts" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Get an SLO's history returns "Not Found" response
    Given new "GetSLOHistory" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    And request contains "from_ts" parameter from "REPLACE.ME"
    And request contains "to_ts" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/slo-app
  Scenario: Get an SLO's history returns "OK" response
    Given there is a valid "slo" in the system
    And new "GetSLOHistory" request
    And request contains "slo_id" parameter from "slo.data[0].id"
    And request contains "from_ts" parameter with value {{ timestamp("now - 1d") }}
    And request contains "to_ts" parameter with value {{ timestamp("now") }}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.series.res_type" is equal to "time_series"

  @generated @skip @team:DataDog/slo-app
  Scenario: Search for SLOs returns "Bad Request" response
    Given new "SearchSLO" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/slo-app
  Scenario: Search for SLOs returns "OK" response
    Given there is a valid "slo" in the system
    And new "SearchSLO" request
    And request contains "query" parameter from "slo.data[0].name"
    And request contains "page[size]" parameter with value 20
    And request contains "page[number]" parameter with value 0
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.slos[0].data.attributes.name" is equal to "{{ slo.data[0].name }}"
    And the response "data.attributes.slos[0].data.attributes.overall_status[0].error_budget_remaining" is equal to null
    And the response "data.attributes.slos[0].data.attributes.overall_status[0].status" is equal to null
    And the response "data.attributes.slos[0].data.attributes.status.state" is equal to "no_data"

  @team:DataDog/slo-app
  Scenario: Update an SLO returns "Bad Request" response
    Given new "UpdateSLO" request
    And there is a valid "slo" in the system
    And request contains "slo_id" parameter from "slo.data[0].id"
    And body with value {"type":"monitor","name":"{{ unique }}","thresholds":[{"target":95.0,"target_display":"95.0","timeframe":"7d","warning":98,"warning_display":"98.0"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/slo-app
  Scenario: Update an SLO returns "Not Found" response
    Given new "UpdateSLO" request
    And request contains "slo_id" parameter from "REPLACE.ME"
    And body with value {"description": null, "groups": ["env:prod", "role:mysql"], "monitor_ids": [], "monitor_tags": [], "name": "Custom Metric SLO", "query": {"denominator": "sum:my.custom.metric{*}.as_count()", "numerator": "sum:my.custom.metric{type:good}.as_count()"}, "sli_specification": {"time_slice": {"comparator": "<", "query": {"formulas": [{"formula": "query2/query1"}], "queries": [{"data_source": "metrics", "name": "query1", "query": "sum:trace.servlet.request.hits{*} by {env}.as_count()"}, {"data_source": "metrics", "name": "query1", "query": "sum:trace.servlet.request.errors{*} by {env}.as_count()"}]}, "threshold": 5}}, "tags": ["env:prod", "app:core"], "target_threshold": 99.9, "thresholds": [{"target": 95, "timeframe": "7d"}, {"target": 95, "timeframe": "30d", "warning": 97}], "timeframe": "30d", "type": "metric", "warning_threshold": 99.95}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/slo-app
  Scenario: Update an SLO returns "OK" response
    Given there is a valid "slo" in the system
    And new "UpdateSLO" request
    And request contains "slo_id" parameter from "slo.data[0].id"
    And body with value {"type":"metric","name":"{{ slo.data[0].name }}","thresholds":[{"target":97.0,"timeframe":"7d","warning":98.0}],"timeframe":"7d","target_threshold":97.0,"warning_threshold":98,"query":{"numerator":"sum:httpservice.hits{code:2xx}.as_count()","denominator":"sum:httpservice.hits{!code:3xx}.as_count()"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].thresholds[0].target" is equal to 97.0
    And the response "data[0].timeframe" is equal to "7d"
    And the response "data[0].target_threshold" is equal to 97.0
    And the response "data[0].warning_threshold" is equal to 98.0
