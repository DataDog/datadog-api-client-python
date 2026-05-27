@endpoint(rum-replay-analysis) @endpoint(rum-replay-analysis-v2)
Feature: Rum Replay Analysis
  Analyze RUM replay sessions to identify and investigate user-facing
  issues. Retrieve issues detected by AI analysis, get details for
  individual issues, and explore the sessions associated with each issue.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumReplayAnalysis" API

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Get replay analysis issue returns "Bad Request" response
    Given operation "GetReplayAnalysisIssue" enabled
    And new "GetReplayAnalysisIssue" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Get replay analysis issue returns "Not Found" response
    Given operation "GetReplayAnalysisIssue" enabled
    And new "GetReplayAnalysisIssue" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Get replay analysis issue returns "OK" response
    Given operation "GetReplayAnalysisIssue" enabled
    And new "GetReplayAnalysisIssue" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List replay analysis issue sessions returns "Bad Request" response
    Given operation "ListReplayAnalysisIssueSessions" enabled
    And new "ListReplayAnalysisIssueSessions" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List replay analysis issue sessions returns "Not Found" response
    Given operation "ListReplayAnalysisIssueSessions" enabled
    And new "ListReplayAnalysisIssueSessions" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List replay analysis issue sessions returns "OK" response
    Given operation "ListReplayAnalysisIssueSessions" enabled
    And new "ListReplayAnalysisIssueSessions" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List replay analysis issues returns "Bad Request" response
    Given operation "ListReplayAnalysisIssues" enabled
    And new "ListReplayAnalysisIssues" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List replay analysis issues returns "OK" response
    Given operation "ListReplayAnalysisIssues" enabled
    And new "ListReplayAnalysisIssues" request
    When the request is sent
    Then the response status is 200 OK
