@endpoint(test-optimization) @endpoint(test-optimization-v2)
Feature: Test Optimization
  Search and manage flaky tests through Test Optimization. See the [Test
  Optimization page](https://docs.datadoghq.com/tests/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TestOptimization" API
    And new "SearchFlakyTests" request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "Bad Request" response
    Given operation "SearchFlakyTests" enabled
    And body with value {"data": {"attributes": {"filter": {"query": "*"}, "page": {"limit": 10}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "Bad Request" response with invalid limit
    Given operation "SearchFlakyTests" enabled
    And body with value {"data": {"attributes": {"filter": {"query": "*"}, "page": {"limit": 2000}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "OK" response
    Given operation "SearchFlakyTests" enabled
    And body with value {"data": {"attributes": {"filter": {"query": "*"}, "page": {"limit": 10}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/ci-app-backend @with-pagination
  Scenario: Search flaky tests returns "OK" response with cursor pagination
    Given body with value {"data": {"attributes": {"filter": {"query": "*"}, "page": {"limit": 2}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 2 items
    And the response "meta.pagination" has field "next_page"

  @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "OK" response with filtered query
    Given operation "SearchFlakyTests" enabled
    And body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"limit": 2}, "sort": "-last_flaked"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "OK" response with specific cursor
    Given operation "SearchFlakyTests" enabled
    And body with value {"data": {"attributes": {"filter": {"query": "*"}, "page": {"cursor": "Q29udGludW91cyBUZXN0aW5nLltETyBOT1QgREVMRVRFXVtPTi1ERU1BTkQgRlVOQ1RJT05BTElUSUVTXVtPVkVSUklERV0gRXh0cmFWYXJpYWJsZXM=", "limit": 2}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 200 OK
