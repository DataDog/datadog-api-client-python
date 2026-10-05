@endpoint(logs-archive-searches) @endpoint(logs-archive-searches-v2)
Feature: Logs Archive Searches
  Search the logs stored in a Logs Archive without reindexing them, and
  optionally rehydrate the matches into a retained historical view.  See the
  [Rehydrating from
  Archives](https://app.datadoghq.com/logs/pipelines/historical-views) page
  for the searches currently running in Datadog.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsArchiveSearches" API

  @generated @skip @team:ddoghq/logs-federated-search @team:ddoghq/logs-routing
  Scenario: Create an Archive Search returns "Bad Request" response
    Given operation "CreateArchiveSearch" enabled
    And new "CreateArchiveSearch" request
    And body with value {"data": {"attributes": {"archive_id": "mhmyYmyLTOaFYKvhNadu1w", "description": "Investigating the checkout latency spike.", "from": "2026-01-01T00:00:00Z", "name": "checkout-latency-investigation", "query": "service:checkout status:error", "rehydration": {"max_rehydrated_events": 1000000, "retention_days": 15, "tier": "standard"}, "to": "2026-01-02T00:00:00Z"}, "type": "archive_search"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/logs-federated-search @team:ddoghq/logs-routing
  Scenario: Create an Archive Search returns "Not Found" response
    Given operation "CreateArchiveSearch" enabled
    And new "CreateArchiveSearch" request
    And body with value {"data": {"attributes": {"archive_id": "mhmyYmyLTOaFYKvhNadu1w", "description": "Investigating the checkout latency spike.", "from": "2026-01-01T00:00:00Z", "name": "checkout-latency-investigation", "query": "service:checkout status:error", "rehydration": {"max_rehydrated_events": 1000000, "retention_days": 15, "tier": "standard"}, "to": "2026-01-02T00:00:00Z"}, "type": "archive_search"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/logs-federated-search @team:ddoghq/logs-routing
  Scenario: Create an Archive Search returns "OK" response
    Given operation "CreateArchiveSearch" enabled
    And new "CreateArchiveSearch" request
    And body with value {"data": {"attributes": {"archive_id": "mhmyYmyLTOaFYKvhNadu1w", "description": "Investigating the checkout latency spike.", "from": "2026-01-01T00:00:00Z", "name": "checkout-latency-investigation", "query": "service:checkout status:error", "rehydration": {"max_rehydrated_events": 1000000, "retention_days": 15, "tier": "standard"}, "to": "2026-01-02T00:00:00Z"}, "type": "archive_search"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/logs-federated-search @team:ddoghq/logs-routing
  Scenario: Get an Archive Search returns "Bad Request" response
    Given operation "GetArchiveSearch" enabled
    And new "GetArchiveSearch" request
    And request contains "archive_search_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/logs-federated-search @team:ddoghq/logs-routing
  Scenario: Get an Archive Search returns "Not Found" response
    Given operation "GetArchiveSearch" enabled
    And new "GetArchiveSearch" request
    And request contains "archive_search_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/logs-federated-search @team:ddoghq/logs-routing
  Scenario: Get an Archive Search returns "OK" response
    Given operation "GetArchiveSearch" enabled
    And new "GetArchiveSearch" request
    And request contains "archive_search_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
