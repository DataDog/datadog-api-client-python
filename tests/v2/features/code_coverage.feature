@endpoint(code-coverage) @endpoint(code-coverage-v2)
Feature: Code Coverage
  Retrieve and analyze code coverage data from Code Coverage. See the [Code
  Coverage page](https://docs.datadoghq.com/code_coverage/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CodeCoverage" API

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a branch returns "Bad Request" response
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"branch": "prod", "repository_id": "github.com/datadog/shopist"}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a branch returns "Not Found" response
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"branch": "prod", "repository_id": "github.com/datadog/shopist"}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a branch returns "OK" response
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"branch": "prod", "repository_id": "github.com/datadog/shopist"}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a branch with empty branch name returns bad request
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist", "branch": ""}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a branch with empty repository_id returns bad request
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"repository_id": "", "branch": "prod"}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a commit in nonexistent repository returns not found
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/nonexistent-repo", "commit_sha": "c55b0ce584e139bde41a00002ab31bc7d75f791d"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a commit returns "Bad Request" response
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_id": "github.com/datadog/shopist"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a commit returns "Not Found" response
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_id": "github.com/datadog/shopist"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a commit returns "OK" response
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_id": "github.com/datadog/shopist"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a commit with empty commit_sha returns bad request
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist", "commit_sha": ""}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a commit with empty repository_id returns bad request
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"repository_id": "", "commit_sha": "c55b0ce584e139bde41a00002ab31bc7d75f791d"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a commit with invalid commit SHA returns bad request
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist", "commit_sha": "abc123"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a nonexistent branch returns not found
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist", "branch": "nonexistent-branch"}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a nonexistent commit returns not found
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist", "commit_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for a nonexistent repository returns not found
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/nonexistent-repo", "branch": "main"}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for an existing branch with valid repository
    Given operation "GetCodeCoverageBranchSummary" enabled
    And new "GetCodeCoverageBranchSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist", "branch": "prod"}, "type": "ci_app_coverage_branch_summary_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "ci_app_coverage_branch_summary"
    And the response "data.attributes" has field "total_coverage"
    And the response "data.attributes" has field "patch_coverage"
    And the response "data.attributes" has field "evaluated_reports_count"
    And the response "data.attributes" has field "evaluated_flags_count"

  @skip @team:DataDog/ci-app-backend
  Scenario: Get code coverage summary for an existing commit with valid repository
    Given operation "GetCodeCoverageCommitSummary" enabled
    And new "GetCodeCoverageCommitSummary" request
    And body with value {"data": {"attributes": {"repository_id": "github.com/datadog/shopist", "commit_sha": "c55b0ce584e139bde41a00002ab31bc7d75f791d"}, "type": "ci_app_coverage_commit_summary_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "ci_app_coverage_commit_summary"
    And the response "data.attributes" has field "total_coverage"
    And the response "data.attributes" has field "patch_coverage"
    And the response "data.attributes" has field "evaluated_reports_count"
    And the response "data.attributes" has field "evaluated_flags_count"
