@endpoint(rum-replay) @endpoint(rum-replay-v2)
Feature: Rum Replay
  Generate and retrieve AI-powered summaries of RUM replay sessions.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumReplay" API
    And operation "GenerateReplaySummary" enabled
    And new "GenerateReplaySummary" request
    And body with value {"data": {"type": "replay_summary_request"}}

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Generate replay summary returns "Bad Request" response
    Given request contains "session_id" parameter from "REPLACE.ME"
    And request contains "data_source" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Generate replay summary returns "Not Found" response
    Given request contains "session_id" parameter from "REPLACE.ME"
    And request contains "data_source" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Generate replay summary returns "OK" response
    Given request contains "session_id" parameter from "REPLACE.ME"
    And request contains "data_source" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
