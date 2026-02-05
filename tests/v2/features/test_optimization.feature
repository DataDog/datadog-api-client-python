@endpoint(test-optimization) @endpoint(test-optimization-v2)
Feature: Test Optimization
  Search and manage flaky tests through Test Optimization. See the [Test
  Optimization page](https://docs.datadoghq.com/tests/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TestOptimization" API

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "Bad Request" response
    Given operation "SearchFlakyTests" enabled
    And new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "include_history": true, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "Bad Request" response with invalid limit
    Given operation "SearchFlakyTests" enabled
    And new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"query": "*"}, "page": {"limit": 2000}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "OK" response
    Given operation "SearchFlakyTests" enabled
    And new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "include_history": true, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip @skip-validation @team:DataDog/ci-app-backend @with-pagination
  Scenario: Search flaky tests returns "OK" response with filtered query
    Given operation "SearchFlakyTests" enabled
    And new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/cart-tracking\""}, "page": {"limit": 10}, "sort": "-last_flaked"}, "type": "search_flaky_tests_request"}}
    When the request with pagination is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "OK" response with history
    Given operation "SearchFlakyTests" enabled
    And new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"limit": 10}, "sort": "fqn", "include_history": true}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes" has field "history"
    And the response "data[0].attributes.history[0]" has field "status"
    And the response "data[0].attributes.history[0]" has field "commit_sha"
    And the response "data[0].attributes.history[0]" has field "timestamp"

  @generated @skip @team:DataDog/ci-app-backend @with-pagination
  Scenario: Search flaky tests returns "OK" response with pagination
    Given operation "SearchFlakyTests" enabled
    And new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "include_history": true, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update flaky test states returns "Bad Request" response
    Given operation "UpdateFlakyTests" enabled
    And new "UpdateFlakyTests" request
    And body with value {"data": {"attributes": {"tests": [{"id": "4eb1887a8adb1847", "new_state": "active"}]}, "type": "update_flaky_test_state_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update flaky test states returns "OK" response
    Given operation "UpdateFlakyTests" enabled
    And new "UpdateFlakyTests" request
    And body with value {"data": {"attributes": {"tests": [{"id": "4eb1887a8adb1847", "new_state": "active"}]}, "type": "update_flaky_test_state_request"}}
    When the request is sent
    Then the response status is 200 OK
