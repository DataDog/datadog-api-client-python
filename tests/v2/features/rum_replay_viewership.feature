@endpoint(rum-replay-viewership) @endpoint(rum-replay-viewership-v2)
Feature: Rum Replay Viewership
  Track and manage RUM replay session viewership. Monitor who watches replay
  sessions and maintain watch history for audit and analytics purposes.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumReplayViewership" API

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Create rum replay session watch returns "Created" response
    Given new "CreateRumReplaySessionWatch" request
    And request contains "session_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"application_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb", "event_id": "11111111-2222-3333-4444-555555555555", "timestamp": "2026-01-13T17:15:53.208340Z"}, "type": "rum_replay_watch"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Delete rum replay session watch returns "No Content" response
    Given new "DeleteRumReplaySessionWatch" request
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List rum replay session watchers returns "OK" response
    Given new "ListRumReplaySessionWatchers" request
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List rum replay viewership history sessions returns "OK" response
    Given new "ListRumReplayViewershipHistorySessions" request
    When the request is sent
    Then the response status is 200 OK
