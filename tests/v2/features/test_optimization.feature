@endpoint(test-optimization) @endpoint(test-optimization-v2)
Feature: Test Optimization
  Search and manage flaky tests through Test Optimization. See the [Test
  Optimization page](https://docs.datadoghq.com/tests/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TestOptimization" API
    And operation "SearchFlakyTests" enabled
    And new "SearchFlakyTests" request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "Bad Request" response
    Given body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "Bad Request" response with invalid limit
    Given body with value {"data": {"attributes": {"filter": {"query": "*"}, "page": {"limit": 2000}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "OK" response
    Given body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip @skip-validation @team:DataDog/ci-app-backend @with-pagination
  Scenario: Search flaky tests returns "OK" response with filtered query
    Given body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/cart-tracking\""}, "page": {"limit": 10}, "sort": "-last_flaked"}, "type": "search_flaky_tests_request"}}
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend @with-pagination
  Scenario: Search flaky tests returns "OK" response with pagination
    Given body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
    When the request with pagination is sent
    Then the response status is 200 OK
