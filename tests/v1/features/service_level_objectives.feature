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
  Scenario: Create an SLO object returns "Bad Request" response
    Given new "CreateSLO" request
    And body with value {"type":"monitor","name":"{{ unique }}","thresholds":[{"target":95.0,"target_display":"95.0","timeframe":"7d","warning":98,"warning_display":"98.0"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/slo-app
  Scenario: Create an SLO object returns "OK" response
    Given new "CreateSLO" request
    And body with value {"type":"metric","description":"string","groups":["env:test","role:mysql"],"monitor_ids":[],"name":"{{ unique }}","query":{"denominator":"sum:httpservice.hits{!code:3xx}.as_count()","numerator":"sum:httpservice.hits{code:2xx}.as_count()"},"tags":["env:prod","app:core"],"thresholds":[{"target":95.0,"target_display":"95.0","timeframe":"7d","warning":98,"warning_display":"98.0"}],"timeframe":"7d","target_threshold":97.0,"warning_threshold":98}
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
    Given operation "SearchSLO" enabled
    And new "SearchSLO" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/slo-app
  Scenario: Search for SLOs returns "OK" response
    Given there is a valid "slo" in the system
    And operation "SearchSLO" enabled
    And new "SearchSLO" request
    And request contains "query" parameter from "slo.data[0].name"
    And request contains "page[size]" parameter with value 20
    And request contains "page[number]" parameter with value 0
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.slos[0].data.attributes.name" is equal to "{{ slo.data[0].name }}"

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
    And body with value null
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
