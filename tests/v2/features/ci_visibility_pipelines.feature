@endpoint(ci-visibility-pipelines) @endpoint(ci-visibility-pipelines-v2)
Feature: CI Visibility Pipelines
  Search or aggregate your CI Visibility pipeline events and send them to
  your Datadog site over HTTP.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "CIVisibilityPipelines" API

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Aggregate pipelines events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "AggregateCIAppPipelineEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "interval": "5m", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "@ci.provider.name:github AND @ci.status:error", "to": "now"}, "group_by": [{"facet": "@ci.status", "histogram": {"interval": 10, "max": 100, "min": 50}, "limit": 10, "sort": {"aggregation": "count", "order": "asc"}, "total": false}], "options": {"timezone": "GMT"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Aggregate pipelines events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "AggregateCIAppPipelineEvents" request
    And body with value {"compute": [{"aggregation": "pc90", "metric": "@duration", "type": "total"}], "filter": {"from": "now-15m", "query": "@ci.provider.name:(gitlab OR github)", "to": "now"}, "group_by": [{ "facet": "@ci.status", "limit": 10, "total": false}], "options": {"timezone": "GMT"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.status" is equal to "done"

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Get a list of pipelines events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListCIAppPipelineEvents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Get a list of pipelines events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListCIAppPipelineEvents" request
    And request contains "filter[query]" parameter with value "@ci.provider.name:circleci"
    And request contains "filter[from]" parameter with value "{{ timeISO('now - 30m') }}"
    And request contains "filter[to]" parameter with value "{{ timeISO('now') }}"
    And request contains "page[limit]" parameter with value 5
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries @with-pagination
  Scenario: Get a list of pipelines events returns "OK" response with pagination
    Given a valid "appKeyAuth" key in the system
    And new "ListCIAppPipelineEvents" request
    And request contains "filter[from]" parameter with value "{{ timeISO('now - 30s') }}"
    And request contains "filter[to]" parameter with value "{{ timeISO('now') }}"
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Search pipelines events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "SearchCIAppPipelineEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@ci.provider.name:github AND @ci.status:error", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Search pipelines events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "SearchCIAppPipelineEvents" request
    And body with value {"filter": {"from": "now-15m", "query": "@ci.provider.name:github AND @ci.status:error", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 5}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries @with-pagination
  Scenario: Search pipelines events returns "OK" response with pagination
    Given a valid "appKeyAuth" key in the system
    And new "SearchCIAppPipelineEvents" request
    And body with value {"filter": {"from": "now-30s", "to": "now"}, "options": {"timezone": "GMT"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Send pipeline event returns "Bad Request" response
    Given new "CreateCIAppPipelineEvent" request
    And body with value {"data": {"attributes": {"resource": "Details TBD"}, "type": "cipipeline_resource_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Send pipeline event returns "Payload Too Large" response
    Given new "CreateCIAppPipelineEvent" request
    And body with value {"data": {"attributes": {"resource": "Details TBD"}, "type": "cipipeline_resource_request"}}
    When the request is sent
    Then the response status is 413 Payload Too Large

  @generated @skip @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Send pipeline event returns "Request Timeout" response
    Given new "CreateCIAppPipelineEvent" request
    And body with value {"data": {"attributes": {"resource": "Details TBD"}, "type": "cipipeline_resource_request"}}
    When the request is sent
    Then the response status is 408 Request Timeout

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Send pipeline event returns "Request accepted for processing" response
    Given new "CreateCIAppPipelineEvent" request
    And body with value {"data": {"attributes": {"resource": {"end": "{{ timeISO('now - 30s') }}", "level": "pipeline", "name": "Deploy to AWS", "partial_retry": false, "start": "{{ timeISO('now - 120s') }}", "status": "success", "unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "url": "https://my-ci-provider.example/pipelines/my-pipeline/run/1","git":{"repository_url":"https://github.com/DataDog/datadog-agent","sha":"7f263865994b76066c4612fd1965215e7dcb4cd2","author_email":"john.doe@email.com"}}}, "type": "cipipeline_resource_request"}}
    When the request is sent
    Then the response status is 202 Request accepted for processing

  @team:Datadog/ci-app-backend @team:Datadog/integrations-tools-and-libraries
  Scenario: Send pipeline job event returns "Request accepted for processing" response
    Given new "CreateCIAppPipelineEvent" request
    And body with value {"data": {"attributes": {"resource": {"end": "{{ timeISO('now - 30s') }}", "level": "job", "name": "Build image", "start": "{{ timeISO('now - 120s') }}", "status": "error", "id": "cf9456de-8b9e-4c27-aa79-27b1e78c1a33", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "pipeline_name": "Deploy to AWS", "url": "https://my-ci-provider.example/jobs/my-jobs/run/1"}}, "type": "cipipeline_resource_request"}}
    When the request is sent
    Then the response status is 202 Request accepted for processing
