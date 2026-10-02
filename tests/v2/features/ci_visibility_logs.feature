@endpoint(ci-visibility-logs) @endpoint(ci-visibility-logs-v2)
Feature: CI Visibility Logs
  Send CI job logs over HTTP for CI Visibility.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "CIVisibilityLogs" API
    And new "SubmitCILog" request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send CI job logs returns "Bad Request" response
    Given body with value [{"ddtags": "runner:linux,architecture:amd64", "job_id": "job-456", "line_number": 812, "message": "Running go test ./...", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "provider_name": "example-provider", "section_name": "tests", "status": "warn"}]
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send CI job logs returns "Payload Too Large" response
    Given body with value [{"ddtags": "runner:linux,architecture:amd64", "job_id": "job-456", "line_number": 812, "message": "Running go test ./...", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "provider_name": "example-provider", "section_name": "tests", "status": "warn"}]
    When the request is sent
    Then the response status is 413 Payload Too Large

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send CI job logs returns "Request Timeout" response
    Given body with value [{"ddtags": "runner:linux,architecture:amd64", "job_id": "job-456", "line_number": 812, "message": "Running go test ./...", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "provider_name": "example-provider", "section_name": "tests", "status": "warn"}]
    When the request is sent
    Then the response status is 408 Request Timeout

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send CI job logs returns "Request accepted for processing" response
    Given body with value [{"ddtags": "runner:linux,architecture:amd64", "job_id": "job-456", "line_number": 812, "message": "Running go test ./...", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "provider_name": "example-provider", "section_name": "tests", "status": "warn"}]
    When the request is sent
    Then the response status is 202 Request accepted for processing

  @team:DataDog/ci-app-backend
  Scenario: Send batched CI job logs returns "Request accepted for processing" response
    Given body with value [{"message": "Starting tests", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "job_id": "job-456", "line_number": 1, "status": "notice", "section_name": "tests"}, {"message": "Tests passed", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "job_id": "job-456", "line_number": 2}]
    When the request is sent
    Then the response status is 202 Request accepted for processing

  @team:DataDog/ci-app-backend
  Scenario: Send one CI job log returns "Request accepted for processing" response
    Given body with value [{"message": "Running go test ./...", "pipeline_unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a", "job_id": "job-456", "provider_name": "example-provider", "line_number": 1, "status": "warn", "section_name": "tests", "ddtags": "runner:linux,architecture:amd64"}]
    When the request is sent
    Then the response status is 202 Request accepted for processing
