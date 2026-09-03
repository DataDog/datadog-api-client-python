@endpoint(ddsql) @endpoint(ddsql-v2)
Feature: DDSQL
  Execute DDSQL queries against the Datadog data catalog and poll for their
  results. Queries are dispatched asynchronously: the initial request may
  return a `running` state with a `query_id`, and clients poll the fetch
  endpoint until the response transitions to `completed` with a column-major
  result set.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DDSQL" API

  @generated @skip @team:DataDog/query-apis
  Scenario: Execute a tabular DDSQL query returns "Bad Request" response
    Given new "ExecuteDdsqlTabularQuery" request
    And body with value {"data": {"attributes": {"query": "SELECT cloud_provider, count(*) FROM dd.hosts group by cloud_provider", "row_limit": 1000, "time": {"from_timestamp": 1736942400000, "to_timestamp": 1736946000000}}, "type": "ddsql_query_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/query-apis
  Scenario: Execute a tabular DDSQL query returns "OK" response
    Given new "ExecuteDdsqlTabularQuery" request
    And body with value {"data": {"attributes": {"query": "SELECT cloud_provider, count(*) FROM dd.hosts group by cloud_provider", "row_limit": 1000, "time": {"from_timestamp": 1736942400000, "to_timestamp": 1736946000000}}, "type": "ddsql_query_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/query-apis
  Scenario: Fetch the result of a DDSQL query returns "Bad Request" response
    Given new "FetchDdsqlTabularQuery" request
    And body with value {"data": {"attributes": {"query_id": "eyJxdWVyeSI6ICJTRUxFQ1QgKiBGUk9NIGxvZ3MifQ=="}, "type": "ddsql_query_fetch_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/query-apis
  Scenario: Fetch the result of a DDSQL query returns "OK" response
    Given new "FetchDdsqlTabularQuery" request
    And body with value {"data": {"attributes": {"query_id": "eyJxdWVyeSI6ICJTRUxFQ1QgKiBGUk9NIGxvZ3MifQ=="}, "type": "ddsql_query_fetch_request"}}
    When the request is sent
    Then the response status is 200 OK
