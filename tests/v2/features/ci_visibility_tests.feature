@endpoint(ci-visibility-tests) @endpoint(ci-visibility-tests-v2)
Feature: CI Visibility Tests
  Search or aggregate your CI Visibility test events over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CIVisibilityTests" API

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Aggregate tests events returns "Bad Request" response
    Given new "AggregateCIAppTestEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "interval": "5m", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "@test.service:web-ui-tests AND @test.status:fail", "to": "now"}, "group_by": [{"facet": "@test.service", "histogram": {"interval": 10, "max": 100, "min": 50}, "limit": 10, "sort": {"aggregation": "count", "order": "asc"}, "total": false}], "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Aggregate tests events returns "OK" response
    Given new "AggregateCIAppTestEvents" request
    And body with value {"compute": [{"aggregation": "count", "metric": "@test.is_flaky", "type": "total"}], "filter": {"from": "now-15m", "query": "@language:(python OR go)", "to": "now"}, "group_by": [{"facet": "@git.branch", "limit": 10, "sort": {"order": "asc"}, "total": false}], "options": {"timezone": "GMT"}, "page": {"limit": 25}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Get a list of tests events returns "Bad Request" response
    Given new "ListCIAppTestEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Get a list of tests events returns "OK" response
    Given new "ListCIAppTestEvents" request
    And request contains "filter[query]" parameter with value "@test.service:web-ui-tests"
    And request contains "filter[from]" parameter with value "{{ timeISO('now - 30s') }}"
    And request contains "filter[to]" parameter with value "{{ timeISO('now') }}"
    And request contains "page[limit]" parameter with value 5
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries @with-pagination
  Scenario: Get a list of tests events returns "OK" response with pagination
    Given new "ListCIAppTestEvents" request
    And request contains "filter[from]" parameter with value "{{ timeISO('now - 30s') }}"
    And request contains "filter[to]" parameter with value "{{ timeISO('now') }}"
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Search tests events returns "Bad Request" response
    Given new "SearchCIAppTestEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@test.service:web-ui-tests AND @test.status:fail", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Search tests events returns "OK" response
    Given new "SearchCIAppTestEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@test.service:web-ui-tests AND @test.status:skip", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries @with-pagination
  Scenario: Search tests events returns "OK" response with pagination
    Given new "SearchCIAppTestEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@test.status:pass AND -@language:python", "to": "now"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items
