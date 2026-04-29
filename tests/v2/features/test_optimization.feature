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
  Scenario: Delete Test Optimization service settings returns "Bad Request" response
    Given new "DeleteTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "github.com/datadog/shopist", "service_name": "shopist"}, "type": "test_optimization_delete_service_settings_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Delete Test Optimization service settings returns "No Content" response
    Given new "DeleteTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "github.com/datadog/shopist", "service_name": "shopist"}, "type": "test_optimization_delete_service_settings_request"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Delete Test Optimization service settings returns "Not Found" response
    Given new "DeleteTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "github.com/datadog/shopist", "service_name": "shopist"}, "type": "test_optimization_delete_service_settings_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get Flaky Tests Management policies returns "Bad Request" response
    Given new "GetFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist"}, "type": "test_optimization_get_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get Flaky Tests Management policies returns "Not Found" response
    Given new "GetFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist"}, "type": "test_optimization_get_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get Flaky Tests Management policies returns "OK" response
    Given new "GetFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist"}, "type": "test_optimization_get_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Get Flaky Tests Management policies with empty repository_id returns bad request
    Given operation "GetFlakyTestsManagementPolicies" enabled
    And new "GetFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"repository_id": ""}, "type": "test_optimization_get_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get Test Optimization service settings returns "Bad Request" response
    Given new "GetTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "github.com/datadog/shopist", "service_name": "shopist"}, "type": "test_optimization_get_service_settings_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get Test Optimization service settings returns "Not Found" response
    Given new "GetTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "github.com/datadog/shopist", "service_name": "shopist"}, "type": "test_optimization_get_service_settings_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get Test Optimization service settings returns "OK" response
    Given new "GetTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "github.com/datadog/shopist", "service_name": "shopist"}, "type": "test_optimization_get_service_settings_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Get Test Optimization service settings with empty env returns bad request
    Given operation "GetTestOptimizationServiceSettings" enabled
    And new "GetTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "", "repository_id": "github.com/datadog/shopist", "service_name": "shopist"}, "type": "test_optimization_get_service_settings_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get Test Optimization service settings with empty repository_id returns bad request
    Given operation "GetTestOptimizationServiceSettings" enabled
    And new "GetTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "", "service_name": "shopist"}, "type": "test_optimization_get_service_settings_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get Test Optimization service settings with empty service_name returns bad request
    Given operation "GetTestOptimizationServiceSettings" enabled
    And new "GetTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "github.com/datadog/shopist", "service_name": ""}, "type": "test_optimization_get_service_settings_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Search flaky tests returns "Bad Request" response
    Given new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"include_history": true, "query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
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
    Given new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"include_history": true, "query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
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
    And body with value {"data": {"attributes": {"filter": {"query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\"", "include_history": true}, "page": {"limit": 10}, "sort": "fqn"}, "type": "search_flaky_tests_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes" has field "history"
    And the response "data[0].attributes.history[0]" has field "status"
    And the response "data[0].attributes.history[0]" has field "commit_sha"
    And the response "data[0].attributes.history[0]" has field "timestamp"
    And the response "data[0].attributes.history[0]" has field "policy_id"
    And the response "data[0].attributes.history[0]" has field "policy_meta"

  @generated @skip @team:DataDog/ci-app-backend @with-pagination
  Scenario: Search flaky tests returns "OK" response with pagination
    Given new "SearchFlakyTests" request
    And body with value {"data": {"attributes": {"filter": {"include_history": true, "query": "flaky_test_state:active @git.repository.id_v2:\"github.com/datadog/shopist\""}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "failure_rate"}, "type": "search_flaky_tests_request"}}
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update Flaky Tests Management policies returns "Bad Request" response
    Given new "UpdateFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"attempt_to_fix": {"retries": 3}, "disabled": {"auto_disable_rule": {"enabled": false, "status": "active", "window_seconds": 3600}, "branch_rule": {"branches": ["main"], "enabled": true, "excluded_branches": [], "excluded_test_services": []}, "enabled": false, "failure_rate_rule": {"branches": [], "enabled": false, "min_runs": 10, "status": "active", "threshold": 0.5}}, "quarantined": {"auto_quarantine_rule": {"enabled": true, "window_seconds": 3600}, "branch_rule": {"branches": ["main"], "enabled": true, "excluded_branches": [], "excluded_test_services": []}, "enabled": true, "failure_rate_rule": {"branches": ["main"], "enabled": true, "min_runs": 10, "threshold": 0.5}}, "repository_id": "github.com/datadog/shopist"}, "type": "test_optimization_update_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update Flaky Tests Management policies returns "Not Found" response
    Given new "UpdateFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"attempt_to_fix": {"retries": 3}, "disabled": {"auto_disable_rule": {"enabled": false, "status": "active", "window_seconds": 3600}, "branch_rule": {"branches": ["main"], "enabled": true, "excluded_branches": [], "excluded_test_services": []}, "enabled": false, "failure_rate_rule": {"branches": [], "enabled": false, "min_runs": 10, "status": "active", "threshold": 0.5}}, "quarantined": {"auto_quarantine_rule": {"enabled": true, "window_seconds": 3600}, "branch_rule": {"branches": ["main"], "enabled": true, "excluded_branches": [], "excluded_test_services": []}, "enabled": true, "failure_rate_rule": {"branches": ["main"], "enabled": true, "min_runs": 10, "threshold": 0.5}}, "repository_id": "github.com/datadog/shopist"}, "type": "test_optimization_update_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update Flaky Tests Management policies returns "OK" response
    Given new "UpdateFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"attempt_to_fix": {"retries": 3}, "disabled": {"auto_disable_rule": {"enabled": false, "status": "active", "window_seconds": 3600}, "branch_rule": {"branches": ["main"], "enabled": true, "excluded_branches": [], "excluded_test_services": []}, "enabled": false, "failure_rate_rule": {"branches": [], "enabled": false, "min_runs": 10, "status": "active", "threshold": 0.5}}, "quarantined": {"auto_quarantine_rule": {"enabled": true, "window_seconds": 3600}, "branch_rule": {"branches": ["main"], "enabled": true, "excluded_branches": [], "excluded_test_services": []}, "enabled": true, "failure_rate_rule": {"branches": ["main"], "enabled": true, "min_runs": 10, "threshold": 0.5}}, "repository_id": "github.com/datadog/shopist"}, "type": "test_optimization_update_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Update Flaky Tests Management policies with empty repository_id returns bad request
    Given operation "UpdateFlakyTestsManagementPolicies" enabled
    And new "UpdateFlakyTestsManagementPolicies" request
    And body with value {"data": {"attributes": {"repository_id": ""}, "type": "test_optimization_update_flaky_tests_management_policies_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update Test Optimization service settings returns "Bad Request" response
    Given new "UpdateTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"auto_test_retries_enabled": false, "code_coverage_enabled": false, "early_flake_detection_enabled": false, "env": "prod", "failed_test_replay_enabled": false, "pr_comments_enabled": true, "repository_id": "github.com/datadog/shopist", "service_name": "shopist", "test_impact_analysis_enabled": false}, "type": "test_optimization_update_service_settings_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update Test Optimization service settings returns "Not Found" response
    Given new "UpdateTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"auto_test_retries_enabled": false, "code_coverage_enabled": false, "early_flake_detection_enabled": false, "env": "prod", "failed_test_replay_enabled": false, "pr_comments_enabled": true, "repository_id": "github.com/datadog/shopist", "service_name": "shopist", "test_impact_analysis_enabled": false}, "type": "test_optimization_update_service_settings_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update Test Optimization service settings returns "OK" response
    Given new "UpdateTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"auto_test_retries_enabled": false, "code_coverage_enabled": false, "early_flake_detection_enabled": false, "env": "prod", "failed_test_replay_enabled": false, "pr_comments_enabled": true, "repository_id": "github.com/datadog/shopist", "service_name": "shopist", "test_impact_analysis_enabled": false}, "type": "test_optimization_update_service_settings_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Update Test Optimization service settings with empty repository_id returns bad request
    Given operation "UpdateTestOptimizationServiceSettings" enabled
    And new "UpdateTestOptimizationServiceSettings" request
    And body with value {"data": {"attributes": {"env": "prod", "repository_id": "", "service_name": "shopist"}, "type": "test_optimization_update_service_settings_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update flaky test states returns "Bad Request" response
    Given new "UpdateFlakyTests" request
    And body with value {"data": {"attributes": {"tests": [{"id": "4eb1887a8adb1847", "new_state": "active"}]}, "type": "update_flaky_test_state_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update flaky test states returns "OK" response
    Given new "UpdateFlakyTests" request
    And body with value {"data": {"attributes": {"tests": [{"id": "4eb1887a8adb1847", "new_state": "active"}]}, "type": "update_flaky_test_state_request"}}
    When the request is sent
    Then the response status is 200 OK
