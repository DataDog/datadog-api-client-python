@endpoint(ci-visibility-pipelines) @endpoint(ci-visibility-pipelines-v2)
Feature: CI Visibility Pipelines
  Search or aggregate your CI Visibility pipeline events over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CIVisibilityPipelines" API

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Aggregate pipelines events returns "Bad Request" response
    Given new "AggregateCIAppPipelineEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "interval": "5m", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "@ci.provider.name:github AND @ci.status:error", "to": "now"}, "group_by": [{"facet": "@ci.status", "histogram": {"interval": 10, "max": 100, "min": 50}, "limit": 10, "sort": {"aggregation": "count", "order": "asc"}, "total": false}], "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Aggregate pipelines events returns "OK" response
    Given new "AggregateCIAppPipelineEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "@ci.provider.name:(gitlab OR github)", "to": "now"}, "group_by": [{ "facet": "@ci.status", "limit": 10, "total": false}], "options": {"timezone": "GMT"}, "page": {"limit": 25}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Get a list of pipelines events returns "Bad Request" response
    Given new "ListCIAppPipelineEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Get a list of pipelines events returns "OK" response
    Given new "ListCIAppPipelineEvents" request
    And request contains "filter[query]" parameter with value "@ci.provider.name:circleci"
    And request contains "filter[from]" parameter with value "{{ timeISO('now - 30m') }}"
    And request contains "filter[to]" parameter with value "{{ timeISO('now') }}"
    And request contains "page[limit]" parameter with value 5
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries @with-pagination
  Scenario: Get a list of pipelines events returns "OK" response with pagination
    Given new "ListCIAppPipelineEvents" request
    And request contains "filter[from]" parameter with value "{{ timeISO('now - 30s') }}"
    And request contains "filter[to]" parameter with value "{{ timeISO('now') }}"
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Search pipelines events returns "Bad Request" response
    Given new "SearchCIAppPipelineEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@ci.provider.name:github AND @ci.status:error", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Search pipelines events returns "OK" response
    Given new "SearchCIAppPipelineEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@ci.provider.name:github AND @ci.status:error", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 5}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries @with-pagination
  Scenario: Search pipelines events returns "OK" response with pagination
    Given new "SearchCIAppPipelineEvents" request
    And body with value {"filter": {"from": "now-30s", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items
